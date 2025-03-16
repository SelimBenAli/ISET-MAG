let lastKeyTime = 0;
let buffer = '';
let enterCount = 0;
const DOUBLE_ENTER_THRESHOLD = 100; // milliseconds between enters
const SCANNER_SPEED_THRESHOLD = 50; // milliseconds, typical scanner speed
let currentEnding = 'doubleEnter';
var userBeginChar = 6;
var hardwareBeginChar = 7;
var barcodelength = 13;
var scann_mode = 1;

function getEnding(e) {
    currentEnding = e;
    console.log('Scanner ending set to:', e);
}

function getScannMode(mode) {
    scann_mode = mode;
    console.log('Scanner mode set to:', scann_mode);
}


function verify_user_barcode() {
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;
    if (userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar) {
        userDiv.value = '';
    }

}

function verify_hardware_barcode() {
    let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;
    if (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar) {
        hardwareDiv.value = '';
    }

}


function verify_user_barcode_place() {
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;
    console.log(typeof userValue, userValue.length !== 0 && (userValue.charAt(0) !== userBeginChar.toString() || userValue.charAt(0) !== userBeginChar))
    if (userValue.length === barcodelength && (userValue.charAt(0) === userBeginChar.toString() || userValue.charAt(0) === userBeginChar)) {
        console.log('User barcode scanned:', userValue);
        let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
        hardwareValue = hardwareDiv.value;
        if (hardwareValue.length === 0) {
            hardwareDiv.focus();
            return;
        }
        call_intervention_check_add();
    }
    console.log(userValue, userBeginChar, typeof userValue.charAt(0), typeof userBeginChar.toString(), userValue.charAt(0) !== userBeginChar.toString() || userValue.charAt(0) !== userBeginChar)
    if (userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar) {
        userDiv.value = '';
    }

}

function verify_hardware_barcode_place() {
    let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;
    console.log(hardwareValue, hardwareValue.length !== 0 && (hardwareValue.charAt(0) !== hardwareBeginChar.toString() || hardwareValue.charAt(0) !== hardwareBeginChar))
    if (hardwareValue.length === barcodelength && (hardwareValue.charAt(0) === hardwareBeginChar.toString() || hardwareValue.charAt(0) === hardwareBeginChar)) {
        console.log('Hardware barcode scanned:', hardwareValue);
        let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
        userValue = userDiv.value;
        if (userValue.length === 0) {
            userDiv.focus();
            return;
        }
        call_intervention_check_add();
    }
    if (hardwareValue.length !== 0 && (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar)) {
        hardwareDiv.value = '';
    }

}

function call_intervention_check_add() {
    console.log('Call intervention check add');
    let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
    hardwareValue = hardwareDiv.value;
    let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
    userValue = userDiv.value;
    if (hardwareValue.length !== barcodelength || (hardwareValue.charAt(0) !== hardwareBeginChar.toString() && hardwareValue.charAt(0) !== hardwareBeginChar)) {
        hardwareDiv.value = '';
        return;
    }
    if (userValue.length !== barcodelength || (userValue.charAt(0) !== userBeginChar.toString() && userValue.charAt(0) !== userBeginChar)) {
        userDiv.value = '';
        return;
    }
    console.log('Intervention check add:', userValue, hardwareValue);
    add_intervention_request(userValue, hardwareValue);
}

function add_intervention_request(userValue, hardwareValue) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/intervention/add-intervention', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                //openPageIntervention()
                const pageName = document.location.pathname.split('/').pop();
                console.log(pageName);
                if (pageName === 'intervention') {
                    load_page_intervention();
                }
                document.getElementById('code-ajout-interventien-utilisateur').value = '';
                document.getElementById('code-ajout-interventien-hardware').value = '';
                alert('Intervention ajoutée avec succès');

            } else {
                alert(response.message);
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
    console.log(inputs)
// Add focus event listener to each input element
    inputs.forEach(input => {
        input.addEventListener('focus', function () {
            console.log(`Focused element ID: ${this.id}`);
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
        console.log('Scanner mode is off');
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
    if (code.length > 0) {
        //resultDiv.textContent = 'Last scanned: ' + code;
        console.log('Barcode scanned:', code);
        buffer = '';
        let userDiv = document.getElementById('code-ajout-interventien-utilisateur');
        let hardwareDiv = document.getElementById('code-ajout-interventien-hardware');
        if (code.charAt(0) === userBeginChar.toString() || code.charAt(0) === userBeginChar) {
            userDiv.value = code;
        } else {
            hardwareDiv.value = code;
        }
    }
    verify_user_barcode_place()
}

// Removed checkOtherEndings and suggestEnding functions
