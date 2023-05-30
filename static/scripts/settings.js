window.onload=function(){
    function setLocal(){
        let darkModeValue = document.getElementById("settings-darkmode-value").innerText;
        if (messageButton === null){
        return;
        }else{      
        localStorage.setItem("darkModeValue", darkModeValue);
      }
    }

    function checkDarkSetting(){
        let defaultColours = document.getElementsByClassName("main-content");
        for (let i = 0; i < defaultColours.length; i++){
            defaultColours[i].classList.remove("secondary-content-colour");
            defaultColours[i].classList.add("dark-mode-colour-secondary");
        }
        let defaultColoursNav = document.getElementsByClassName("navbar");
        for (let i = 0; i < defaultColoursNav.length; i++){
            defaultColoursNav[i].classList.add("dark-mode-colour-nav");
            defaultColoursNav[i].classList.remove("main-content-colour");
            
        }
        let defaultColoursFooter = document.getElementById("footer");
        defaultColoursFooter.classList.add("dark-mode-colour-footer");
    
        let defaultColoursbtn = document.getElementsByClassName("btn")
        for (let i = 0; i < defaultColoursbtn.length; i++){
            defaultColoursbtn[i].classList.add("tertiary-dark-colour");
            defaultColoursbtn[i].classList.remove("button-style");
            
        }
        let defaultIconColours = document.getElementsByClassName("footer-icon")
        for (let i = 0; i < defaultIconColours.length; i++){
            defaultIconColours[i].classList.add("tertiary-dark-colour");
            
        }
    }
    checkDarkSetting();
};