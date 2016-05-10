//make the default start and end date today's date 

$('#start-date').datepicker({ dateFormat: 'mm/dd/yy'}).datepicker("setDate", new Date());

$('#end-date').datepicker({ dateFormat: 'mm/dd/yy'}).datepicker("setDate", new Date());

//alert the user when they click save on a complete form

$("#form").submit(function(evt) {
    alert("Thank you! This schedule is complete.");
    evt.preventDefault();
});

//when all required fields are complete, change color of save button to yellow

function checkInputs() { $(".required").keyup(function(){
    
    var empty = false;
    $(".required").each(function() {
        if ($(this).val() === '') {
             empty = true;
            }
        });
    if (empty) {
      $("#save").css("background-color", "white");
    }
    else {
      $("#save").css("background-color", "yellow");
    }
});
}

checkInputs();
//initialize date picker for start and end dates

$(function() {
    $("#start-date").datepicker({
         inline: true,
          showOtherMonths: true,
    });
  });

$(function() {
    $("#end-date").datepicker({
         inline: true,
         showOtherMonths: true,
    });
  });


function checkStartTime() { $("#start-time").keyup(function(){
  var VAL = $(this).val();

  var validTime = new RegExp('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$');

  if (validTime.test(VAL)) {
    $("#start-time").css("background-color", "grey");
  }
  else {
    alert("invald entry");
  }
});
}

checkStartTime();

function formatAsDollars() {
  var price = document.getElementById("#price");
  price.value = '$' + price.value.replace(/[^\d]/g,'').replace(/(\d\d?)$/,'.$1');
}



