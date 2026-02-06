document.getElementById("searchBox").addEventListener("input", function () {
    const keyword = this.value.toLowerCase();

    document.querySelectorAll("tbody tr, table tr").forEach(row => {
        const link = row.querySelector("td a");
        if (!link) return;

        const text = link.textContent.toLowerCase();
        row.style.display = text.includes(keyword) ? "" : "none";
    });
});