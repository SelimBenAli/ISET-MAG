var liste_utilisateur_tous = []
var liste_utilisateur = []
var division_table = 20

function load_page_utilisateur() {
    enter_loading_mode()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/user/get-utilisateurs', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                liste_utilisateur = response.utilisateurs
                liste_utilisateur_tous = response.utilisateurs
                load_table_utilisateur_parameters()
                quit_loading_mode()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_utilisateur() {
    var search = document.getElementById("nom-utilisateur").value;
    var search_code = document.getElementById("code-utilisateur").value = "";
    if (search === "") {
        liste_utilisateur = liste_utilisateur_tous
    }
    liste_utilisateur = liste_utilisateur_tous.filter(utilisateur => (utilisateur.nom_utilisateur.includes(search.toUpperCase()) || utilisateur.prenom_utilisateur.includes(search.toUpperCase())))
    load_table_utilisateur_parameters()
}

function search_utilisateur_code() {
    var search = document.getElementById("code-utilisateur").value;
    var search_nom = document.getElementById("nom-utilisateur").value = "";
    if (search === "") {
        liste_utilisateur = liste_utilisateur_tous
    }
    liste_utilisateur = liste_utilisateur_tous.filter(utilisateur => (utilisateur.code_a_barre_utilisateur.includes(search)))
    load_table_utilisateur_parameters()
}

function load_table_utilisateur_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Prenom</th><th>Email</th><th>Téléphone</th><th>Role</th><th>Compte</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Prenom</th><th>Email</th><th>Téléphone</th><th>Role</th><th>Compte</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_utilisateur.forEach(utilisateur => {
        bouton_compte = "<button class='btn btn-outline-dark' onclick='desactiver_compte(" + utilisateur.id_utilisateur + ")'>Désactiver</button>"
        if (utilisateur.compte_utilisateur === "Pas Encore Confirmé") {
            bouton_compte = "<p class='text-danger' >Pas Encore Confirmé</p>"
        }
        else if (utilisateur.compte_utilisateur === "Banni") {
            bouton_compte = "<button class='btn btn-outline-info' onclick='activer_compte(" + utilisateur.id_utilisateur + ")'>Activer</button>"
        }
        body.push("<tr><td>" + utilisateur.code_utilisateur + "</td><td>" + utilisateur.nom_utilisateur + "</td><td>" + utilisateur.prenom_utilisateur + "</td><td>" + utilisateur.mail_utilisateur + "</td><td>" + utilisateur.telephone_utilisateur + "</td><td>" + utilisateur.role_utilisateur.nom_role + "</td><td>" + bouton_compte + "</td><td><button class='btn btn-outline-secondary' onclick='openPageUtilisateurUpdate(" + utilisateur.id_utilisateur + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_utilisateur(" + utilisateur.id_utilisateur + ")'>Supprimer</button></td></tr>")
    });
    division_table = 20
    load_table_utilisateur(header, footer, body, division_table)
}


function load_table_utilisateur(header, footer, body, division_table) {
    get_data_ready_load_table("table-utilisateur", header, footer, body, division_table)
    get_data_ready_pagination("pagination-utilisateur", liste_utilisateur.length, division_table, "dataTable_info_utilisateur", "utilisateurs")
}

function ajout_utilisateur() {
    var nom = document.getElementById("nom-utilisateur").value;
    var prenom = document.getElementById("prenom-utilisateur").value;
    var email = document.getElementById("email-utilisateur").value;
    var telephone = document.getElementById("telephone-utilisateur").value;
    var role = document.getElementById("role-utilisateur").value;
    var code = document.getElementById("code-utilisateur").value;

    if (nom === "" ) {
        alert("Nom est vide")
    }
    else if (prenom === "" ) {
        alert("Prenom est vide")
    }
    else if (email === "" ) {
        alert("Email est vide")
    }
    else if (telephone === "" ) {
        alert("Téléphone est vide")
    }
    else if (role === "" ) {
        alert("Role est vide")
    }
    else if (code === "" ) {
        alert("Code est vide")
    }
    else {
        ajout_utilisateur_request()
    }

}

function ajout_utilisateur_request() {
    var nom = document.getElementById("nom-utilisateur").value;
    var prenom = document.getElementById("prenom-utilisateur").value;
    var email = document.getElementById("email-utilisateur").value;
    var telephone = document.getElementById("telephone-utilisateur").value;
    var role = document.getElementById("role-utilisateur").value;
    var code = document.getElementById("code-utilisateur").value;
    var btn = document.getElementById("add-user-btn")
    btn.disabled = true
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/add-utilisateur', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                openPageUtilisateur()
            } else {
                alert('Erreur');
                btn.disabled = false
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_utilisateur: nom,
        prenom_utilisateur: prenom,
        email_utilisateur: email,
        telephone_utilisateur: telephone,
        role_utilisateur: role,
        code_utilisateur: code
    }));
}

function modifier_utilisateur(id_utilisateur) {
    var nom = document.getElementById("nom-utilisateur").value;
    var prenom = document.getElementById("prenom-utilisateur").value;
    var email = document.getElementById("email-utilisateur").value;
    var telephone = document.getElementById("telephone-utilisateur").value;
    var role = document.getElementById("role-utilisateur").value;
    var code = document.getElementById("code-utilisateur").value;
    if (nom === "" ) {
        alert("Nom est vide")
    }
    else if (prenom === "" ) {
        alert("Prenom est vide")
    }
    else if (email === "" ) {
        alert("Email est vide")
    }
    else if (telephone === "" ) {
        alert("Téléphone est vide")
    }
    else if (role === "" ) {
        alert("Role est vide")
    }
    else if (code === "" ) {
        alert("Code est vide")
    }
    else {
        modifier_utilisateur_request(id_utilisateur)
    }
}

function modifier_utilisateur_request(id_utilisateur) {
    var nom = document.getElementById("nom-utilisateur").value;
    var prenom = document.getElementById("prenom-utilisateur").value;
    var email = document.getElementById("email-utilisateur").value;
    var telephone = document.getElementById("telephone-utilisateur").value;
    var role = document.getElementById("role-utilisateur").value;
    var code = document.getElementById("code-utilisateur").value;
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/user/update-utilisateur/' + id_utilisateur, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                openPageUtilisateur()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_utilisateur: nom,
        prenom_utilisateur: prenom,
        email_utilisateur: email,
        telephone_utilisateur: telephone,
        role_utilisateur: role,
        code_utilisateur: code
    }));
}

function activer_compte(id_utilisateur) {
    if (confirm("Voulez-vous vraiment activer ce compte?"))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/user/activer-compte/' + id_utilisateur, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageUtilisateur()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function desactiver_compte(id_utilisateur) {
    if (confirm("Voulez-vous vraiment désactiver ce compte?"))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/user/desactiver-compte/' + id_utilisateur, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageUtilisateur()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function desactiver_tous() {
    if (confirm("Voulez-vous vraiment désactiver tous les comptes?"))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/user/desactiver-tous-compte', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageUtilisateur()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function activer_tous() {
    if (confirm("Voulez-vous vraiment activer tous les comptes?"))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/user/activer-tous-compte', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageUtilisateur()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}

function supprimer_utilisateur(id_utilisateur) {
    if (confirm("Voulez-vous vraiment supprimer cet utilisateur?"))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('DELETE', '/user/delete-utilisateur/' + id_utilisateur, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.status === 'success') {
                    openPageUtilisateur()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}