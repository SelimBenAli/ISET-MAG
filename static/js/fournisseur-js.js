var liste_fournisseur_tous = []
var liste_fournisseur = []
var division_table = 7

function load_page_fournisseur() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/fournisseur/get-fournisseurs', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                liste_fournisseur = response.fournisseurs
                liste_fournisseur_tous = response.fournisseurs
                load_table_fournisseur_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_fournisseur() {
    search = document.getElementById("nom").value
    if (search === "") {
        liste_fournisseur = liste_fournisseur_tous
    } else {
        liste_fournisseur = liste_fournisseur_tous.filter(fournisseur => fournisseur.nom_fournisseur.toLowerCase().includes(search.toLowerCase()))
    }
    load_table_fournisseur_parameters()
}

function load_table_fournisseur_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Telephone</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Telephone</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_fournisseur.forEach(fournisseur => {
        body.push("<tr><td>" + fournisseur.id_fournisseur + "</td><td>" + fournisseur.nom_fournisseur + "</td><td>" + fournisseur.telephone_fournisseur + "</td><td><button class='btn btn-outline-secondary' onclick='openPageFournisseurUpdate(" + fournisseur.id_fournisseur + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_fournisseur(" + fournisseur.id_fournisseur + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_fournisseur(header, footer, body, division_table)
}


function load_table_fournisseur(header, footer, body, division_table) {
    get_data_ready_load_table("table-fournisseur", header, footer, body, division_table)
    get_data_ready_pagination("pagination-fournisseur", liste_fournisseur.length, division_table, "dataTable_info_fournisseur", "fournisseurs")
}

function ajout_fournisseur() {
    nom = document.getElementById("nom-fournisseur").value
    telephone = document.getElementById("tel-fournisseur").value
    if (nom === "" || telephone === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_fournisseur_request(nom, telephone)
}

function ajout_fournisseur_request(nom, telephone) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/fournisseur/add-fournisseur', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert('Erreur lors de l\'ajout du fournisseur');
            }
        }
    };
    xhr.send(JSON.stringify({nom: nom, telephone: telephone}));
}

function modifier_fournisseur(id_fournisseur) {
    nom = document.getElementById("nom-fournisseur").value
    telephone = document.getElementById("tel-fournisseur").value
    if (nom === "" || telephone === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_fournisseur_request(id_fournisseur, nom, telephone)
}

function modifier_fournisseur_request(id_fournisseur, nom, telephone) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/fournisseur/update-fournisseur', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert('Erreur lors de la modification du fournisseur');
            }
        }
    };
    xhr.send(JSON.stringify({id_fournisseur: id_fournisseur, nom_fournisseur: nom, telephone_fournisseur: telephone}));
}

function supprimer_fournisseur(id_fournisseur) {
    confirmation = confirm("Voulez-vous vraiment supprimer ce fournisseur?")
    if (confirmation) {
        supprimer_fournisseur_request(id_fournisseur)
    }
}

function supprimer_fournisseur_request(id_fournisseur) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/fournisseur/delete-fournisseur', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert('Erreur lors de la suppression du fournisseur');
            }
        }
    };
    xhr.send(JSON.stringify({id_fournisseur: id_fournisseur}));
}