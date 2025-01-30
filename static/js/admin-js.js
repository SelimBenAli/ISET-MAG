var lien = "http://127.0.0.1:5000/static/";
function login() {
    console.log('login')
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email === '' || password === '') {
        alert('Please fill all fields');
        return;
    }
    login_request(email, password)
}

function login_request(email, password) {
    console.log(email, password)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/admin/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({email: email, password: password}));

}

function load_messages_notifications() {
    console.log('load_messages_notifications')
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/messages-notifications', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                show_messages_notifications(response.messages)
                alert_message_number(response.messages.length)
            }
        }
    };
    xhr.send();
}

function show_messages_notifications(data) {
    div = document.getElementById('messages-notifications-div');
    div.innerHTML = '<h6 class="dropdown-header">Boite de récéption</h6>';
    data.slice(0, 7).forEach(function (message) {
        div.innerHTML += `
        
                        <a class="dropdown-item d-flex align-items-center"
                                                                         href="#">
                        </div>
                        <div class="fw-bold">
                           <div class="text-truncate"><span>${message.sujet_message}</span>
                            </div>
                            <p class="small text-gray-500 mb-0">${message.utilisateur_message.nom_utilisateur} ${message.utilisateur_message.prenom_utilisateur} - ${message.date_message}</p>
                        </div>
                    </a>
                       
        `;
    })
    div.innerHTML += ' <a class="dropdown-item text-center small text-gray-500" onclick="openPageMessage()">Afficher Tous les Messages.</a>'
}

function message_notification_sound() {
    var audio = document.getElementById("sound-message")
    audio.play();
}

function alert_message_number(number) {
    var alert = document.getElementById('alert-message-number');
    if (number === 0) {
        alert.style.display = 'none';
        return;
    }
    alert.style.display = 'block';
    alert.innerHTML = number;
}

//window.onload = load_messages_notifications;


var socket = io();
socket.on('update_admin_message', function (data) {
    console.log("updated : ", data)
    load_messages_notifications(data)
    message_notification_sound()
});

