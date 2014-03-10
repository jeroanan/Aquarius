var byTitleShowing = false;

function toggleByTitle() {
     if (byTitleShowing == false) {
    showByTitle();
 }
 else {
    hideByTitle();
 }
     return false;
  }

function showByTitle() {
 byTitleShowing = true;
 document.getElementById("bytitle").style.display="";
}

  function hideByTitle() {
     byTitleShowing = false;
 document.getElementById("bytitle").style.display="none";
  }