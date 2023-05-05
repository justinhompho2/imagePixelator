//jQuery requires a server to work. We are serverless as of now

function onPageLoad() {
    console.log("https://youtu.be/Ffx56ZqZoIM");
}

window.addEventListener("load", onPageLoad);

function onClick(){
    console.log("IFYKYK otherwise this is completely SFW");
    location.replace("https://youtu.be/Ffx56ZqZoIM");
}

function goToInsta(){
    location.replace("https://www.instagram.com/");
}

function goToTwit() {
    location.replace("https://twitter.com/")
}

function goToFace() {
    location.replace("https://www.facebook.com/")
}

function onHover(caller) {
    if (caller.classList.contains('upload_button')) {
        caller.style.backgroundColor = "blue";
    } else if (caller.classList.contains('download_button')) {
        caller.style.backgroundColor = "darkorange";
    } else if (caller.classList.contains("popup_button")) {
        caller.style.backgroundColor = "green";
    }

    
}

function offHover(caller) {
    if (caller.classList.contains('upload_button')) {
        caller.style.backgroundColor = "lightblue";
    } else if (caller.classList.contains('download_button')) {
        caller.style.backgroundColor = "orange";
    } else if (caller.classList.contains("popup_button")) {
        caller.style.backgroundColor = "yellowgreen";
    }
}