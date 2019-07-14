$(document).ready(function() {

    $.ajax({
        url: "http://localhost:8000/player/"
    }).then(function(data) {
        console.log(data);
      });
} );
