window.onload=function(){
    /*
    onload find the elements with the ids of value-input, devrease-qty and increase-qty assign the last 
    two click events as their buttons
    on click increase or decrease the default value per click 
    then get the input default value again and assign it the new value 
    
    */
    let IncreaseButtons = document.getElementsByClassName("increase-qty");
    for (let i = 0; i < IncreaseButtons.length; i++) {
        let current = document.querySelector('.value-input');
        let nextSibling = current.nextElementSibling;
        IncreaseButtons[i].addEventListener("click", function() {
            nextSibling.value ++;
            console.log(nextSibling.value)
        });
      }

    let DecreaseButtons = document.getElementsByClassName("decrease-qty");
    console.log(DecreaseButtons);
    for (let i = 0; i < DecreaseButtons.length; i++) {
        let current = document.querySelector('.value-input');
        let nextSibling = current.nextElementSibling;
        DecreaseButtons[i].addEventListener("click", function() {
            console.log(nextSibling.value)
            nextSibling.value --;
        });
      }


}