function load_page_admins() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/admin/load-page-admins', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var admins = response.admins;
            var table = document.getElementById("table-admins");
            table.innerHTML = "";
            table.innerHTML = `<tr>
                                    <th>ID</th>
                                    <th>Nom</th>
                                    <th>Prénom</th>
                                    <th>Email</th>
                                    <th>Désactiver</th>
                                    <th>Supprimer</th>
                                </tr>`;
            admins.forEach(function (admin) {
                table.innerHTML += `<tr>
                                        <td>${admin.id_admin}</td>
                                        <td>${admin.nom_admin}</td>
                                        <td>${admin.prenom_admin}</td>
                                        <td>${admin.email_admin}</td>
                                        <td>
                                            <button class="btn btn-warning" onclick="desactivate_admin(${admin.id_admin})">Desactiver</button>
                                        </td>
                                        <td>
                                                                                    <button class="btn btn-danger" onclick="delete_admin(${admin.id_admin})">Supprimer</button>
                                        </td>
                                    </tr>`;
            })
        }
    };
    xhr.send();
}

function desactivate_admin(id_admin) {
    conf = confirm("Voulez-vous vraiment désactiver cet admin ?");
    if (conf)
    {
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