function openPageSignUpClient() {
    window.location.href = "/client/sign-up";
}

function openPageContactClient() {
    window.location.href = "/client/contact";
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
                window.location.href = "/client/location";
            } else {
                login_btn.disabled = false;
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({email: email, password: password}));
}