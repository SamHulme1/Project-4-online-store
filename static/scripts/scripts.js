window.onload = function () {
    /*
    onload find the elements with the ids of message button, message-area and notification
    add an event lister to the message button, when a message is displayed in the template let the
    user let the user click on the button and change the html of the message to to relect the fact 
    that they have clicked on the button and they now have no new messages
    */
    let messageButton = document.getElementById("message-button");
    let messageDisplay = document.getElementById("message-area");
    let notificationStatus = document.getElementById("notification");
    let catagory = document.getElementsByClassName("name-of-catagory");
    let messageButtonMobile = document.getElementById("message-button-mobile");
    let messageDisplayMobile = document.getElementById("message-area");
    let catagoryTitle = document.getElementsByClassName("catagory-name");


    if (messageButton === null){
        return;
    }else{
        messageButton.addEventListener("click", function viewMessages(){
            notificationStatus.innerHTML = 
            `<div id="message-button" class="btn">
            <i class="fa-solid fa-bell notification-icon"></i>
            </div>
            <span id="notification-status-none" class="text-center">0</span>
            `;
            messageDisplay.removeAttribute("class");
            });
    }
    
    if (messageButton === null){
        return;
    }else{
        messageButtonMobile.addEventListener("click", function viewMessages(){
            notificationStatus.innerHTML = 
            `<div id="message-button-mobile" class="btn">
            <i class="fa-solid fa-bell notification-icon"></i>
            </div>
            <span id="notification-status-none-mobile" class="text-center">0</span>
            `;
            messageDisplayMobile.removeAttribute("class");
            });
    }
    
    if (catagory === null){
        return;
    }else{
        for (let i = 0; i < catagory.length; i++){
            if (catagory[i].innerText === "None"){
                catagory[i].innerText = "uncatagorised";
            }
        }
        for (let i = 0; i < catagoryTitle.length; i++){
            if (catagoryTitle[i].innerText === "None"){
                catagoryTitle[i].innerText = "uncatagorised";
            }
        }
    }
    
};



