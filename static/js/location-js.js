var liste_location_tous = []
var liste_location = []
var division_table = 7

function load_page_location() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/location/get-locations', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_location_tous = response.locations
                liste_location = response.locations
                load_table_location_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}


function search_location_by_user() {
    search = document.getElementById("utilisateur-location").value
    console.log(search)
    if (search === "") {
        liste_location = liste_location_tous
    } else {
        liste_location = liste_location_tous.filter(location => (location.utilisateur_location.nom_utilisateur.toLowerCase().includes(search.toLowerCase()) || location.utilisateur_location.prenom_utilisateur.toLowerCase().includes(search.toLowerCase())))
    }
    load_table_location_parameters()
}

function search_location_by_date_debut() {
    search = document.getElementById("date-debut-location").value
    console.log(search)
    if (search === "") {
        liste_location = liste_location_tous
    } else {
        liste_location = liste_location_tous.filter(location => location.date_debut_estimee_location.includes(search))
    }
    load_table_location_parameters()
}

function search_location_by_date_fin() {
    search = document.getElementById("date-fin-location").value
    console.log(search)
    if (search === "") {
        liste_location = liste_location_tous
    } else {
        liste_location = liste_location_tous.filter(location => location.date_fin_estimee_location.includes(search))
    }
    load_table_location_parameters()
}

function changer_etat() {
    etat = document.getElementById("etat-location").value
    console.log(etat)
    if (etat === "get-all") {
        liste_location = liste_location_tous
    } else {
        liste_location = liste_location_tous.filter(location => location.confirmation_location.toString() === etat.toString())
    }
    load_table_location_parameters()
}

function load_table_location_parameters() {
    console.log(liste_location)
    header = "<thead><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Quantité</th><th>Date Début Estimée</th><th>Date Fin Estimée</th><th>Confirmer</th><th>Refuser</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Quantité</th><th>Date Début Estimée</th><th>Date Fin Estimée</th><th>Confirmer</th><th>Refuser</th></tr></tfoot>"
    body = []
    liste_location.forEach(location => {
            add = "<td><button class='btn btn-outline-secondary' onclick='confirmer_demande( " + location.id_location + ")'>Confirmer</button></td><td><button class='btn btn-outline-danger' onclick='refuser_demande(" + location.id_location + ")'>Refuser</button></td>"

        if (location.confirmation_location === 1) {
            add = "<td><button class='btn btn-secondary' disabled>Confirmer</button></td><td><button class='btn btn-outline-danger' disabled >Refuser</button></td>"
        }
        else if (location.confirmation_location === -1) {
            add = "<td><button class='btn btn-outline-secondary' disabled>Confirmer</button></td><td><button class='btn btn-danger' disabled >Refuser</button></td>"
        }
        body.push("<tr><td>" + location.id_location + "</td><td>" + location.utilisateur_location.nom_utilisateur + " " + location.utilisateur_location.prenom_utilisateur + "</td><td>" + location.modele_location.nom_modele + " " + location.modele_location.marque_modele.nom_marque + "</td><td>" + location.quantite_location + "</td><td>" + location.date_debut_estimee_location + "</td><td>" + location.date_fin_estimee_location + "</td>" + add + "</tr>")
    });
    division_table = 7
    load_table_location(header, footer, body, division_table)
}


function load_table_location(header, footer, body, division_table) {
    get_data_ready_load_table("table-location", header, footer, body, division_table)
    get_data_ready_pagination("pagination-location", liste_location.length, division_table, "dataTable_info_location", "locations")
}

function confirmer_demande(id_location) {
    conf = confirm("Voulez-vous vraiment accepter cette demande de location?")
    if (conf)
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/location/confirmer-location/' + id_location, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                console.log(response)
                if (response.status === 'success') {
                    load_page_location()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function refuser_demande(id_location) {
    conf = confirm("Voulez-vous vraiment refuser cette demande de location?")
    if (conf)
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/location/refuser-location/' + id_location, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                console.log(response)
                if (response.status === 'success') {
                    load_page_location()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}