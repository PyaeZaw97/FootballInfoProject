$(document).ready(function(){
    console.log(window.location.search.substring(1));
    var SearchString = window.location.search.substring(1);
    $.ajax({
        url:"http://localhost:8000/team/"+SearchString+"/"
    }).then(function(data) {
        console.log(data);


    $('[id=teamname]').attr('value',data.TeamName);
    $('[id=league]').attr('value',data.League);
    // $('[id=club]').attr('value',data.Club);
    // $('[id=position]').attr('value',data.Position);
    // $('[id=birthdate]').attr('value',data.Birthdate);
    // $('[id=nationality]').attr('value',data.Nationality);
   
});

    $("#editteam").click(function(){

        var TeamName=document.getElementById("teamname").value;
        var League=document.getElementById("league").value;
        // var Club=document.getElementById("club").value;
        // var Position=document.getElementById("position").value;
        // var Birthdate=document.getElementById("birthdate").value;
        // var Nationality=document.getElementById("nationality").value;
        

        var post_data = {
        "id": 4,
        "TeamName": TeamName,
        "League": League,
        "Player_id": []
        }

    $.ajax({
                        type    : 'PUT',
                        contentType : 'application/json; charset=utf-8',
                        url:"http://localhost:8000/team/"+SearchString+"/",

                        data    : JSON.stringify(post_data),
                        dataType: "json",
                        contentType: "application/json",
                        success: function(data){
                            alert("success! Edit Team");
                            window.location.assign("team_list.html");
                        }
                    });
    });



});