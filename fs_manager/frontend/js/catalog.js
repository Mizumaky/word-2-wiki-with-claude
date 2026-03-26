/**
 * FS Manager - Home (favorites + recent), online files
 */

let starCache = [];

// ==================== Favorites ====================

async function loadHome() {
    await loadStarredFiles();
    await loadRecentFiles();
}

async function loadStarredFiles() {
    try { starCache = await API.get("/api/catalog/pinned"); }
    catch { starCache = []; }
    renderStarredFiles(starCache);
}

function renderStarredFiles(items) {
    const container = document.getElementById("fav-files-container");
    if (items.length === 0) {
        container.innerHTML = '<div class="empty-state">No favorites yet. Browse files and star them to add here.</div>';
        return;
    }

    const wrapper = document.createElement("div");

    for (const item of items) {
        const row = document.createElement("div");
        row.className = "file-row";

        row.innerHTML =
            '<span class="col-icon"><span class="icon-word">W</span></span>' +
            '<span class="col-name">' + escHtml(item.label) + '</span>' +
            '<span class="col-actions">' +
                '<span class="open-label">Open in</span>' +
                '<button class="btn-action primary" data-action="word">Word</button>' +
                '<button class="btn-action" data-action="html">HTML</button>' +
                '<button class="btn-action stub" data-action="interactive" title="Coming soon">Interactive</button>' +
                '<button class="btn-star is-starred" data-action="unstar" title="Remove from favorites">\u2605</button>' +
            '</span>';

        const fileInfo = { path: item.path, label: item.label, isOnline: false };

        row.addEventListener("dblclick", () => execDefaultAction(fileInfo));
        row.addEventListener("click", (e) => {
            const btn = e.target.closest("[data-action]");
            if (!btn) return;
            e.stopPropagation();
            if (btn.dataset.action === "word") openFileAndTrack(item.path, item.label);
            else if (btn.dataset.action === "html") viewHtml(item.path);
            else if (btn.dataset.action === "interactive") alert("Interactive viewer not yet implemented.");
            else if (btn.dataset.action === "unstar") unstarById(item.id);
        });

        row.addEventListener("contextmenu", async (e) => {
            e.preventDefault();
            const items2 = [
                { label: "Open in Word", action: "word" },
                { label: "Open as HTML", action: "html" },
                { label: "Open Interactive", action: "interactive" },
                { separator: true },
                { label: "Show in Explorer", action: "explorer" },
                { label: "\u2605 Remove from favorites", action: "unstar" },
            ];
            const action = await showContextMenu(e.clientX, e.clientY, items2);
            if (action === "word") openFileAndTrack(item.path, item.label);
            else if (action === "html") viewHtml(item.path);
            else if (action === "interactive") alert("Interactive viewer not yet implemented.");
            else if (action === "explorer") showInExplorer(item.path);
            else if (action === "unstar") unstarById(item.id);
        });

        wrapper.appendChild(row);
    }

    container.innerHTML = "";
    container.appendChild(wrapper);
}

function isStarred(path) {
    return starCache.some(p => normPath(p.path) === normPath(path));
}

async function toggleStar(path, name) {
    const existing = starCache.find(p => normPath(p.path) === normPath(path));
    try {
        if (existing) await API.del("/api/catalog/pinned/" + existing.id);
        else await API.post("/api/catalog/pinned", { label: name, path: path });
        await loadStarredFiles();
        // Refresh the current file view to update star icons
        if (activePinnedFolder) navigateToPinnedTree(activePinnedFolder);
        else if (currentPath) navigateTo(currentPath, false);
    } catch (err) { alert("Error: " + err.message); }
}

async function unstarById(id) {
    try {
        await API.del("/api/catalog/pinned/" + id);
        await loadStarredFiles();
    } catch (err) { alert("Error: " + err.message); }
}

// ==================== Recent ====================

async function loadRecentFiles() {
    try {
        const recent = await API.get("/api/catalog/recent");
        renderRecentFiles(recent);
    } catch { /* ignore */ }
}

function renderRecentFiles(recent) {
    const container = document.getElementById("recent-files-container");
    if (recent.length === 0) {
        container.innerHTML = '<div class="empty-state">No recent files.</div>';
        return;
    }

    const wrapper = document.createElement("div");

    for (const file of recent) {
        const row = document.createElement("div");
        row.className = "file-row";
        const isOnline = file.source_type === "onedrive";

        row.innerHTML =
            '<span class="col-icon"><span class="icon-word' + (isOnline ? ' online' : '') + '">W</span></span>' +
            '<span class="col-name">' + escHtml(file.label) + '</span>' +
            '<span class="col-time">' + formatRelative(file.opened_at) + '</span>' +
            '<span class="col-actions">' +
                '<span class="open-label">Open in</span>' +
                '<button class="btn-action primary" data-action="word">Word</button>' +
                '<button class="btn-action" data-action="html">HTML</button>' +
                '<button class="btn-action stub" data-action="interactive" title="Coming soon">Interactive</button>' +
            '</span>';

        const fileInfo = { path: file.path, label: file.label, isOnline, url: file.url };

        row.addEventListener("dblclick", () => execDefaultAction(fileInfo));
        row.addEventListener("click", (e) => {
            const btn = e.target.closest("[data-action]");
            if (!btn) return;
            e.stopPropagation();
            if (btn.dataset.action === "word") openFileAndTrack(file.path, file.label, isOnline, file.url);
            else if (btn.dataset.action === "html") viewHtml(file.path);
            else if (btn.dataset.action === "interactive") alert("Interactive viewer not yet implemented.");
        });

        row.addEventListener("contextmenu", async (e) => {
            e.preventDefault();
            const ctxItems = [
                { label: "Open in Word", action: "word" },
                { label: "Open as HTML", action: "html" },
                { label: "Open Interactive", action: "interactive" },
                { separator: true },
            ];
            if (isOnline) ctxItems.push({ label: "Copy link", action: "copy" });
            else ctxItems.push({ label: "Show in Explorer", action: "explorer" });
            const action = await showContextMenu(e.clientX, e.clientY, ctxItems);
            if (action === "word") openFileAndTrack(file.path, file.label, isOnline, file.url);
            else if (action === "html") viewHtml(file.path);
            else if (action === "interactive") alert("Interactive viewer not yet implemented.");
            else if (action === "explorer") showInExplorer(file.path);
            else if (action === "copy") { navigator.clipboard.writeText(file.url || file.path); }
        });

        wrapper.appendChild(row);
    }

    container.innerHTML = "";
    container.appendChild(wrapper);
}

