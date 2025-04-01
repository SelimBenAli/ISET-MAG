var liste_marque_tous = []
var liste_marque = []
var division_table = 7

function load_page_marque() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/marque/get-marques', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_marque = response.marques
                liste_marque_tous = response.marques
                load_table_marque_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_marque() {
    search = document.getElementById("nom_marque").value
    if (search === "") {
        liste_marque = liste_marque_tous
    } else {
        liste_marque = liste_marque_tous.filter(marque => marque.nom_marque.toLowerCase().includes(search.toLowerCase()))
    }
    load_table_marque_parameters()
}

function load_table_marque_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_marque.forEach(marque => {
        body.push("<tr><td>" + marque.id_marque + "</td><td>" + marque.nom_marque + "</td><td><button class='btn btn-outline-secondary' onclick='openPageMarqueUpdate(" + marque.id_marque + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_marque(" + marque.id_marque + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_marque(header, footer, body, division_table)
}


function load_table_marque(header, footer, body, division_table) {
    get_data_ready_load_table("table-marque", header, footer, body, division_table)
    get_data_ready_pagination("pagination-marque", liste_marque.length, division_table, "dataTable_info_marque", "marques")
}

function ajout_marque() {
    nom = document.getElementById("nom-marque").value
    if (nom === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_marque_request(nom)
}

function ajout_marque_request(nom) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/marque/add-marque', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard//marque"
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({nom_marque: nom}));
}

function modifier_marque(id_marque) {
    nom = document.getElementById("nom-marque").value
    if (nom === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_marque_request(id_marque, nom)
}

function modifier_marque_request(id_marque, nom) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/marque/update-marque', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard//marque"
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({id_marque: id_marque, nom_marque: nom}));
}

function supprimer_marque(id_marque) {
    confirmation = confirm("Voulez-vous vraiment supprimer cette marque?")
    if (confirmation) {
        supprimer_marque_request(id_marque)
    }
}

function supprimer_marque_request(id_marque) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/marque/delete-marque', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                window.location.href = "/dashboard//marque"
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({id_marque: id_marque}));
}