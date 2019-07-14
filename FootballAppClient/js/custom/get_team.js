$(document).ready(function() {

    $.ajax({
        url: "http://localhost:8000/team/"
    }).then(function(data) {
        console.log(data);

        for (var i = 0; i < data.length; i++) {
        var tr = $('<tr/>');

              $(tr).append("<td>" + data[i].TeamName+"</td>");
              $(tr).append("<td>" + data[i].League+"</td>");
              // $(tr).append("<td>" + data[i].Club+"</td>");
              // $(tr).append("<td>" + data[i].Position+"</td>");
              // $(tr).append("<td>" + data[i].Birthdate+"</td>");
              // $(tr).append("<td>" + data[i].Nationality+"</td>");
              $(tr).append("<td><a href=team_list.html?"+data[i].id+" id='deleteProduct' class='btn btn-danger'>Delete</a></td>");
              $(tr).append("<td><a href=edit_team.html?"+data[i].id+" class='btn btn-primary'>Edit</a></td>");
              
              $('#team_list').append(tr);
          }

      $('#team_table').DataTable();
} );



      });

