 $(document).ready(function() {
 	    $("#addteam").click(function(){

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
                        type    : 'POST',
                        contentType : 'application/json; charset=utf-8',
                        url     : "http://localhost:8000/team/",
                        data    : JSON.stringify(post_data),
                        dataType: "json",
                        contentType: "application/json",
                        success: function(data){
                            alert("success! You added New Team");
                             window.location.assign("team_list.html")
                        }
                    });
 	});
});


