var liste_hardware_tous = []
var liste_hardware = []
var division_table = 20
var current_hardware = null

function load_page_hardware_liste(page) {
    enter_loading_mode();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/hardware/get-hardwares-limit/' + page, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_hardware = response.hardwares
                liste_hardware_tous = response.hardwares
                load_table_hardware_parameters();
                load_backend_pagination(response.pages, page, response.nombre_totale, response.hardwares.length);
                quit_loading_mode();
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function load_page_hardware_search_by_code(code) {
    enter_loading_mode();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/hardware/get-hardwares-by-code/' + code, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_hardware = response.hardwares
                liste_hardware_tous = response.hardwares
                load_table_hardware_parameters();
                quit_loading_mode();
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function load_page_hardware_search_by_inv(inv) {
    enter_loading_mode();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/hardware/get-hardwares-by-inv/' + inv, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_hardware = response.hardwares
                liste_hardware_tous = response.hardwares
                load_table_hardware_parameters();
                quit_loading_mode();
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}


function search_hardware_by_modele() {
    modele = document.getElementById("search-modele").value
    if (modele === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.modele_hardware.id_modele === parseInt(modele))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_marque() {
    marque = document.getElementById("search-marque").value
    if (marque === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.modele_hardware.marque_modele.id_marque === parseInt(marque))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_magasin() {
    magasin = document.getElementById("search-magasin").value
    if (magasin === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.magasin_hardware.id_magasin === parseInt(magasin))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_salle() {
    salle = document.getElementById("search-salle").value
    if (salle === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.salle_hardware.id_salle === parseInt(salle))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_etat() {
    etat = document.getElementById("search-etat").value
    if (etat === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.etat_hardware.id_etat === parseInt(etat))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_code() {
    code = document.getElementById("search-code").value
    if (code === "") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.code_hardware === code)
    }
    load_table_hardware_parameters()
}

function search_hardware_by_numero_inventaire() {
    numero_inventaire = document.getElementById("search-numero-inventaire").value
    if (numero_inventaire === "") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.numero_inventaire_hardware.toString().includes(numero_inventaire.toString()))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_code_inv_backend() {
    code_div = document.getElementById("search-code")
    numero_inventaire_div = document.getElementById("search-numero-inventaire")
    code = code_div.value
    numero_inventaire = numero_inventaire_div.value
    if (code === "" && numero_inventaire === "") {
        load_page_hardware_liste(1)
    } else {
        if (code !== "") {
            load_page_hardware_search_by_code(code)
        }
        if (numero_inventaire !== "") {
            load_page_hardware_search_by_inv(numero_inventaire)
        }
    }

}

function verify_hardware_search_code_backend() {
    numero_inventaire = document.getElementById("search-numero-inventaire")
    numero_inventaire.value = ""
}

function verify_hardware_search_inv_backend() {
    code = document.getElementById("search-code")
    code.value = ""
}

function search_hardware_by_date_achat() {
    date_achat = document.getElementById("search-date-achat").value
    if (date_achat === "") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.date_achat_hardware === date_achat)
    }
    load_table_hardware_parameters()
}

function search_hardware_by_date_mise_en_service() {
    date_mise_en_service = document.getElementById("search-date-mise-en-service").value
    if (date_mise_en_service === "") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.date_mise_en_service_hardware === date_mise_en_service)
    }
    load_table_hardware_parameters()
}

function search_hardware_by_date_ajout() {
    date_ajout = document.getElementById("search-date-ajout").value
    if (date_ajout === "") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.date_ajout_hardware === date_ajout)
    }
    load_table_hardware_parameters()
}

function search_hardware_by_fournisseur() {
    fournisseur = document.getElementById("search-fournisseur").value
    if (fournisseur === "0") {
        liste_hardware = liste_hardware_tous
    } else {
        liste_hardware = liste_hardware_tous.filter(hardware => hardware.fournisseur_hardware.id_fournisseur === parseInt(fournisseur))
    }
    load_table_hardware_parameters()
}

