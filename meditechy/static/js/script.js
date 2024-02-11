
$(document).ready(function() {
 
})


function readFile() {
  var reader = new FileReader();
  var file = document.querySelector('#g-icon').files[0];
  reader.onload = function(e) {
      document.querySelector('.g-icon').src = e.target.result;
  }
  reader.readAsDataURL(file);
}

function dropDown(elem) {
    elem.siblings('.dropdown-content').toggleClass('show');
}
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.fa-ellipsis-v')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

