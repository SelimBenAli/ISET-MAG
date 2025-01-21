function trouver_hardware_reclamation() {
    var numero_inventaire = document.getElementById("numero_inventaire").value;
    window.location.href = "/client/reclamation/" + numero_inventaire;
}

function envoyer_reclamation() {
    var description = document.getElementById("description").value;
    var reclamation_btn = document.getElementById("reclamation-btn");
    reclamation_btn.disabled = true;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/add-reclamation', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                //reclamation_btn.disabled = false;
                openPageHistoriqueReclamationClient();
            } else {
                reclamation_btn.disabled = false;
                alert('Erreur lors de l\'envoi de la réclamation');
            }
        }
    };
    xhr.send(JSON.stringify({description: description}));
}