/**
 * FS Manager - File browser: sidebar, address bar, navigation, file listing
 */

let currentPath = null;
let lastBrowsePath = null;
let navHistory = [];
let navHistoryIndex = -1;
let activePinnedFolder = null;
let localSources = [];
let downloadsPath = null;

// ==================== Address bar ====================

const addressBar = document.getElementById("address-bar");
const bcDisplay = document.getElementById("breadcrumb-display");
const pathEdit = document.getElementById("path-edit");
const navBack = document.getElementById("nav-back");
const navUp = document.getElementById("nav-up");
const navGo = document.getElementById("nav-go");

document.getElementById("breadcrumb-area").addEventListener("click", (e) => {
    if (e.target.closest(".bc-segment")) return;
    addressBar.classList.add("editing");
    pathEdit.value = currentPath || "";
    pathEdit.focus();
    pathEdit.select();
});

pathEdit.addEventListener("blur", () => {
    setTimeout(() => addressBar.classList.remove("editing"), 150);
});

pathEdit.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        e.preventDefault();
        const val = pathEdit.value.trim();
        if (val) navigateTo(val, true);
        addressBar.classList.remove("editing");
    } else if (e.key === "Escape") {
        addressBar.classList.remove("editing");
    }
});

navGo.addEventListener("click", () => {
    if (addressBar.classList.contains("editing")) {
        const val = pathEdit.value.trim();
        if (val) navigateTo(val, true);
        addressBar.classList.remove("editing");
    }
});

navBack.addEventListener("click", () => {
    if (navHistoryIndex > 0) {
        navHistoryIndex--;
        navigateTo(navHistory[navHistoryIndex], false);
    }
});

navUp.addEventListener("click", () => {
    if (!currentPath) return;
    const norm = normPath(currentPath).replace(/\/+$/, "");
    const parent = norm.replace(/\/[^/]+$/, "");
    if (!parent || parent === norm) return;
    const target = parent.match(/^[A-Za-z]:$/) ? parent + "/" : parent;
    navigateTo(target, true);
});

function updateNavButtons() {
    navBack.disabled = navHistoryIndex <= 0;
    navUp.disabled = !currentPath;
}

function renderBreadcrumb(fullPath) {
    const parts = normPath(fullPath).split("/").filter(Boolean);
    let accumulated = "";
    bcDisplay.innerHTML = "";

    parts.forEach((part, i) => {
        accumulated += (i === 0 ? "" : "/") + part;
        if (i > 0) {
            const sep = document.createElement("span");
            sep.className = "bc-sep";
            sep.textContent = "\u203A";
            bcDisplay.appendChild(sep);
        }
        const seg = document.createElement("span");
        seg.className = "bc-segment";
        seg.textContent = part;
        if (i < parts.length - 1) {
            const target = (i === 0 && part.endsWith(":")) ? accumulated + "/" : accumulated;
            seg.addEventListener("click", (e) => { e.stopPropagation(); navigateTo(target, true); });
        }
        bcDisplay.appendChild(seg);
    });
}

// ==================== Navigation ====================

async function navigateTo(path, addToHistory) {
    if (!path) return;
    path = path.replace(/\\/g, "/");
    currentPath = path;
    lastBrowsePath = path;
    activePinnedFolder = null;
    renderSidebar();

    if (addToHistory !== false) {
        navHistory = navHistory.slice(0, navHistoryIndex + 1);
        navHistory.push(path);
        navHistoryIndex = navHistory.length - 1;
    }

    updateNavButtons();
    renderBreadcrumb(path);
    addressBar.classList.remove("editing");

    const body = document.getElementById("file-list-body");
    body.innerHTML = '<div class="empty-state">Loading...</div>';

    try {
        const entries = await API.get("/api/sources/browse?path=" + encodeURIComponent(path));
        renderFileList(entries, body, path);
    } catch (err) {
        body.innerHTML = '<div class="empty-state">Error: ' + escHtml(err.message) + '</div>';
    }
}

async function navigateToPinnedTree(path) {
    currentPath = path;
    activePinnedFolder = normPath(path);
    renderSidebar();
    updateNavButtons();
    renderBreadcrumb(path);

    const body = document.getElementById("file-list-body");
    body.innerHTML = '<div class="empty-state">Loading...</div>';

    try {
        const entries = await API.get("/api/sources/browse-tree?path=" + encodeURIComponent(path));
        renderTreeList(entries, body, 0);
    } catch (err) {
        body.innerHTML = '<div class="empty-state">Error: ' + escHtml(err.message) + '</div>';
    }
}

// ==================== Flat file list ====================

