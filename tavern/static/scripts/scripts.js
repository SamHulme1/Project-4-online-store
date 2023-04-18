window.onload=function(){
    /*
    onload find the element with the id of back-button and assign it
    conditional statement to check if the assisened backButton is equal to null
    if it is do nothing 
    if it isn't assign it an onclick event listener 
    conditional statement is used to eliminate typeError when the loaded document doesn't have a back button
    */
    let messageButton = document.getElementById("message-button");
    let messageDisplay = document.getElementById("message-area");
    let notificationStatus = document.getElementById("notification");
    messageButton.addEventListener("click", function viewMessages(){
        notificationStatus.innerHTML = 
        `<div id="message-button" class="btn">
        <i class="fa-solid fa-bell notification-icon"></i>
        </div>
        <span id="notification-status-none" class="text-center">0</span>
        `;
        messageDisplay.removeAttribute("class");
        });
    
    let messageButtonMobile = document.getElementById("message-button-mobile");
    let messageDisplayMobile = document.getElementById("message-area");
    messageButtonMobile.addEventListener("click", function viewMessages(){
        notificationStatus.innerHTML = 
        `<div id="message-button-mobile" class="btn">
        <i class="fa-solid fa-bell notification-icon"></i>
        </div>
        <span id="notification-status-none-mobile" class="text-center">0</span>
        `;
        messageDisplayMobile.removeAttribute("class");
        });
    let catagory = document.getElementsByClassName("name-of-catagory");
    for (let i = 0; i < catagory.length; i++){
        if (catagory[i].innerText === "None"){
            console.log(catagory[i])
            catagory[i].innerText = "uncatagorised";
        }
    }
    let catagoryTitle = document.getElementsByClassName("catagory-name");
    for (let i = 0; i < catagoryTitle.length; i++){
        if (catagoryTitle[i].innerText === "None"){
            catagoryTitle[i].innerText = "uncatagorised";
        }
    }
}




