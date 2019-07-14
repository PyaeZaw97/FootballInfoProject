 $(document).ready(function() {
    teamid();


 	     $("#addplayer").click(function(){

        var Name=document.getElementById("name").value;
        var Age=document.getElementById("age").value;
        var Club=document.getElementById("club").value;
        var Position=document.getElementById("position").value;
        var Birthdate=document.getElementById("birthdate").value;
        var Nationality=document.getElementById("nationality").value;
        var InfoId=$("#teamid option:selected").val();

        var post_data = {
        "id": 4,
        "Name": Name,
        "Age": Age,
        "Club": Club,
        "Position": Position,
        "Birthdate": Birthdate,
        "Nationality": Nationality,
        "InfoId": InfoId,

        

        }
    $.ajax({
                        type    : 'POST',
                        contentType : 'application/json; charset=utf-8',
                        url     : "http://localhost:8000/player/",
                        data    : JSON.stringify(post_data),
                        dataType: "json",
                        contentType: "application/json",
                        success: function addplayer(data){
                            alert("success! You added New Player");
                             window.location.assign("player_list.html")
                        }
                    });
 	});




function teamid() {
    $.ajax({
                        type    : 'GET',
                        contentType : 'application/json; charset=utf-8',
                        url     : "http://localhost:8000/team/",
                        dataType: "json",
                        contentType: "application/json",

            }).then(function(data){
        for(var i=0;i<data.length;i++){
            var val = data[i].id;
            var text = data[i].TeamName;
            var option = document.createElement("option");
            option.text = text;
            option.value = val;
            var select = document.getElementById("teamid");
            select.appendChild(option);
        }
    });



};
});

