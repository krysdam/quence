// Load first3 and last3 lists from files.
// Don't let the user generate a password until the lists are loaded.
let first3 = [];
let last3 = [];

document.getElementById("generate").disabled = true;
Promise.all([
    loadList('first3.txt').then(list => first3 = list),
    loadList('last3.txt').then(list => last3 = list)
]).then(() => {
    document.getElementById("generate").disabled = false;
    document.getElementById("copy").disabled = false;
});

/**
 * Load a list of words from a file.
 */
function loadList(fname) {
    return fetch(fname)
        .then(response => response.text())
        .then(text =>
            text.split('\n').map(f => f.trim()).filter(f => f)
        )
        .catch(error => {
            console.error(`Failed to load ${fname}:`, error);
        })
}

/**
 * Return a random element from an array.
 */
function getRandomElement(arr) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    return arr[randomIndex];
}

/**
 * Generate a random 6-letter word.
 */
function getRandomWord() {
    const word = getRandomElement(first3) + getRandomElement(last3);
    return word;
}

/**
 * Generate a random password (word-word-word).
 */
function getRandomPassword() {
    const password = getRandomWord()
        + "-" + getRandomWord()
        + "-" + getRandomWord();
    return password;
}

/**
 * Generate a random password and display it.
 */
function generatePassword() {
    const password = getRandomPassword();
    document.getElementById("password").value = password;
    document.getElementById("copy").innerText = "Copy";
}

/**
 * Copy the current password to the clipboard.
 */
function copyToClipboard() {
    const passwordField = document.getElementById("password");
    navigator.clipboard.writeText(passwordField.value).then(() => {
        document.getElementById("copy").innerText = "Copied!";
        setTimeout(() => {
            document.getElementById("copy").innerText = "Copy";
        }, 2000);
    }).catch(error => {
        console.error("Failed to copy text:", error);
    });
}