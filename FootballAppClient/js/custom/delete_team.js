$(document).ready(function() {
var SearchString = window.location.search.substring(1);
    $.ajax({
        url:"http://localhost:8000/team/"
    }).then(function(data) {
        console.log(SearchString);
    });        $.ajax({
                        type    : 'DELETE',
                        contentType : 'application/json; charset=utf-8',
                        url:"http://localhost:8000/team/"+SearchString+"/",
                        //data    : JSON.stringify(post_data),
                        dataType: "json",
                        contentType: "application/json",
                        success: function(data){
                            alert("success! Delete Your Team List");
                             window.location.assign("team_list.html")
                        }
                    });
    });

