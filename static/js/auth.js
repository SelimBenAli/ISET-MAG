function openPageSignUpClient() {
    window.location.href = "/client/sign-up";
}

function openPageContactClient() {
    window.location.href = "/client/contact";
}

function openPageLocationClient() {
    window.location.href = "/client/location";
}

function openPageReclamationClient() {
    window.location.href = "/client/reclamation/new";
}

function openPageHistoriqueMaterielleClient() {
    window.location.href = "/client/historique-materielle";
}

function openPageHistoriqueReclamationClient() {
    window.location.href = "/client/historique-reclamation";
}

function openPageHistoriqueLocationClient() {
    window.location.href = "/client/historique-location";
}

function openPageReclamationActiveClient() {
    window.location.href = "/client/reclamation-active";
}

function openPageFermerReclamationClient(idr) {
    window.location.href = "/client/fermer-reclamation/" + idr;
}

function logout_request() {
    window.location.href = "/auth/logout";
}

function client_login_request() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var login_btn = document.getElementById("login-btn");
    login_btn.disabled = true;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/auth/client-login-request', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                login_btn.disabled = false;
                openPageHistoriqueMaterielleClient();
            } else {
                login_btn.disabled = false;
                alert("Erreur d'authentification");
                alert(response.message);
            }
        }
    };
    xhr.send(JSON.stringify({email: email, password: password}));
}