function renderFileList(entries, container, browsePath) {
    container.innerHTML = "";

    if (entries.length === 0) {
        container.innerHTML = '<div class="empty-state">No .docx files or subfolders here.</div>';
        return;
    }

    const parent = normPath(browsePath).replace(/\/[^/]+\/?$/, "");
    if (parent && parent !== normPath(browsePath)) {
        container.appendChild(makeDirRow("..", parent));
    }

    for (const entry of entries) {
        if (entry.is_dir) {
            container.appendChild(makeDirRow(entry.name, entry.path));
        } else {
            container.appendChild(makeFileRow(entry, 0));
        }
    }
}

function makeDirRow(name, path, depth) {
    const row = document.createElement("div");
    row.className = "file-row is-dir" + (depth ? " indent-" + Math.min(depth, 4) : "");
    row.addEventListener("click", () => navigateTo(path, true));
    row.innerHTML =
        '<span class="col-icon"><span class="icon-folder">\uD83D\uDCC1</span></span>' +
        '<span class="col-name"><span class="dir-name">' + escHtml(name) + '</span></span>';
    return row;
}

// ==================== Tree list ====================

function renderTreeList(entries, container, depth) {
    if (!entries || entries.length === 0) {
        if (depth === 0) container.innerHTML = '<div class="empty-state">No .docx files found.</div>';
        return;
    }
    if (depth === 0) container.innerHTML = "";

    for (const entry of entries) {
        if (entry.is_dir) {
            container.appendChild(makeTreeDirRow(entry, depth));
            if (entry.children && entry.children.length > 0) {
                const childContainer = document.createElement("div");
                childContainer.className = "tree-children";
                renderTreeList(entry.children, childContainer, depth + 1);
                container.appendChild(childContainer);
            }
        } else {
            container.appendChild(makeFileRow(entry, depth));
        }
    }
}

function makeTreeDirRow(entry, depth) {
    const row = document.createElement("div");
    row.className = "file-row is-dir" + (depth ? " indent-" + Math.min(depth, 4) : "");
    const hasChildren = entry.children && entry.children.length > 0;
    row.innerHTML =
        '<span class="col-icon">' + (hasChildren ? '<span class="chevron open">\u25B6</span>' : '') + '</span>' +
        '<span class="col-name"><span class="dir-name">\uD83D\uDCC1 ' + escHtml(entry.name) + '</span></span>';
    if (hasChildren) {
        row.addEventListener("click", () => {
            const chevron = row.querySelector(".chevron");
            const children = row.nextElementSibling;
            if (children && children.classList.contains("tree-children")) {
                const hidden = children.style.display === "none";
                children.style.display = hidden ? "" : "none";
                chevron.classList.toggle("open", hidden);
            }
        });
    }
    return row;
}

// ==================== File row (local) ====================

function makeFileRow(entry, depth) {
    const row = document.createElement("div");
    row.className = "file-row" + (depth ? " indent-" + Math.min(depth, 4) : "");
    row.dataset.path = entry.path;

    const starred = isStarred(entry.path);
    const info = [formatSize(entry.size), formatDate(entry.modified)].filter(Boolean).join(" \u00B7 ");
    row.title = entry.name + (info ? "\n" + info : "");

    row.innerHTML =
        '<span class="col-icon"><span class="icon-word">W</span></span>' +
        '<span class="col-name">' + escHtml(entry.name) + '</span>' +
        '<span class="col-actions">' +
            '<span class="open-label">Open in</span>' +
            '<button class="btn-action primary" data-action="word">Word</button>' +
            '<button class="btn-action" data-action="html">HTML</button>' +
            '<button class="btn-action stub" data-action="interactive" title="Coming soon">Interactive</button>' +
            '<button class="btn-star' + (starred ? ' is-starred' : '') + '" data-action="star" title="' + (starred ? 'Remove from favorites' : 'Add to favorites') + '">' + (starred ? '\u2605' : '\u2606') + '</button>' +
        '</span>';

    const fileInfo = { path: entry.path, label: entry.name, isOnline: false };

    row.addEventListener("dblclick", () => execDefaultAction(fileInfo));
    row.addEventListener("click", (e) => {
        const btn = e.target.closest("[data-action]");
        if (btn) {
            e.stopPropagation();
            if (btn.dataset.action === "word") openFileAndTrack(entry.path, entry.name);
            else if (btn.dataset.action === "html") viewHtml(entry.path);
            else if (btn.dataset.action === "interactive") alert("Interactive viewer not yet implemented.");
            else if (btn.dataset.action === "star") toggleStar(entry.path, entry.name);
            return;
        }
        document.querySelectorAll(".file-row.selected").forEach(r => r.classList.remove("selected"));
        row.classList.add("selected");
    });

    row.addEventListener("contextmenu", async (e) => {
        e.preventDefault();
        const items = [
            { label: "Open in Word", action: "word" },
            { label: "Open as HTML", action: "html" },
            { label: "Open Interactive", action: "interactive" },
            { separator: true },
            { label: "Show in Explorer", action: "explorer" },
            { label: starred ? "\u2605 Remove from favorites" : "\u2606 Add to favorites", action: "star" },
        ];
        const action = await showContextMenu(e.clientX, e.clientY, items);
        if (action === "word") openFileAndTrack(entry.path, entry.name);
        else if (action === "html") viewHtml(entry.path);
        else if (action === "interactive") alert("Interactive viewer not yet implemented.");
        else if (action === "explorer") showInExplorer(entry.path);
        else if (action === "star") toggleStar(entry.path, entry.name);
    });

    return row;
}

