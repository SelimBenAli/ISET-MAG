let lastKeyTime = 0;
let buffer = '';
let enterCount = 0;
const DOUBLE_ENTER_THRESHOLD = 100; // milliseconds between enters
const SCANNER_SPEED_THRESHOLD = 50; // milliseconds, typical scanner speed
let currentEnding = 'doubleEnter';

const resultDiv = document.getElementById('result');

function getEnding(e) {
    currentEnding = e;
    console.log('Scanner ending set to:', e);
}

document.body.addEventListener('keydown', function (event) {
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

        case 'space':
            if (event.key === ' ') {
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
});

function processBarcode(code) {
    if (code.length > 0) {
        resultDiv.textContent = 'Last scanned: ' + code;
        console.log('Barcode scanned:', code);
        buffer = '';
    }
}

// Removed checkOtherEndings and suggestEnding functions
