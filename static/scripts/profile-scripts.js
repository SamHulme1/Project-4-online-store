window.onload=function(){
    //removes the default d from the userinfo forms
    //adds placeolders
    let profileInfoInput=document.getElementsByTagName("label");
    for (let i = 0; i < profileInfoInput.length; i++) {
        removeDefault = profileInfoInput[i].innerText.slice(1);
        profileInfoInput[i].innerText = removeDefault;
        profileInfoInput[i].nextElementSibling.placeholder = removeDefault;
      }
}