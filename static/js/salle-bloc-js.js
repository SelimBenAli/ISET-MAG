var liste_salle_tous = []
var liste_bloc_tous = []
var liste_salle = []
var liste_bloc = []
var division_table = 7

function load_page_salle_bloc() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/salle-bloc/get-salle-and-bloc', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_salle = response.salles
                liste_bloc = response.blocs
                liste_salle_tous = response.salles
                liste_bloc_tous = response.blocs
                load_table_salle_parameters()
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send();

}

function search_salle() {
    search = document.getElementById("nom_salle").value
    liste_salle = liste_salle_tous.filter(salle => salle.nom_salle.toLowerCase().includes(search.toLowerCase()))
    load_table_salle_parameters()
}

function search_salle_by_bloc() {
    search = document.getElementById("id_bloc").value
    if (search === 'get-all') {
        liste_salle = liste_salle_tous
    } else {
        liste_salle = liste_salle_tous.filter(salle => salle.bloc_salle.id_bloc === search)
    }
    load_table_salle_parameters()
}

function search_bloc() {
    search = document.getElementById("nom_bloc").value
    liste_bloc = liste_bloc_tous.filter(bloc => bloc.nom_bloc.toLowerCase().includes(search.toLowerCase()))
    load_table_bloc_parameters()
}


function load_table_salle_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Bloc</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Bloc</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_salle.forEach(salle => {
        body.push("<tr><td>" + salle.id_salle + "</td><td>" + salle.nom_salle + "</td><td>" + salle.bloc_salle.nom_bloc + "</td><td><button class='btn btn-outline-secondary' onclick='openPageSalleUpdate(" + salle.id_salle + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_salle(" + salle.id_salle + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_salle(header, footer, body, division_table)
}


function load_table_salle(header, footer, body, division_table) {
    get_data_ready_load_table("table-salle", header, footer, body, division_table)
    get_data_ready_pagination("pagination-salle", liste_salle.length, division_table, "dataTable_info_salle", "salles")
}

function load_table_bloc_parameters() {
    header = "<thead><tr><th>Code</th><th>Nom</th><th>Modifier</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Nom</th><th>Modifier</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_bloc.forEach(bloc => {
        body.push("<tr><td>" + bloc.id_bloc + "</td><td>" + bloc.nom_bloc + "</td><td><button class='btn btn-outline-secondary' onclick='openPageBlocUpdate(" + bloc.id_bloc + ")'>Modifier</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_bloc(" + bloc.id_bloc + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_bloc(header, footer, body, division_table)
}

function load_table_bloc(header, footer, body, division_table) {
    get_data_ready_load_table("table-bloc", header, footer, body, division_table)
    get_data_ready_pagination("pagination-bloc", liste_salle.length, division_table, "dataTable_info_bloc", "blocs")
}

function switchSallePage() {
    div_salle = document.getElementById("div-salle")
    div_bloc = document.getElementById("div-bloc")
    div_salle.style.display = "block"
    div_bloc.style.display = "none"
    load_table_salle_parameters()
}

function switchBlocPage() {
    div_salle = document.getElementById("div-salle")
    div_bloc = document.getElementById("div-bloc")
    div_salle.style.display = "none"
    div_bloc.style.display = "block"
    load_table_bloc_parameters()
}

function ajout_bloc() {
    nom = document.getElementById("nom-bloc").value
    if (nom === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_bloc_request(nom)
}

function ajout_bloc_request(nom) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/salle-bloc/add-bloc', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_bloc: nom
    }));
}

function ajout_salle() {
    nom = document.getElementById("nom-salle").value
    bloc = document.getElementById("id-bloc").value
    if (nom === "" || bloc === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    ajout_salle_request(nom, bloc)
}

function ajout_salle_request(nom, bloc) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/salle-bloc/add-salle', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({
        nom_salle: nom,
        id_bloc: bloc
    }));
}

function modifier_bloc(id_bloc) {
    nom = document.getElementById("nom-bloc").value
    if (nom === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_bloc_request(id_bloc, nom)
}

function modifier_bloc_request(id_bloc, nom) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/salle-bloc/update-bloc', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Erreur lors de la modification du bloc');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_bloc: id_bloc,
        nom_bloc: nom
    }));
}

function supprimer_bloc(id_bloc) {
    confirmation = confirm("Voulez-vous vraiment supprimer ce bloc?")
    if (confirmation) {
        supprimer_bloc_request(id_bloc)
    }
}

function supprimer_bloc_request(id_bloc) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/salle-bloc/delete-bloc', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Erreur lors de la suppression du bloc');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_bloc: id_bloc
    }));
}

function modifier_salle(id_salle) {
    nom = document.getElementById("nom-salle").value
    bloc = document.getElementById("id-bloc").value
    if (nom === "" || bloc === "") {
        alert("Veuillez remplir tous les champs")
        return
    }
    modifier_salle_request(id_salle, nom, bloc)
}

function modifier_salle_request(id_salle, nom, bloc) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/salle-bloc/update-salle', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Erreur lors de la modification de la salle');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_salle: id_salle,
        nom_salle: nom,
        id_bloc: bloc
    }));
}

function supprimer_salle(id_salle) {
    confirmation = confirm("Voulez-vous vraiment supprimer cette salle?")
    if (confirmation) {
        supprimer_salle_request(id_salle)
    }
}

function supprimer_salle_request(id_salle) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/salle-bloc/delete-salle', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/salle-bloc";
            } else {
                alert('Erreur lors de la suppression de la salle');
            }
        }
    };
    xhr.send(JSON.stringify({
        id_salle: id_salle
    }));
}