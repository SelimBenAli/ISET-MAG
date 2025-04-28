let lastKeyTime = 0;
let buffer = '';
let enterCount = 0;
const DOUBLE_ENTER_THRESHOLD = 100; // milliseconds between enters
const SCANNER_SPEED_THRESHOLD = 50; // milliseconds, typical scanner speed
let currentEnding = 'doubleEnter';
var userBeginChar = 2;
var hardwareBeginChar = 7;
var barcodelength = 13;
var scann_mode = 1;

function getEnding(e) {
    currentEnding = e;

}

function getScannMode(mode) {
    scann_mode = mode;

}


function verify_user_barcode() {
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;
    if (userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar) {
        userDiv.value = '';
    }

}

function verify_hardware_barcode() {
    var hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;
    if (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar) {
        hardwareDiv.value = '';
        console.log('hardware', hardwareDiv.value, hardwareValue);
        let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    }

}


function verify_user_barcode_place() {
    console.log('entring_verification 1')
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;

    if (userValue.length === barcodelength && (userValue.charAt(0) === userBeginChar.toString() || userValue.charAt(0) === userBeginChar)) {

        let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
        hardwareValue = hardwareDiv.value;
        if (hardwareValue.length === 0) {
            hardwareDiv.focus();
            // alert('Code matériel incorrect');
            console.log('quit verification 1')
            return;
        } else {
            console.log('continue verification 1')
            call_intervention_check_add();
        }
    }

    console.log('process verification 1')


    if ((userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar) || userValue.length !== barcodelength) {
        console.log('log verification 1')
        notifs.error('Code utilisateur incorrect');
        userDiv.value = '';
    }

}

function verify_hardware_barcode_place() {
    console.log('entring_verification 2')
    let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;

    if (hardwareValue.length === barcodelength && (hardwareValue.charAt(0) === hardwareBeginChar.toString() || hardwareValue.charAt(0) === hardwareBeginChar)) {
        console.log('writing hard 3')
        let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
        userValue = userDiv.value;
        if (userValue.length === 0) {
            userDiv.focus();
            // alert('Code utilisateur incorrect');
            console.log('quit verification 2')
            return;
        }
        console.log('continue verification 2')
        call_intervention_check_add();
    }
    console.log('process verification 2')
    if (hardwareValue.length !== barcodelength || (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar)) {
        notifs.error('Code matériel incorrect');
        console.log('log verification 2')
        hardwareDiv.value = '';
        console.log('NOT writing hard 4')
    }

}

function call_intervention_check_add() {

    let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;
    if (hardwareValue.length !== barcodelength || (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar)) {
        hardwareDiv.value = '';
        notifs.error('Code matériel incorrect');
        return;
    }
    if (userValue.length !== barcodelength || (userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar)) {
        userDiv.value = '';
        notifs.error('Code utilisateur incorrect');
        return;
    }

    add_intervention_request(userValue, hardwareValue);
}

function add_intervention_request(userValue, hardwareValue) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/intervention/add-intervention', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                //openPageIntervention()
                const pageName = document.location.pathname.split('/').pop();

                if (pageName === 'intervention') {
                    load_page_intervention(1, 0, '', '', '');
                }
                document.getElementById('code-ajout-interventien-utilisateur').value = '';
                document.getElementById('code-ajout-interventien-hardware').value = '';
                notifs.success('Prêt ajoutée avec succès');

            } else {
                notifs.warn('Erreur', 'Hardware déjà en cours d\'intervention', 3000);
                document.getElementById('code-ajout-interventien-utilisateur').value = '';
                document.getElementById('code-ajout-interventien-hardware').value = '';
            }
        }
    };
    xhr.send(JSON.stringify({user: userValue, hardware: hardwareValue}));
}

// Select all relevant input elements
function prepare_focus() {
    const inputs = document.querySelectorAll('input[type="text"], input[type="search"], input[type="number"], textarea');

// Add focus event listener to each input element
    inputs.forEach(input => {
        input.addEventListener('focus', function () {

            if (this.id !== 'code-ajout-interventien-utilisateur' &&
                this.id !== 'code-ajout-interventien-hardware') {
                var toggle = document.getElementById('toggle-intervention');
                toggle.checked = false;
                showInterventionParameters();
                scann_mode = 2;
            }
        });
    });
}


document.body.addEventListener('keydown', function (event) {
    if (scann_mode === 1 || scann_mode === '1') {
        const currentTime = new Date().getTime();
        const timeDiff = currentTime - lastKeyTime;

        // Assume scanner input if keys come very fast
        const isLikelyScanner = timeDiff < SCANNER_SPEED_THRESHOLD && timeDiff > 0;

        switch (currentEnding) {
            case 'doubleEnter':
                if (event.key === 'Enter') {
                    event.preventDefault();
                    if (isLikelyScanner) event.stopPropagation();
                    enterCount++;
                    if (enterCount === 2 && timeDiff < DOUBLE_ENTER_THRESHOLD) {
                        processBarcode(buffer);
                        enterCount = 0;
                    } else if (timeDiff >= DOUBLE_ENTER_THRESHOLD) {
                        enterCount = 1;
                        buffer = '';
                    }
                } else if (event.key.length === 1) {
                    buffer += event.key;
                    enterCount = 0;
                }
                break;

            case 'enter':
                if (event.key === 'Enter') {
                    event.preventDefault();
                    if (isLikelyScanner) event.stopPropagation();
                    processBarcode(buffer);
                    enterCount = 0;
                } else if (event.key.length === 1) {
                    buffer += event.key;
                    enterCount = 0;
                }
                break;

            case 'tab':
                if (event.key === 'Tab') {
                    event.preventDefault();
                    if (isLikelyScanner) event.stopPropagation();
                    processBarcode(buffer);
                    enterCount = 0;
                } else if (event.key.length === 1) {
                    buffer += event.key;
                    enterCount = 0;
                }
                break;

            case 'arrow':
                if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
                    event.preventDefault();
                    if (isLikelyScanner) event.stopPropagation();
                    processBarcode(buffer);
                    enterCount = 0;
                } else if (event.key.length === 1) {
                    buffer += event.key;
                    enterCount = 0;
                }
                break;
        }

        lastKeyTime = currentTime;
    } else {

        /*setTimeout(() => {
            c = confirm('Mode scanner désactivé, voulez-vous activer le mode scanner ?');
            if (c) {
                var toggle = document.getElementById('toggle-intervention');
                toggle.checked = true;
                showInterventionParameters();
                scann_mode = 1;
            }
        }, 1000);*/

    }

});

function processBarcode(code) {
    let x = 0;
    if (code.length > 0) {
        console.log('Last scanned: ' + code)


        buffer = '';
        let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
        let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
        if (code.charAt(0) === userBeginChar.toString() || code.charAt(0) === userBeginChar) {
            console.log('writing user 1')
            userDiv.value = code;
            if (hardwareDiv.value.length !== barcodelength || (hardwareDiv.value.charAt(0) !== hardwareBeginChar.toString() && hardwareDiv.value.charAt(0) !== hardwareBeginChar))
                hardwareDiv.value = '';
            x = 1
        } else {
            console.log('writing hard 2')
            hardwareDiv.value = code;
            if (userDiv.value.length !== barcodelength || (userDiv.value.charAt(0) !== userBeginChar.toString() && userDiv.value.charAt(0) !== userBeginChar))
                userDiv.value = '';
            x = 2
        }
    }
    if (x === 1) {
        verify_user_barcode_place();
    } else if (x === 2) {
        verify_hardware_barcode_place();
    }
    // verify_user_barcode_place()
}

// Removed checkOtherEndings and suggestEnding functions
