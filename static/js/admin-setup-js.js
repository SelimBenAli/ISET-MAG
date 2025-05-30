var admins = []
var admins_all = []

function load_page_admins() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/admin/load-page-admins', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            admins = response.admins;
            admins_all = response.admins;
            load_admin_list(admins);
        }
    };
    xhr.send();
}

function load_admin_list(admins) {
    var table = document.getElementById("table-admins");
    table.innerHTML = "";
    table.innerHTML = `<tr>
                                    <th>ID</th>
                                    <th>Nom</th>
                                    <th>Prénom</th>
                                    <th>Email</th>
                                    <th>Récuperer</th>
                                    <th>Modifier</th>
                                    <th>Désactiver</th>
                                    <th>Supprimer</th>
                                </tr>`;
    admins.forEach(function (admin) {
        action_button = `<button class="btn btn-warning" onclick="desactivate_admin(${admin.id_admin})">Desactiver</button>`
        if (admin.desactive_admin === 1) {
            action_button = `<button class="btn btn-success" onclick="activate_admin(${admin.id_admin})">Activer</button>`
        }
        table.innerHTML += `<tr>
                                        <td>${admin.id_admin}</td>
                                        <td>${admin.nom_admin}</td>
                                        <td>${admin.prenom_admin}</td>
                                        <td>${admin.email_admin}</td>
                                        <td>
                                            <button class="btn btn-info" name="recup-btn" onclick="recuperer_admin(${admin.id_admin})">Récuperer</button>
                                        </td>
                                        <td>
                                            <button class="btn btn-secondary" onclick="modifier_admin(${admin.id_admin})">Modifier</button>
                                        </td>
                                        <td>
                                            ${action_button}
                                        </td>
                                        <td>
                                            <button class="btn btn-danger" onclick="delete_admin(${admin.id_admin})">Supprimer</button>
                                        </td>
                                    </tr>`;
    })
}

function desactivate_admin(id_admin) {
    conf = confirm("Voulez-vous vraiment désactiver cet admin ?");
    if (conf) {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', `/admin/desactivate-admin/${id_admin}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                openPageAdminUtilisateur();
            }
        };
        xhr.send();
    }
}

function search_admin() {
    nom = document.getElementById('search-admin').value;
    if (nom === "") {
        admins = admins_all;
        load_admin_list(admins);
        return;
    }
    admins = admins.filter(function (admin) {
        return admin.nom_admin.toLowerCase().includes(nom.toLowerCase());
    })
    load_admin_list(admins);
}

function activate_admin(id_admin) {
    conf = confirm("Voulez-vous vraiment activer cet admin ?");
    if (conf) {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', `/admin/activate-admin/${id_admin}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                openPageAdminUtilisateur();
            }
        };
        xhr.send();
    }
}

function ajout_admin() {
    nom = document.getElementById('nom-admin').value;
    prenom = document.getElementById('prenom-admin').value;
    email = document.getElementById('email-admin').value;
    btn = document.getElementById('my-button');
    btn.innerHTML = "En cours...";
    btn.disabled = true;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/admin/add-admin', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                openPageAdminUtilisateur();
            } else {
                alert('Error');
                btn.innerHTML = "Ajouter";
                btn.disabled = false;
            }
        }
    };
    xhr.send(JSON.stringify({nom_admin: nom, prenom_admin: prenom, email_admin: email}));
}

function delete_admin(id_admin) {
    conf = confirm("Voulez-vous vraiment supprimer cet admin ?");
    if (conf) {
        var xhr = new XMLHttpRequest();
        xhr.open('DELETE', `/admin/delete-admin/${id_admin}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                openPageAdminUtilisateur();
            }
        };
        xhr.send();

    }
}

function modifier_admin(id_admin) {
    var new_email = prompt("Entrez le nouvel email de l'admin");
    if (new_email === null) {
        alert('Opération annulée, email invalid! ');
        return;
    }
    modifier_admin_request(id_admin, new_email);
}

function modifier_admin_request(id_admin, email){

    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/admin/update-admin/' + id_admin, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                openPageAdminUtilisateur();
            } else {
                alert('Error' + response.message);
            }
        }
    };
    xhr.send(JSON.stringify({email_admin: email}));
}

function recuperer_admin(id_admin) {
    var xhr = new XMLHttpRequest();
    var rec = document.getElementsByName('recup-btn');
    rec.forEach(function (r) {
        r.disabled = true;
    });
    xhr.open('PUT', `/admin/recuperer-admin/${id_admin}`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                alert('Email de récupération envoyé avec succès à \n ' + response.email);
            } else {
                alert('Error' + response.message);
            }
        }
        rec.forEach(function (r) {
            r.disabled = false;
        });
    };
    xhr.send();
}