var liste_message_tous = []
var liste_message = []
var division_table = 7

function load_page_message() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/get-messages', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                liste_message = response.messages
                liste_message_tous = response.messages
                load_table_message_parameters()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send();

}

function search_message_by_user() {
    var search = document.getElementById("utilisateur-message").value
    liste_message = liste_message_tous.filter(message => message.utilisateur_message.nom_utilisateur.toLowerCase().includes(search.toLowerCase()) || message.utilisateur_message.prenom_utilisateur.toLowerCase().includes(search.toLowerCase()))
    load_table_message_parameters()
}

function search_message_by_subject() {
    var search = document.getElementById("sujet-message").value
    liste_message = liste_message_tous.filter(message => message.sujet_message.toLowerCase().includes(search.toLowerCase()))
    load_table_message_parameters()
}

function load_table_message_parameters() {
    header = "<thead><tr><th>Code</th><th>Utilisateur</th><th>Sujet</th><th>Voir</th><th>Supprimer</th></tr></thead>"
    footer = "<tfoot><tr><th>Code</th><th>Utilisateur</th><th>Sujet</th><th>Voir</th><th>Supprimer</th></tr></tfoot>"
    body = []
    liste_message.forEach(message => {
        body.push("<tr><td>" + message.id_message + "</td><td>" + message.utilisateur_message.nom_utilisateur + " " + message.utilisateur_message.prenom_utilisateur + "</td><td>" + message.sujet_message + "</td><td><button class='btn btn-outline-secondary' onclick='consulter_message(" + message.id_message + ")'>Voir</button></td><td><button class='btn btn-outline-danger' onclick='supprimer_message(" + message.id_message + ")'>Supprimer</button></td></tr>")
    });
    division_table = 7
    load_table_message(header, footer, body, division_table)
}


function load_table_message(header, footer, body, division_table) {
    get_data_ready_load_table("table-message", header, footer, body, division_table)
    get_data_ready_pagination("pagination-message", liste_message.length, division_table, "dataTable_info_message", "messages")
}

function consulter_message(id_message) {
    my_message = liste_message.find(message => message.id_message === id_message)
    console.log(my_message.contenu_message)
    document.getElementById("hidden-big-div").style.display = "block";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 0
    }
    document.getElementById("message-data").innerHTML = "Par " + my_message.utilisateur_message.nom_utilisateur + " " + my_message.utilisateur_message.prenom_utilisateur + ", " + my_message.date_message
    document.getElementById("message-sujet").innerText = "Sujet : " +  my_message.sujet_message
    document.getElementById("message-contenu").innerHTML =  my_message.contenu_message
}

function fermer_message() {
    document.getElementById("hidden-big-div").style.display = "none";
    l = document.getElementsByClassName("page-link")
    for (i = 0; i < l.length; i++) {
        l[i].style.zIndex = 3
    }
}

function supprimer_message(id_message) {
    if (confirm('Voulez-vous vraiment supprimer ce message ?')) {
        var xhr = new XMLHttpRequest();
        xhr.open('DELETE', '/message/delete-message/' + id_message, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                console.log(response)
                if (response.status === 'success') {
                    load_page_message()
                } else {
                    alert('Erreur');
                }
            }
        };
        xhr.send();
    }
}