/**
 * FS Manager - Core: API, theme, tabs, settings, context menu, helpers
 */

const API = {
    async get(url) {
        const res = await fetch(url);
        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: res.statusText }));
            throw new Error(err.detail || res.statusText);
        }
        return res.json();
    },
    async post(url, data) {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: res.statusText }));
            throw new Error(err.detail || res.statusText);
        }
        return res.json();
    },
    async del(url) {
        const res = await fetch(url, { method: "DELETE" });
        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: res.statusText }));
            throw new Error(err.detail || res.statusText);
        }
        return res.json();
    },
};

// --- Theme ---
const themeBtn = document.getElementById("btn-theme");
function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    themeBtn.textContent = theme === "dark" ? "\u2600" : "\u263E";
    themeBtn.title = theme === "dark" ? "Light mode" : "Dark mode";
    localStorage.setItem("fs-manager-theme", theme);
}
themeBtn.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme");
    applyTheme(cur === "dark" ? "light" : "dark");
});
applyTheme(localStorage.getItem("fs-manager-theme") || "light");

// --- Tabs ---
const tabs = document.querySelectorAll(".tab-bar .tab");
const tabContents = document.querySelectorAll(".tab-content");
tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("active"));
        tabContents.forEach(tc => tc.classList.remove("active"));
        tab.classList.add("active");
        document.getElementById("tab-" + tab.dataset.tab).classList.add("active");
    });
});

// --- Dialogs ---
document.querySelectorAll(".close-dialog").forEach(btn => {
    btn.addEventListener("click", () => btn.closest("dialog").close());
});

// --- Settings ---
function getSetting(key, fallback) {
    try {
        const s = JSON.parse(localStorage.getItem("fs-manager-settings") || "{}");
        return s[key] !== undefined ? s[key] : fallback;
    } catch { return fallback; }
}

function setSetting(key, value) {
    try {
        const s = JSON.parse(localStorage.getItem("fs-manager-settings") || "{}");
        s[key] = value;
        localStorage.setItem("fs-manager-settings", JSON.stringify(s));
    } catch { /* ignore */ }
}

document.getElementById("btn-settings").addEventListener("click", () => {
    document.getElementById("default-open-action").value = getSetting("defaultAction", "word");
    document.getElementById("settings-dialog").showModal();
});

document.getElementById("btn-save-settings").addEventListener("click", () => {
    setSetting("defaultAction", document.getElementById("default-open-action").value);
    document.getElementById("settings-dialog").close();
});

// --- Context menu ---
const ctxMenu = document.getElementById("context-menu");

function showContextMenu(x, y, items) {
    ctxMenu.innerHTML = items.map(item => {
        if (item.separator) return '<div class="ctx-separator"></div>';
        const cls = "ctx-item" + (item.danger ? " danger" : "");
        return '<div class="' + cls + '" data-ctx="' + item.action + '">' + item.label + '</div>';
    }).join("");
    // Position
    ctxMenu.style.left = x + "px";
    ctxMenu.style.top = y + "px";
    ctxMenu.style.display = "block";
    // Adjust if off-screen
    const rect = ctxMenu.getBoundingClientRect();
    if (rect.right > window.innerWidth) ctxMenu.style.left = (x - rect.width) + "px";
    if (rect.bottom > window.innerHeight) ctxMenu.style.top = (y - rect.height) + "px";

    return new Promise(resolve => {
        function handler(e) {
            const item = e.target.closest("[data-ctx]");
            ctxMenu.style.display = "none";
            document.removeEventListener("click", handler, true);
            document.removeEventListener("contextmenu", dismiss);
            resolve(item ? item.dataset.ctx : null);
        }
        function dismiss() {
            ctxMenu.style.display = "none";
            document.removeEventListener("click", handler, true);
            document.removeEventListener("contextmenu", dismiss);
            resolve(null);
        }
        setTimeout(() => {
            document.addEventListener("click", handler, true);
            document.addEventListener("contextmenu", dismiss, { once: true });
        }, 0);
    });
}

// --- Helpers ---
function escHtml(s) {
    const d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
}
function escAttr(p) {
    return p.replace(/\\/g, "/").replace(/"/g, "&quot;");
}
function formatSize(bytes) {
    if (bytes == null) return "";
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1048576) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / 1048576).toFixed(1) + " MB";
}
function formatDate(iso) {
    if (!iso) return "";
    const d = new Date(iso);
    return d.toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" });
}
function formatRelative(iso) {
    if (!iso) return "";
    const diff = Date.now() - new Date(iso).getTime();
    const mins = Math.floor(diff / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + "m ago";
    const hrs = Math.floor(mins / 60);
    if (hrs < 24) return hrs + "h ago";
    const days = Math.floor(hrs / 24);
    if (days < 7) return days + "d ago";
    return new Date(iso).toLocaleDateString();
}
function normPath(p) { return (p || "").replace(/\\/g, "/"); }

// Build the standard "Open in" actions HTML for a file row
function makeActionButtons(isOnline) {
    return '<span class="col-actions">' +
        '<span class="open-label">Open in</span>' +
        '<button class="btn-action primary" data-action="word">Word</button>' +
        '<button class="btn-action" data-action="html">HTML</button>' +
        '<button class="btn-action stub" data-action="interactive" title="Coming soon">Interactive</button>' +
        '</span>';
}

// Execute the default double-click action for a file
function execDefaultAction(fileInfo) {
    const action = getSetting("defaultAction", "word");
    if (action === "html") viewHtml(fileInfo.path);
    else if (action === "interactive") alert("Interactive viewer not yet implemented.");
    else openFileAndTrack(fileInfo.path, fileInfo.label, fileInfo.isOnline, fileInfo.url);
}

// --- Init ---
document.addEventListener("DOMContentLoaded", () => {
    loadHome();
    initLocalFiles();
    loadOnlineFiles();
});
