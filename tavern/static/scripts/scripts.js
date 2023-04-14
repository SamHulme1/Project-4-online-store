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
}