// ==================== Sidebar ====================

async function initLocalFiles() {
    try { localSources = await API.get("/api/sources/local"); }
    catch { localSources = []; }
    try {
        const result = await API.get("/api/sources/downloads-path");
        downloadsPath = result.path;
    } catch { /* ignore */ }

    renderSidebar();

    // Pin folder dialog
    document.getElementById("btn-pin-folder").addEventListener("click", () => {
        if (currentPath) {
            const pathNorm = currentPath.replace(/\//g, "\\");
            document.getElementById("pin-path").value = pathNorm;
            const parts = currentPath.replace(/\\/g, "/").split("/").filter(Boolean);
            document.getElementById("pin-label").value = parts[parts.length - 1] || "";
        }
        document.getElementById("pin-folder-dialog").showModal();
    });

    document.getElementById("btn-save-pin").addEventListener("click", async () => {
        const label = document.getElementById("pin-label").value.trim();
        const path = document.getElementById("pin-path").value.trim();
        if (!label || !path) return;
        try {
            await API.post("/api/sources/local", { label, path });
            document.getElementById("pin-folder-dialog").close();
            document.getElementById("pin-folder-form").reset();
            localSources = await API.get("/api/sources/local");
            renderSidebar();
        } catch (err) { alert("Error: " + err.message); }
    });

    if (downloadsPath) navigateTo(downloadsPath, true);
}

function renderSidebar() {
    const container = document.getElementById("sidebar-locations");
    container.innerHTML = "";

    // Browse — always present
    if (downloadsPath) {
        const isActive = !activePinnedFolder && currentPath;
        const item = document.createElement("div");
        item.className = "sidebar-item" + (isActive ? " active" : "");
        item.innerHTML =
            '<span class="si-icon"><span class="icon-folder">\uD83D\uDCC2</span></span>' +
            '<span class="si-label">Browse</span>';
        item.addEventListener("click", () => {
            if (lastBrowsePath) navigateTo(lastBrowsePath, false);
            else navigateTo(downloadsPath, true);
        });
        container.appendChild(item);
    }

    for (const src of localSources) {
        const isActive = activePinnedFolder === normPath(src.path);
        const item = document.createElement("div");
        item.className = "sidebar-item" + (isActive ? " active" : "");
        item.innerHTML =
            '<span class="si-icon"><span class="icon-folder">\uD83D\uDCC1</span></span>' +
            '<span class="si-label">' + escHtml(src.label) + '</span>' +
            '<button class="si-remove" data-remove-id="' + src.id + '" title="Unpin">\u00D7</button>';

        item.addEventListener("click", (e) => {
            if (e.target.closest("[data-remove-id]")) return;
            if (activePinnedFolder === normPath(src.path)) {
                activePinnedFolder = null;
                renderSidebar();
                if (lastBrowsePath) navigateTo(lastBrowsePath, false);
                else if (downloadsPath) navigateTo(downloadsPath, true);
                return;
            }
            navigateToPinnedTree(src.path);
        });

        const removeBtn = item.querySelector("[data-remove-id]");
        if (removeBtn) {
            removeBtn.addEventListener("click", async (e) => {
                e.stopPropagation();
                if (!confirm("Unpin this folder?")) return;
                try {
                    await API.del("/api/sources/local/" + e.target.dataset.removeId);
                    activePinnedFolder = null;
                    localSources = await API.get("/api/sources/local");
                    renderSidebar();
                } catch (err) { alert("Error: " + err.message); }
            });
        }

        container.appendChild(item);
    }
}

// ==================== File actions ====================

async function openFileAndTrack(path, name, isOnline, url) {
    try {
        if (isOnline && url) {
            await API.post("/api/actions/open-url", { url });
            await API.post("/api/catalog/recent", { label: name, path: url, source_type: "onedrive", url });
        } else {
            await API.post("/api/actions/open-in-word", { path });
            await API.post("/api/catalog/recent", { label: name || path.split(/[\\/]/).pop(), path });
        }
        loadHome();
    } catch (err) { alert("Error opening file: " + err.message); }
}

async function viewHtml(path) {
    try {
        const result = await API.post("/api/actions/view-html", { path });
        alert(result.message);
    } catch (err) { alert("Error: " + err.message); }
}

async function showInExplorer(path) {
    try {
        await API.post("/api/actions/show-in-explorer", { path });
    } catch (err) { alert("Error: " + err.message); }
}