function search_hardware_by_all() {
    modele = document.getElementById("search-modele").value
    marque = document.getElementById("search-marque").value
    magasin = document.getElementById("search-magasin").value
    salle = document.getElementById("search-salle").value
    etat = document.getElementById("search-etat").value
    code = document.getElementById("search-code").value
    numero_inventaire = document.getElementById("search-numero-inventaire").value
    date_achat = document.getElementById("search-date-achat").value
    date_mise_en_service = document.getElementById("search-date-mise-en-service").value
    fournisseur = document.getElementById("search-fournisseur").value
    liste_hardware = liste_hardware_tous.filter(hardware => hardware.modele_hardware.id_modele === parseInt(modele) && hardware.modele_hardware.marque_modele.id_marque === parseInt(marque) && hardware.magasin_hardware.id_magasin === parseInt(magasin) && hardware.salle_hardware.id_salle === parseInt(salle) && hardware.etat_hardware.id_etat === parseInt(etat) && hardware.code_hardware === code && hardware.numero_inventaire_hardware === numero_inventaire && hardware.date_achat_hardware === date_achat && hardware.date_mise_en_service_hardware === date_mise_en_service && hardware.fournisseur_hardware.id_fournisseur === parseInt(fournisseur))
    load_table_hardware_parameters()
}

function load_table_hardware_parameters() {

    header = "<thead><tr><th>Code</th><th>Modèle</th><th>Marque</th><th>Magasin</th><th>Salle</th><th>Num Inventaire</th><th>Etat</th><th>Code à Bar</th><th>Consulter</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Modèle</th><th>Marque</th><th>Magasin</th><th>Salle</th><th>Num Inventaire</th><th>Etat</th><th>Code à Bar</th><th>Consulter</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_hardware.forEach(hardware => {
        body.push("<tr><td>" + hardware.id_hardware + "</td><td>" + hardware.modele_hardware.nom_modele + "</td><td>" + hardware.modele_hardware.marque_modele.nom_marque + "</td><td>" + hardware.magasin_hardware.nom_magasin + "</td><td>" + hardware.salle_hardware.nom_salle + "</td><td>" + hardware.numero_inventaire_hardware + "</td><td>" + hardware.etat_hardware.nom_etat + "</td><td>" + hardware.code_hardware + "</td><td><button class='btn btn-outline-info' onclick='openPageHardwareConsult(" + hardware.id_hardware + ")'>Consulter</button></td><td><button class='btn btn-outline-secondary' onclick='openPageHardwareUpdate(" + hardware.id_hardware + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_hardware(" + hardware.id_hardware + ")'>Supprimer</button></td></tr>")
    });
    division_table = 20
    load_table_hardware(header, footer, body, division_table)
}


function load_table_hardware(header, footer, body, division_table) {
    get_data_ready_load_table("table-hardware", header, footer, body, division_table)
    //load_backend_pagination()


}

function ajout_hardware() {
    if (document.getElementById("modele-hardware").value === "") {
        alert("Veuillez choisir un modèle")
        return
    }
    if (document.getElementById("fournisseur-hardware").value === "") {
        alert("Veuillez choisir un modèle")
        return
    }
    if (document.getElementById("magasin-hardware").value === "" && document.getElementById("salle-hardware").value === "") {
        alert("Veuillez choisir un magasin ou une salle")
        return
    }
    if (document.getElementById("numero-inventaire-hardware").value === "") {
        alert("Veuillez entrer un numéro d'inventaire")
        return
    }
    /*if (document.getElementById("code-hardware").value === "") {
        alert("Veuillez entrer un code à barre")
        return
    }*/
    if (document.getElementById("etat-hardware").value === "") {
        alert("Veuillez choisir un état")
        return
    }
    ajout_hardware_request()

}

