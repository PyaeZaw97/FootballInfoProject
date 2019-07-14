$(document).ready(function() {

    $.ajax({
        url: "http://localhost:8000/player/"
    }).then(function(data) {
        console.log(data);

        for (var i = 0; i < data.length; i++) {
        var tr = $('<tr/>');

              $(tr).append("<td>" + data[i].Name+"</td>");
              $(tr).append("<td>" + data[i].Age+"</td>");
              $(tr).append("<td>" + data[i].Club+"</td>");
              $(tr).append("<td>" + data[i].Position+"</td>");
              $(tr).append("<td>" + data[i].Birthdate+"</td>");
              $(tr).append("<td>" + data[i].Nationality+"</td>");
              $(tr).append("<td><a href=player_list.html?"+data[i].id+" id='deleteProduct' class='btn btn-danger'>Delete</a></td>");
              $(tr).append("<td><a href=edit_player.html?"+data[i].id+" class='btn btn-primary'>Edit</a></td>");
              
              $('#player_list').append(tr);
          }

      $('#player_table').DataTable();
} );



      });

