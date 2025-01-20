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