function ajout_hardware_request() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/hardware/add-hardware', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                if (response.status === 'success') {
                    alert("Ajout effectué")
                    openPageHardware()
                }
            } else {
                alert('Erreur lors de l\'ajout' + response.message);
            }
        }
    };
    xhr.send(JSON.stringify({
        modele_hardware: document.getElementById("modele-hardware").value,
        fournisseur_hardware: document.getElementById("fournisseur-hardware").value,
        magasin_hardware: document.getElementById("magasin-hardware").value,
        salle_hardware: document.getElementById("salle-hardware").value,
        numero_inventaire_hardware: document.getElementById("numero-inventaire-hardware").value,
        date_achat_hardware: document.getElementById("date-achat-hardware").value,
        date_mise_en_service_hardware: document.getElementById("date-mise-en-service-hardware").value,
        // code_hardware: document.getElementById("code-hardware").value,
        etat_hardware: document.getElementById("etat-hardware").value
    }));
}

function modifier_hardware(idh) {
    if (document.getElementById("modele-hardware").value === "") {
        alert("Veuillez choisir un modèle")
        return
    }
    if (document.getElementById("fournisseur-hardware").value === "") {
        alert("Veuillez choisir un modèle")
        return
    }
    if (document.getElementById("magasin-hardware").value === "" && document.getElementById("salle-hardware").value === "") {
        alert("Veuillez choisir un magasin ou une salle")
        return
    }
    if (document.getElementById("numero-inventaire-hardware").value === "") {
        alert("Veuillez entrer un numéro d'inventaire")
        return
    }
    /*if (document.getElementById("code-hardware").value === "") {
        alert("Veuillez entrer un code à barre")
        return
    }*/
    if (document.getElementById("etat-hardware").value === "") {
        alert("Veuillez choisir un état")
        return
    }
    modifier_hardware_request(idh)

}

function modifier_hardware_request(idh) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/hardware/update-hardware/' + idh, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                if (response.status === 'success') {
                    alert("Modification effectuée")
                    openPageHardware()
                }
            } else {
                alert('Erreur lors de la modification');
            }
        }
    };
    xhr.send(JSON.stringify({
        modele_hardware: document.getElementById("modele-hardware").value,
        fournisseur_hardware: document.getElementById("fournisseur-hardware").value,
        magasin_hardware: document.getElementById("magasin-hardware").value,
        salle_hardware: document.getElementById("salle-hardware").value,
        numero_inventaire_hardware: document.getElementById("numero-inventaire-hardware").value,
        date_achat_hardware: document.getElementById("date-achat-hardware").value,
        date_mise_en_service_hardware: document.getElementById("date-mise-en-service-hardware").value,
        code_hardware: document.getElementById("code-hardware").value,
        etat_hardware: document.getElementById("etat-hardware").value
    }));
}

function supprimer_hardware(idh) {
    confirmation = confirm("Voulez-vous vraiment supprimer cet élément?")
    if (confirmation) {
        supprimer_hardware_request(idh)
    }
}

function supprimer_hardware_request(idh) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/hardware/delete-hardware/' + idh, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                if (response.status === 'success')
                {
                    alert("Suppression effectuée")
                    openPageHardware()
                }
            } else {
                alert('Erreur lors de la suppression');
            }
        }
    };
    xhr.send();
}

function openPageHardwareConsult(idh) {
    document.getElementById("hidden-big-div").style.display = "block";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 0
    }

    hardware = liste_hardware_tous.find(hardware => hardware.id_hardware === idh)
    document.getElementById("hardware-modele").innerHTML = "Modèle : " + hardware.modele_hardware.nom_modele + " " + hardware.modele_hardware.marque_modele.nom_marque
    document.getElementById("hardware-num-inv").innerHTML = "Numéro d'Inventaire : " + hardware.numero_inventaire_hardware
    document.getElementById("hardware-code").innerHTML = "Code : " + hardware.code_hardware
    document.getElementById("hardware-etat").innerHTML = "Etat : " + hardware.etat_hardware.nom_etat
    document.getElementById("hardware-date-achat").innerHTML = "Date d'Achat : " + hardware.date_achat_hardware
    document.getElementById("hardware-date-mise-service").innerHTML = "Date de Mise en Service : " + hardware.date_mise_service_hardware
    document.getElementById("hardware-date-ajout").innerHTML = "Date d'Ajout : " + hardware.date_ajout_hardware
    current_hardware = hardware.id_hardware
    load_table_hl_parameters(hardware.historique_relation_hardware)
}


