window.addEventListener("load",function(){
    function checkDarkSetting(){
        let storageDark = localStorage.getItem("darkModeValue");
        let defaultColours = document.getElementsByClassName("main-content");
        let defaultColoursNav = document.getElementsByClassName("navbar");
        let defaultColoursFooter = document.getElementById("footer");
        let defaultColoursbtn = document.getElementsByClassName("btn");
        let defaultIconColours = document.getElementsByClassName("footer-icon");
        if (storageDark === "True"){
            for (let i = 0; i < defaultColours.length; i++){
                defaultColours[i].classList.remove("secondary-content-colour");
                defaultColours[i].classList.add("dark-mode-colour-secondary");
            }
            for (let i = 0; i < defaultColoursNav.length; i++){
                defaultColoursNav[i].classList.add("dark-mode-colour-nav");
                defaultColoursNav[i].classList.remove("main-content-colour");
                
            }
            defaultColoursFooter.classList.add("dark-mode-colour-footer");
        
            for (let i = 0; i < defaultColoursbtn.length; i++){
                defaultColoursbtn[i].classList.add("tertiary-dark-colour");
                defaultColoursbtn[i].classList.remove("button-style");
                
            }
            for (let i = 0; i < defaultIconColours.length; i++){
                defaultIconColours[i].classList.add("tertiary-dark-colour");
                
            }
        } else if (storageDark === "False"){
            for (let i = 0; i < defaultColours.length; i++){
                defaultColours[i].classList.add("secondary-content-colour");
                defaultColours[i].classList.remove("dark-mode-colour-secondary");
            }
            for (let i = 0; i < defaultColoursNav.length; i++){
                defaultColoursNav[i].classList.remove("dark-mode-colour-nav");
                defaultColoursNav[i].classList.add("main-content-colour");
                
            }
            defaultColoursFooter.classList.remove("dark-mode-colour-footer");
        
            for (let i = 0; i < defaultColoursbtn.length; i++){
                defaultColoursbtn[i].classList.remove("tertiary-dark-colour");
                defaultColoursbtn[i].classList.add("button-style");
                
            }
            for (let i = 0; i < defaultIconColours.length; i++){
                defaultIconColours[i].classList.remove("tertiary-dark-colour");
                
            }
        } else {
            return;
        }
    }
    checkDarkSetting();
});