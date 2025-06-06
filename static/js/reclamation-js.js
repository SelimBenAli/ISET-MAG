var liste_reclamation_tous = []
var liste_reclamation = []
var division_table = 10

function load_page_reclamation(page, status, user_code, num_inv) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/reclamation/get-reclamations-limit/' + page + '/' + status + '/user_' + user_code + '/num_inv_' + num_inv, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_reclamation = response.reclamations
                liste_reclamation_tous = response.reclamations
                load_table_reclamation_parameters()
                load_backend_pagination(response.pages, page, response.nombre_totale, response.reclamations.length);
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_reclamation_by_user() {
    var search = document.getElementById("utilisateur-reclamation").value
    if (search === "") {
        liste_reclamation = liste_reclamation_tous
    }
    liste_reclamation = liste_reclamation_tous.filter(reclamation => reclamation.utilisateur_reclamation.nom_utilisateur.toLowerCase().includes(search.toLowerCase()) || reclamation.utilisateur_reclamation.prenom_utilisateur.toLowerCase().includes(search.toLowerCase()))
    load_table_reclamation_parameters()
}

function search_reclamation() {
    var etat = document.getElementById("etat_reclamation").value
    var user_code = document.getElementById("utilisateur-reclamation").value
    var num_inv = document.getElementById("num-inv-reclamation").value
    load_page_reclamation(1, etat, user_code, num_inv)
}

/*function search_reclamation_by_status() {
    var search = document.getElementById("etat_reclamation").value
    if (search === "0") {
        liste_reclamation = liste_reclamation_tous
    } else if (search === "1") {
        liste_reclamation = liste_reclamation_tous.filter(reclamation => {
            return reclamation.technicien_reclamation == null
        });
    } else {
        liste_reclamation = liste_reclamation_tous.filter(reclamation => {
            return reclamation.technicien_reclamation != null
        });
    }
    load_table_reclamation_parameters()
}*/


function search_reclamation_by_num_inventaire() {
    var search = document.getElementById("num-inv-reclamation").value
    if (search === "") {
        liste_reclamation = liste_reclamation_tous
    }
    liste_reclamation = liste_reclamation_tous.filter(reclamation => reclamation.hardware_reclamation.numero_inventaire_hardware.toLowerCase().includes(search.toLowerCase()))
    load_table_reclamation_parameters()
}

function load_table_reclamation_parameters() {
    header = "<thead><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Numéro Inventaire</th><th>Date</th><th>Voir Réclamation</th><th>Technicien</th><th>Voir Description</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Utilisateur</th><th>Modèle</th><th>Numéro Inventaire</th><th>Date</th><th>Voir Réclamation</th><th>Technicien</th><th>Voir Description</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_reclamation.forEach(reclamation => {
        add_technicien = "<td> Pas Encore </td><td><button class='btn btn-outline-info' disabled>Voir Description</button></td>";
        if (reclamation.technicien_reclamation != null && reclamation.technicien_reclamation !== 'null') {
            add_technicien = "<td> " + reclamation.technicien_reclamation.nom_utilisateur + " " + reclamation.technicien_reclamation.prenom_utilisateur + " </td><td><button class='btn btn-outline-info' onclick='consulter_description_technicien(" + reclamation.id_reclamation + ")' >Voir Description</button></td>"
        }
        body.push("<tr><td>" + reclamation.id_reclamation + "</td><td>" + reclamation.utilisateur_reclamation.nom_utilisateur + " " + reclamation.utilisateur_reclamation.prenom_utilisateur + "</td><td>" + reclamation.hardware_reclamation.modele_hardware.nom_modele + " " + reclamation.hardware_reclamation.modele_hardware.marque_modele.nom_marque + "</td><td>" + reclamation.hardware_reclamation.numero_inventaire_hardware + "</td><td>" + reclamation.date_reclamation + "</td><td><button class='btn btn-outline-info' onclick='consulter_reclamation(" + reclamation.id_reclamation + ")'>Voir Réclamation</button></td>" + add_technicien + "<td><button class='btn btn-outline-danger' onclick='supprimer_reclamation(" + reclamation.id_reclamation + ")'>Supprimer</button></td></tr>")
    });
    division_table = 10
    load_table_reclamation(header, footer, body, division_table)
}


