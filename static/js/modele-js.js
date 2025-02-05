var liste_modele_tous = []
var liste_modele = []
var division_table = 7

function load_page_modele() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/modele/get-modeles', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_modele = response.modeles
                liste_modele_tous = response.modeles
                load_table_modele_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function search_modele() {
    search = document.getElementById("nom_modele").value
    if (search === "") {
        liste_modele = liste_modele_tous
    } else {
        liste_modele = liste_modele_tous.filter(modele => modele.nom_modele.toLowerCase().includes(search.toLowerCase()))
    }
    load_table_modele_parameters()
}

function search_modele_by_marque() {
    search = document.getElementById("marque-modele").value
    console.log(search)
    if (search === "get-all") {
        liste_modele = liste_modele_tous
    } else {
        liste_modele = liste_modele_tous.filter(modele => modele.marque_modele.id_marque === parseInt(search))
    }
    load_table_modele_parameters()
}

function load_table_modele_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Marque</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Marque</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_modele.forEach(modele => {
        body.push("<tr><td>" + modele.id_modele + "</td><td>" + modele.nom_modele + "</td><td>" + modele.marque_modele.nom_marque + "</td><td><button class='btn btn-outline-secondary' onclick='openPageModeleUpdate(" + modele.id_modele + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_modele(" + modele.id_modele + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_modele(header, footer, body, division_table)
}


function load_table_modele(header, footer, body, division_table) {
    get_data_ready_load_table("table-modele", header, footer, body, division_table)
    get_data_ready_pagination("pagination-modele", liste_modele.length, division_table, "dataTable_info_modele", "modèles")
}

function ajout_modele() {
    nom = document.getElementById("nom-modele").value
    marque = document.getElementById("marque-modele").value
    if (nom === "" || marque === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_modele_request(nom, marque)
}

function ajout_modele_request(nom, marque) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/modele/add-modele', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                openPageModele()
            } else {
                alert('Erreur !');
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_modele: nom,
        id_marque: marque
    }));
}

function modifier_modele(id_modele) {
    nom = document.getElementById("nom-modele").value
    marque = document.getElementById("marque-modele").value
    if (nom === "" || marque === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_modele_request(id_modele, nom, marque)
}

function modifier_modele_request(id_modele, nom, marque) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/modele/update-modele', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                openPageModele()
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_modele: id_modele,
        nom_modele: nom,
        id_marque: marque
    }));
}

function supprimer_modele(id_modele) {
    confirmation = confirm("Voulez-vous vraiment supprimer ce modèle?")
    if (confirmation) {
        supprimer_modele_request(id_modele)
    }
}

function supprimer_modele_request(id_modele) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/modele/delete-modele/' + id_modele, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                openPageModele()
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send();
}