// ==================== Online Files ====================

document.getElementById("btn-add-online").addEventListener("click", () => {
    document.getElementById("add-online-dialog").showModal();
});

document.getElementById("btn-save-online").addEventListener("click", async () => {
    const label = document.getElementById("online-label").value.trim();
    const url = document.getElementById("online-url").value.trim();
    const folder = document.getElementById("online-folder").value.trim();
    if (!label || !url) return;
    try {
        await API.post("/api/catalog/online", { label, url, folder: folder || "" });
        document.getElementById("add-online-dialog").close();
        document.getElementById("add-online-form").reset();
        loadOnlineFiles();
    } catch (err) { alert("Error: " + err.message); }
});

async function loadOnlineFiles() {
    try {
        const files = await API.get("/api/catalog/online");
        const container = document.getElementById("online-files-container");

        if (files.length === 0) {
            container.innerHTML = '<div class="empty-state">No online files added. Click "+ Add Link" to add a OneDrive shared link.</div>';
            return;
        }

        // Group by folder
        const groups = {};
        for (const file of files) {
            const folder = file.folder || "";
            if (!groups[folder]) groups[folder] = [];
            groups[folder].push(file);
        }

        const sortedGroups = Object.entries(groups).sort((a, b) => {
            if (a[0] === "") return 1;
            if (b[0] === "") return -1;
            return a[0].localeCompare(b[0]);
        });

        container.innerHTML = "";

        for (const [folder, items] of sortedGroups) {
            const section = document.createElement("div");
            section.className = "online-section";

            if (folder) {
                section.innerHTML = '<div class="online-section-header">' + escHtml(folder) + '</div>';
            }

            const list = document.createElement("div");

            for (const item of items) {
                const row = document.createElement("div");
                row.className = "file-row";

                const starred = isStarred(item.url);

                row.innerHTML =
                    '<span class="col-icon"><span class="icon-word online">W</span></span>' +
                    '<span class="col-name">' + escHtml(item.label) + '</span>' +
                    '<span class="col-actions">' +
                        '<span class="open-label">Open in</span>' +
                        '<button class="btn-action primary" data-action="word">Word</button>' +
                        '<button class="btn-action" data-action="html">HTML</button>' +
                        '<button class="btn-action stub" data-action="interactive" title="Coming soon">Interactive</button>' +
                        '<button class="btn-star' + (starred ? ' is-starred' : '') + '" data-action="star" title="' + (starred ? 'Remove from favorites' : 'Add to favorites') + '">' + (starred ? '\u2605' : '\u2606') + '</button>' +
                    '</span>';

                const fileInfo = { path: item.url, label: item.label, isOnline: true, url: item.url };

                row.addEventListener("dblclick", () => execDefaultAction(fileInfo));
                row.addEventListener("click", (e) => {
                    const btn = e.target.closest("[data-action]");
                    if (!btn) return;
                    e.stopPropagation();
                    if (btn.dataset.action === "word") openFileAndTrack(item.url, item.label, true, item.url);
                    else if (btn.dataset.action === "html") viewHtml(item.url);
                    else if (btn.dataset.action === "interactive") alert("Interactive viewer not yet implemented.");
                    else if (btn.dataset.action === "star") toggleStar(item.url, item.label);
                });

                row.addEventListener("contextmenu", async (e) => {
                    e.preventDefault();
                    const ctxItems = [
                        { label: "Open in Word", action: "word" },
                        { label: "Open as HTML", action: "html" },
                        { label: "Open Interactive", action: "interactive" },
                        { separator: true },
                        { label: "Copy link", action: "copy" },
                        { label: starred ? "\u2605 Remove from favorites" : "\u2606 Add to favorites", action: "star" },
                        { separator: true },
                        { label: "Remove link", action: "remove", danger: true },
                    ];
                    const action = await showContextMenu(e.clientX, e.clientY, ctxItems);
                    if (action === "word") openFileAndTrack(item.url, item.label, true, item.url);
                    else if (action === "html") viewHtml(item.url);
                    else if (action === "interactive") alert("Interactive viewer not yet implemented.");
                    else if (action === "copy") { navigator.clipboard.writeText(item.url); }
                    else if (action === "star") toggleStar(item.url, item.label);
                    else if (action === "remove") {
                        if (confirm("Remove this online link?")) removeOnlineFile(item.id);
                    }
                });

                list.appendChild(row);
            }

            section.appendChild(list);
            container.appendChild(section);
        }
    } catch { /* ignore */ }
}

async function removeOnlineFile(id) {
    try {
        await API.del("/api/catalog/online/" + id);
        loadOnlineFiles();
    } catch (err) { alert("Error: " + err.message); }
}
