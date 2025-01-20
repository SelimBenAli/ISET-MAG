var liste_intervention_tous = []
var liste_intervention = []
var division_table = 7

function load_page_intervention() {
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
            } else {
                alert('Error');
            }
        }
    };
    xhr.send();
}

function load_table_intervention_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Salle</th><th>Hardware</th><th>Admin</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Salle</th><th>Hardware</th><th>Admin</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_intervention.forEach(intervention => {
        body.push("<tr><td>" + intervention.id_intervention + "</td><td>" + intervention.utilisateur_intervention.nom_utilisateur + "</td><td>" + intervention.utilisateur_intervention.prenom_utilisateur + "</td><td>" + intervention.date_debut_intervention + "</td><td>" + intervention.date_fin_intervention + "</td><td>" + intervention.salle_intervention.nom_salle + "</td><td>" + intervention.hardware_intervention.numero_inventaire_hardware + "</td><td>" + intervention.admin_intervention.nom_admin + " " + intervention.admin_intervention.prenom_admin + "</td><td><button class='btn btn-outline-secondary' onclick=''>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_intervention(" + intervention.id_intervention + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_intervention(header, footer, body, division_table)
}


function load_table_intervention(header, footer, body, division_table) {
    get_data_ready_load_table("table-intervention", header, footer, body, division_table)
    get_data_ready_pagination("pagination-intervention", liste_intervention.length, division_table, "dataTable_info_intervention", "interventions")
}