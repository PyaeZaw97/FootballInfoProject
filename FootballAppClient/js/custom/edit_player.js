$(document).ready(function(){
    console.log(window.location.search.substring(1));
    var SearchString = window.location.search.substring(1);
    $.ajax({
        url:"http://localhost:8000/player/"+SearchString+"/"
    }).then(function(data) {
        console.log(data);


    $('[id=name]').attr('value',data.Name);
    $('[id=age]').attr('value',data.Age);
    $('[id=club]').attr('value',data.Club);
    $('[id=position]').attr('value',data.Position);
    $('[id=birthdate]').attr('value',data.Birthdate);
    $('[id=nationality]').attr('value',data.Nationality);
   
});

    $("#editplayer").click(function(){

        var Name=document.getElementById("name").value;
        var Age=document.getElementById("age").value;
        var Club=document.getElementById("club").value;
        var Position=document.getElementById("position").value;
        var Birthdate=document.getElementById("birthdate").value;
        var Nationality=document.getElementById("nationality").value;
        

        var post_data = {
        "id": 4,
        "Name": Name,
        "Age": Age,
        "Club": Club,
        "Position": Position,
        "Birthdate": Birthdate,
        "Nationality": Nationality,

        }

    $.ajax({
                        type    : 'PUT',
                        contentType : 'application/json; charset=utf-8',
                        url:"http://localhost:8000/player/"+SearchString+"/",

                        data    : JSON.stringify(post_data),
                        dataType: "json",
                        contentType: "application/json",
                        success: function(data){
                            alert("success! Edit Player");
                            window.location.assign("player_list.html");
                        }
                    });
    });



});