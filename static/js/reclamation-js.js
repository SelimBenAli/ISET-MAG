var liste_reclamation_tous = []
var liste_reclamation = []
var division_table = 7

function load_page_fournisseur() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/reclamation/get-reclamations', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_reclamation = response.reclamations
                liste_reclamation_tous = response.reclamations
                load_table_reclamation_parameters()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function load_table_reclamation_parameters() {
    header = "<thead><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Numéro Inventaire</th><th>Date</th><th>Description</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Numéro Inventaire</th><th>Date</th><th>Description</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_reclamation.forEach(reclamation => {
        body.push("<tr><td>" + reclamation.id_reclamation + "</td><td>" + fournisseur.nom_fournisseur + "</td><td>" + fournisseur.telephone_fournisseur + "</td><td><button class='btn btn-outline-secondary' onclick='openPageFournisseurUpdate(" + fournisseur.id_fournisseur + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_fournisseur(" + fournisseur.id_fournisseur + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_fournisseur(header, footer, body, division_table)
}


function load_table_fournisseur(header, footer, body, division_table) {
    get_data_ready_load_table("table-reclamation", header, footer, body, division_table)
    get_data_ready_pagination("pagination-reclamation", liste_reclamation.length, division_table, "dataTable_info_reclamation", "reclamations")
}
