document.getElementById("scrape-btn").addEventListener("click", async () => {
    const url = document.getElementById("scrape-url").value;
    const command = prompt("Entrez une commande (ex: supprimer image ou supprimer mot:bonjour)");

    const loader = document.getElementById("loader");
    const output = document.getElementById("scrape-output");
    loader.style.display = "block";
    output.innerHTML = "";

    try {
        const res = await fetch("/scrape", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url, command })
        });
        const data = await res.json();
        loader.style.display = "none";
        output.innerHTML = data.cleaned_html || "Aucun résultat";
    } catch (err) {
        loader.style.display = "none";
        output.innerHTML = "Erreur: " + err.message;
    }
});
