window.onload=function(){
   const printButton = document.getElementById("print-button");
   const printArea = document.getElementById("print-area").innerHTML;
   const page = document.body.innerHTML;
   /*
      print the document, 
      add an event listener the button with the id of print button
      get the html within the div with the id of print-area
      get all html within the document
      set the document inner html to the html of the div
      remove the background image
      call the print function
      set the stlye of the html back to its original state
      
      */
   printButton.addEventListener("click", function(){
      document.body.innerHTML = printArea;
      document.body.style.backgroundImage = "none";
      window.print();
      document.body.innerHTML = page;
      document.body.style.backgroundImage = "url(https://images.pexels.com/photos/1151243/pexels-photo-1151243.jpeg)";
   });
  
};