function onPageLoad() {
    console.log("https://youtu.be/Ffx56ZqZoIM");
}

window.addEventListener("load", onPageLoad);

function onClick(){
    console.log("IFYKYK otherwise this is completely SFW");
    // location.replace("https://youtu.be/Ffx56ZqZoIM");
    location.href = "#active";
    //want to add transition time to this^^^^
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