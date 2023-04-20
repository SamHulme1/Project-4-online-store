window.onload=function(){
    /*
    onload class select all the buttons, 
    loop through them and select all the elements that contain the quantity values
    find the next sibling of the quantity values element using the index of the button
    add and event listener for each button at the same index which increases or decrease 
    the value of the quatity button by 1 
    
    */
    let IncreaseButtons = document.getElementsByClassName("increase-qty");
    let DecreaseButtons = document.getElementsByClassName("decrease-qty");

    if(IncreaseButtons===null){
        return;
    } else {
        let quantityValue = document.querySelectorAll('.value-input');
        for (let i = 0; i < IncreaseButtons.length; i++) {
            let nextSibling = quantityValue[i].nextElementSibling;
            IncreaseButtons[i].addEventListener("click", function() {
                nextSibling.value ++;
            });
          }
    }

    if(DecreaseButtons===null){
        return;
    } else { 
        let quantityValue = document.querySelectorAll('.value-input');
        for (let i = 0; i < DecreaseButtons.length; i++) {
            let nextSibling = quantityValue[i].nextElementSibling;
            DecreaseButtons[i].addEventListener("click", function() {
                nextSibling.value --;
            });
          }
    }

};