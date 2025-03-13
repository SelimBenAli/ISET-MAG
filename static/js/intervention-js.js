var liste_intervention_tous = []
var liste_intervention = []
var division_table = 7

function load_page_intervention() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function load_table_intervention_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Hardware</th><th>Admin</th><th>Fermer</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Hardware</th><th>Admin</th><th>Fermer</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_intervention.forEach(intervention => {
        add_fermeture = "<button class='btn btn-outline-success' disabled>Fermer</button>"
        if (intervention.date_fin_intervention === null) {
            add_fermeture = "<button class='btn btn-outline-success' onclick='fermer_intervention(" + intervention.id_intervention + ")'>Fermer</button>"
        }
        body.push("<tr><td>" + intervention.id_intervention + "</td><td>" + intervention.utilisateur_intervention.nom_utilisateur + "</td><td>" + intervention.utilisateur_intervention.prenom_utilisateur + "</td><td>" + intervention.date_debut_intervention + "</td><td>" + intervention.date_fin_intervention + "</td><td>" + intervention.hardware_intervention.numero_inventaire_hardware + "</td><td>" + intervention.admin_intervention.nom_admin + " " + intervention.admin_intervention.prenom_admin + "</td><td>" + add_fermeture + "</td><td><button class='btn btn-outline-secondary' onclick=''>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_intervention(" + intervention.id_intervention + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_intervention(header, footer, body, division_table)
}


function load_table_intervention(header, footer, body, division_table) {
    get_data_ready_load_table("table-intervention", header, footer, body, division_table)
    get_data_ready_pagination("pagination-intervention", liste_intervention.length, division_table, "dataTable_info_intervention", "interventions")
}

function search_intervention() {
    let status = document.getElementById('status-int').value
    if (status === 'ALL') {
        liste_intervention = liste_intervention_tous
    } else if (status === 'CURRENT') {
        liste_intervention = liste_intervention_tous.filter(intervention => intervention.date_fin_intervention === null)
    }
    else {
        liste_intervention = liste_intervention_tous.filter(intervention => intervention.date_fin_intervention !== null)
    }
    let code_hard = document.getElementById('code-hardware-search').value
    let code_user = document.getElementById('code-user-search').value
    let num_hard = document.getElementById('num-hardware-search').value
    if (code_hard !== '') {
        liste_intervention = liste_intervention.filter(intervention => intervention.hardware_intervention.code_hardware === code_hard)
    }
    if (code_user !== '') {
        liste_intervention = liste_intervention.filter(intervention => intervention.utilisateur_intervention.code_a_barre_utilisateur === code_user)
    }
    if (num_hard !== '') {
        liste_intervention = liste_intervention.filter(intervention => intervention.hardware_intervention.numero_inventaire_hardware.includes(num_hard))
    }
    load_table_intervention_parameters()
}

function fermer_intervention(id_intervention) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/intervention/close-intervention/' + id_intervention, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                quit_loading_mode()
                load_page_intervention()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}