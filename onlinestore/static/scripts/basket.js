window.onload=function(){
    /*
    onload find the elements with the ids of value-input, devrease-qty and increase-qty assign the last 
    two click events as their buttons
    on click increase or decrease the default value per click 
    then get the input default value again and assign it the new value 
    
    */
    let quantityInput = parseInt(document.getElementById("value-input").value);
    let decreaseButton = document.getElementById("decrease-qty");
    decreaseButton.addEventListener("click", function() {
        quantityInput -- ;
        document.getElementById("value-input").value = quantityInput;
    });

    let IncreaseButton = document.getElementById("increase-qty");
    IncreaseButton.addEventListener("click", function() {
        quantityInput ++ ;
        document.getElementById("value-input").value = quantityInput;
    });

}