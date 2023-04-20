window.onload=function(){
    //adds placeolders to all form elements based on there labels
    let labels = document.getElementsByTagName("label");
    for (let i = 0; i < labels.length; i++) {
        placeholderValue = labels[i].innerText
        labels[i].nextElementSibling.placeholder = placeholderValue;
      }
}