function load_table_reclamation(header, footer, body, division_table) {
    get_data_ready_load_table("table-reclamation", header, footer, body, division_table)
    get_data_ready_pagination("pagination-reclamation", liste_reclamation.length, division_table, "dataTable_info_reclamation", "reclamations")
}

function consulter_reclamation(id_reclamation) {
    my_message = liste_reclamation.find(reclamation => reclamation.id_reclamation === id_reclamation)
    document.getElementById("hidden-big-div").style.display = "block";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 0
    }
    document.getElementById("reclamation-data").innerHTML = "Par " + my_message.utilisateur_reclamation.nom_utilisateur + " " + my_message.utilisateur_reclamation.prenom_utilisateur + ", " + my_message.date_reclamation
    document.getElementById("reclamation-sujet").innerText = "Hardware : " + my_message.hardware_reclamation.modele_hardware.nom_modele + " " + my_message.hardware_reclamation.modele_hardware.marque_modele.nom_marque + " " + my_message.hardware_reclamation.numero_inventaire_hardware
    document.getElementById("reclamation-contenu").innerHTML = my_message.description_reclamation
}

function fermer_reclamation() {
    document.getElementById("hidden-big-div").style.display = "none";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 3
    }
}

function supprimer_reclamation(id_reclamation) {
    if (confirm('Voulez-vous vraiment supprimer cette réclamation ?')) {
        var xhr = new XMLHttpRequest();
        xhr.open('DELETE', '/reclamation/delete-reclamation/' + id_reclamation, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageReclamation()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function consulter_description_technicien(idr) {
    my_message = liste_reclamation.find(reclamation => reclamation.id_reclamation === idr)
    document.getElementById("hidden-big-div").style.display = "block";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 0
    }
    document.getElementById("reclamation-data").innerHTML = "Par " + my_message.technicien_reclamation.nom_utilisateur + " " + my_message.technicien_reclamation.prenom_utilisateur + ", " + my_message.date_technicien_reclamation
    document.getElementById("reclamation-sujet").innerText = "Hardware : " + my_message.hardware_reclamation.modele_hardware.nom_modele + " " + my_message.hardware_reclamation.modele_hardware.marque_modele.nom_marque + " " + my_message.hardware_reclamation.numero_inventaire_hardware
    document.getElementById("reclamation-contenu").innerHTML = my_message.description_technicien_reclamation
}

function load_backend_pagination(pages, current_page, nombre_totale, len) {
    var pagination = document.getElementById("pagination-reclamation");
    pagination.innerHTML = ""
    disable_prev = ''
    if (current_page === 1) {
        disable_prev = 'disabled'
    }
    pagination.innerHTML += `<li class="page-item"><button class="page-link ${disable_prev}" onclick="get_page_backend(${current_page - 1})" aria-label="Previous" ><span aria-hidden="true">«</span></button></li>`
    for (var i = 1; i <= pages; i++) {
        active = ''
        if (i === current_page) {
            active = 'active'
        }
        pagination.innerHTML += `<li id="button-pagination-${i}" class="page-item ${active}"><button onclick="get_page_backend(${i})" class="page-link">${i}</button></li>`
    }
    disable_next = ''
    if (current_page === pages) {
        disable_next = 'disabled'
    }
    pagination.innerHTML += `<li class="page-item"><button class="page-link ${disable_next}" onclick="get_page_backend(${current_page + 1})" aria-label="Next" ><span aria-hidden="true">»</span></button></li>`
    load_pagination_backend_status(10, nombre_totale, current_page, len)
}

function load_pagination_backend_status(dt, nombre_totale, current_page, len) {
    var pagination = document.getElementById("dataTable_info_reclamation");
    pagination.innerHTML = ""
    pagination.innerHTML += `Affichage de ${dt * (current_page - 1) + 1} à ${(dt * current_page) - (10 - len)} sur ${nombre_totale} reclamations`
}

function get_page_backend(p) {
    let status = document.getElementById("etat_reclamation").value
    var user_code = document.getElementById("utilisateur-reclamation").value
    var num_inv = document.getElementById("num-inv-reclamation").value
    load_page_reclamation(p, status, user_code, num_inv)
}