function load_table_hl_parameters(liste_hl) {
    t = document.getElementById("table-hl")
    t.innerHTML = "<thead><tr><th>Code</th><th>Marque</th><th>Modèle</th><th>Numéro Inventaire</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Marque</th><th>Modèle</th><th>Numéro Inventaire</th><th>Supprimer</th></tr></tfoot>"
    body = []
    l = 0;
    liste_hl.forEach(hardware_id => {
        my_hardware = liste_hardware.find(hardware => hardware.id_hardware === hardware_id)
        l++;
        t.innerHTML += "<tr><td>" + my_hardware.id_hardware + "</td><td>" + my_hardware.modele_hardware.marque_modele.nom_marque + "</td><td>" + my_hardware.modele_hardware.nom_modele + "</td><td>" + my_hardware.numero_inventaire_hardware + "</td><td><button class='btn btn-outline-danger' onclick='supprimer_liaison(" + my_hardware.code_hardware + ")'>Supprimer</button></td></tr>"
    });
    t.innerHTML += footer

}


function fermer_hardware() {
    close_div()
    current_hardware = null
}

function close_div() {
    document.getElementById("hidden-big-div").style.display = "none";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 1
    }
}

function ajout_liason() {
    new_link = ask_for_hardware_id()
    if (new_link != null) {
        ajout_liason_request(new_link)
    }
}

function ask_for_hardware_id() {
    var id_hardware = prompt("Entrez l'ID du matériel à lier", "");
    if (id_hardware != null) {
        return id_hardware
    }
}

function ajout_liason_request(idh) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/hardware/add-hardware-link/' + current_hardware, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                if (response.status === 'success') {
                    alert("Ajout effectué")
                    liste_hardware = response.hardwares
                    liste_hardware_tous = response.hardwares
                    close_div()
                    openPageHardwareConsult(current_hardware)
                }
            } else {
                alert('Erreur lors de l\'ajout');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_hardware2: idh
    }));
}

function supprimer_liaison(idh) {
    confirmation = confirm("Voulez-vous vraiment supprimer cette liaison?")
    if (confirmation) {
        supprimer_liaison_request(idh)
    }
}

function supprimer_liaison_request(idh) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/hardware/delete-hardware-link/' + current_hardware, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                if (response.status === 'success') {
                    alert("Suppression effectuée")
                    liste_hardware = response.hardwares
                    liste_hardware_tous = response.hardwares
                    close_div()
                    openPageHardwareConsult(current_hardware)
                }
            } else {
                alert('Erreur lors de la suppression');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_hardware2: idh
    }));
}

function get_page_backend(p) {
    load_page_hardware_liste(p)
}

function previous_page_backend(p) {
    load_page_hardware_liste(p)
}

function next_page_backend(p) {
    load_page_hardware_liste(p)
}

function load_backend_pagination(pages, current_page, nombre_totale, len) {
    var pagination = document.getElementById("pagination-hardware");
    pagination.innerHTML = ""
    disable_prev = ''
    if (current_page === 1) {
        disable_prev = 'disabled'
    }
    pagination.innerHTML += `<li class="page-item"><button class="page-link ${disable_prev}" onclick="previous_page_backend(${current_page - 1})" aria-label="Previous" ><span aria-hidden="true">«</span></button></li>`
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
    pagination.innerHTML += `<li class="page-item"><button class="page-link ${disable_next}" onclick="next_page_backend(${current_page + 1})" aria-label="Next" ><span aria-hidden="true">»</span></button></li>`
    load_pagination_backend_status(20, nombre_totale, current_page, len)
}

function load_pagination_backend_status(dt, nombre_totale, current_page, len) {
    var pagination = document.getElementById("dataTable_info_hardware");
    pagination.innerHTML = ""
    pagination.innerHTML += `Affichage de ${dt * (current_page - 1) + 1} à ${(dt * current_page) - (20 - len)} sur ${nombre_totale} hardwares`
}
