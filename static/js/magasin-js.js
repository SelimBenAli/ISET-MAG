var liste_magasin_tous = []
var liste_magasin = []
var division_table = 7

function load_page_magasin() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/magasin/get-magasins', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_magasin = response.magasins
                liste_magasin_tous = response.magasins
                load_table_magasin_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_magasin() {
    search = document.getElementById("nom_magasin").value
    if (search === "") {
        liste_magasin = liste_magasin_tous
    } else {
        liste_magasin = liste_magasin_tous.filter(magasin => magasin.nom_magasin.toLowerCase().includes(search.toLowerCase()))
    }
    load_table_magasin_parameters()
}

function search_magasin_by_bloc() {
    search = document.getElementById("magasin-bloc").value
    if (search === "get-all") {
        liste_magasin = liste_magasin_tous
    } else {
        liste_magasin = liste_magasin_tous.filter(magasin => magasin.salle_magasin.bloc_salle.id_bloc === parseInt(search))
    }
    load_table_magasin_parameters()
}

function load_table_magasin_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Salle</th><th>Bloc</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Salle</th><th>Bloc</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_magasin.forEach(magasin => {
        body.push("<tr><td>" + magasin.id_magasin + "</td><td>" + magasin.nom_magasin + "</td><td>" + magasin.salle_magasin.nom_salle + "</td><td>" + magasin.salle_magasin.bloc_salle.nom_bloc + "</td><td><button class='btn btn-outline-secondary' onclick='openPageMagasinUpdate(" + magasin.id_magasin + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_magasin(" + magasin.id_magasin + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_magasin(header, footer, body, division_table)
}


function load_table_magasin(header, footer, body, division_table) {
    get_data_ready_load_table("table-magasin", header, footer, body, division_table)
    get_data_ready_pagination("pagination-magasin", liste_magasin.length, division_table, "dataTable_info_magasin", "magasins")
}

function ajout_magasin() {
    nom = document.getElementById("nom-magasin").value
    salle = document.getElementById("salle-magasin").value
    if (nom === "" || salle === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_magasin_request(nom, salle)
}

function ajout_magasin_request(nom, salle) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/magasin/add-magasin', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                openPageMagasin()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_magasin: nom,
        id_salle: salle
    }));
}

function modifier_magasin(id) {
    nom = document.getElementById("nom-magasin").value
    salle = document.getElementById("salle-magasin").value
    if (nom === "" || salle === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_magasin_request(id, nom, salle)
}

function modifier_magasin_request(id, nom, salle) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/magasin/update-magasin/' + id, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                openPageMagasin()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_magasin: id,
        nom_magasin: nom,
        id_salle: salle
    }));
}

function supprimer_magasin(id) {
    confirmation = confirm("Voulez-vous vraiment supprimer ce magasin?")
    if (confirmation) {
        supprimer_magasin_request(id)
    }
}

function supprimer_magasin_request(id) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/magasin/delete-magasin/' + id, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                openPageMagasin()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}