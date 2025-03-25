var liste_intervention_tous = []
var liste_intervention = []
var division_table = 10

function load_page_intervention(page, status, code_hard, code_user, num_hard) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-limit/' + page + '/status_' + status + '/code_hard_' + code_hard + '/code_user_' + code_user + '/num_hard_' + num_hard, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                load_backend_pagination(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function load_page_intervention_current(p) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-current/' + p, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                load_backend_pagination_current(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function load_page_intervention_closed(p) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-closed/' + p, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                load_backend_pagination_closed(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function load_table_intervention_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Hardware</th><th>Admin d'ajout</th><th>Admin de fermeture</th><th>Fermer</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Prénom</th><th>Date Début</th><th>Date Fin</th><th>Hardware</th><th>Admin d'ajout</th><th>Admin de fermeture</th><th>Fermer</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_intervention.forEach(intervention => {
        add_fermeture = "<button class='btn btn-outline-success' disabled>Fermer</button>"
        if (intervention.date_fin_intervention === null) {
            add_fermeture = "<button class='btn btn-outline-success' onclick='fermer_intervention(" + intervention.id_intervention + ")'>Fermer</button>"
            add_admin_fermeture = "Pas Encore"
        } else {
            add_admin_fermeture = intervention.admin_fermeture_intervention.nom_admin + " " + intervention.admin_fermeture_intervention.prenom_admin
        }
        body.push("<tr><td>" + intervention.id_intervention + "</td><td>" + intervention.utilisateur_intervention.nom_utilisateur + "</td><td>" + intervention.utilisateur_intervention.prenom_utilisateur + "</td><td>" + intervention.date_debut_intervention + "</td><td>" + intervention.date_fin_intervention + "</td><td>" + intervention.hardware_intervention.numero_inventaire_hardware + "</td><td>" + intervention.admin_intervention.nom_admin + " " + intervention.admin_intervention.prenom_admin + "</td><td>" + add_admin_fermeture + "</td><td>" + add_fermeture + "</td><td><button class='btn btn-outline-danger' onclick='supprimer_intervention(" + intervention.id_intervention + ")'>Supprimer</button></td></tr>")
    });
    division_table = 10
    load_table_intervention(header, footer, body, division_table)
}


function load_table_intervention(header, footer, body, division_table) {
    get_data_ready_load_table("table-intervention", header, footer, body, division_table)
    get_data_ready_pagination("pagination-intervention", liste_intervention.length, division_table, "dataTable_info_intervention", "interventions")
}

function search_intervention_by_code_user(p) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-user-code/' + p, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                // load_backend_pagination_closed(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function search_intervention_by_code_hard(p) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-hard-code/' + p, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                // load_backend_pagination_closed(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function search_intervention_by_num_hard(p) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/intervention/get-interventions-hard-num/' + p, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_intervention = response.interventions
                liste_intervention_tous = response.interventions
                load_table_intervention_parameters()
                // load_backend_pagination_closed(response.pages, response.current_page, response.nombre_totale, liste_intervention.length)
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function search_intervention_code_hard() {
    cu_div = document.getElementById('code-user-search').value = ''
    nh_div = document.getElementById('num-hardware-search').value = ''
}

function search_intervention_code_user() {
    ch_div = document.getElementById('code-hardware-search').value = ''
    nh_div = document.getElementById('num-hardware-search').value = ''
}

function search_intervention_num_inv() {
    ch_div = document.getElementById('code-hardware-search').value = ''
    cu_div = document.getElementById('code-user-search').value = ''
}

function search_intervention() {
    let status = document.getElementById('status-int').value
    if (status === 'ALL') {
        liste_intervention = liste_intervention_tous
    } else if (status === 'CURRENT') {
        liste_intervention = liste_intervention_tous.filter(intervention => intervention.date_fin_intervention === null)
    } else {
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
    if (confirm('Voulez-vous vraiment fermer cette intervention?'))
    {
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
                    load_page_intervention(1, 0, '', '', '')
                } else {
                    alert(response.message);
                    quit_loading_mode()
                    load_page_intervention(1, 0, '', '', '')
                }
            }
        };
        xhr.send();
    }
}

function supprimer_intervention(id_intervention) {
    if (confirm('Voulez-vous vraiment supprimer cette intervention?')) {
        supprimer_intervention_request(id_intervention)
    }
}

function supprimer_intervention_request(id_intervention) {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/intervention/delete-intervention/' + id_intervention, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                quit_loading_mode()
                load_page_intervention(1, 0, '', '', '')
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();
}

function search_intervention_status() {
    let status = document.getElementById('status-int').value
    let code_hard = document.getElementById('code-hardware-search').value
    let code_user = document.getElementById('code-user-search').value
    let num_hard = document.getElementById('num-hardware-search').value
    load_page_intervention(1, status, code_hard, code_user, num_hard)
}

function get_page_backend(p) {
    let status = document.getElementById('status-int').value
    let code_hard = document.getElementById('code-hardware-search').value
    let code_user = document.getElementById('code-user-search').value
    let num_hard = document.getElementById('num-hardware-search').value
    load_page_intervention(p, status, code_hard, code_user, num_hard)
}

function load_backend_pagination(pages, current_page, nombre_totale, len) {
    var pagination = document.getElementById("pagination-intervention");
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
    load_pagination_backend(10, nombre_totale, current_page, len)
}

function load_pagination_backend(dt, nombre_totale, current_page, len) {
    var pagination = document.getElementById("dataTable_info_intervention");
    pagination.innerHTML = ""
    pagination.innerHTML += `Affichage de ${dt * (current_page - 1) + 1} à ${(dt * current_page) - (10 - len)} sur ${nombre_totale} interventions`
}