function save_scanner_ending() {
    var scan_ending = document.getElementById('scan-ending-select').value;
    if (confirm("Confirmer la modification ?")) {
        {
            var xhr = new XMLHttpRequest();
            xhr.open('PUT', '/parameter/parametre-scanner-update', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);

                    if (response.status === 'success') {
                        openPageAdminSettings()
                    } else {
                        alert('Erreur');
                    }
                }
            };
            xhr.send(JSON.stringify({scan_ending: scan_ending}));
        }
    }
}