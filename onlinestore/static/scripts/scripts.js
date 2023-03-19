window.onload=function(){
    /*
    onload find the element with the id of back-button and assign it
    conditional statement to check if the assisened backButton is equal to null
    if it is do nothing 
    if it isn't assign it an onclick event listener 
    conditional statement is used to eliminate typeError when the loaded document doesn't have a back button
    */
    let backButton = document.getElementById("back-button");
    if (backButton == null){
    } else {
        backButton.addEventListener("click", function backToResults(){
            history.back()
        });
    }
}


