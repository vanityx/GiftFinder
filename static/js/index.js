// function to show what tags a product has
function changeSize_onload(){
    document.getElementById("tag_selecter_chosen").style.minWidth+="554px";     //Adding style to the tag box. Min width 200px, the box cant be smaller than 200px
 // document.getElementById("tag_selecter_chosen").style.maxWidth+="600px";     //Adding style to the tag box. Max width 600px, the box cant be bigger than 600px
    document.getElementById("tag_selecter_chosen").style.Width+="586px";
}
function showTags(str) {
    document.getElementById("tag_selecter").innerHTML = "";
    xhttp = new XMLHttpRequest();                                               //Starts a XML request and calls it xhttp.
    xhttp.onreadystatechange = function() {                                     //Runs the function if the state changes in xhttp.

    if (this.readyState == 4 && this.status == 200) {                           //If the XML file has been downleded successfully.
    $(".chosen-select").trigger("chosen:updated");                              //Updates the tag select windows javascript file.
    changeSize_onload()
    xmlDoc = this.responseXML;                                                  //Saves XML document to the variable xmlDoc.
    tag = "";                                                                   //Declares tag as string.
    alreadyadded_selected = [];                                                 //Declares alreadyadded_selected as array/list. This will later be used to check if the tag already as been written out on the page or not.
    alreadyadded = [];                                                          //Declares alreadyadded as array/list. This will later be used to check if the tag already as been written out on the page or not.
    x = xmlDoc.getElementsByTagName("id");                                      //Selects all tags called "id" and saves them to a variable called x.
    y = xmlDoc.getElementsByTagName("name");                                    //Selects all tags called "name" and saves them to a variable called y.
    Exx = xmlDoc.getElementsByTagName("all_id");                                //Selects all tags called "all_id" and saves them to a variable called Exx.
    Exy = xmlDoc.getElementsByTagName("all_name");                              //Selects the tag called "all_name" and saves them to a variable called Exy.
    u = xmlDoc.getElementsByTagName('extendedtags');
    for (i = 0; i < Exx.length; i++) {          // for tags in                  //Loops through the length of all id's in the database. Also Declares "i" which is later used more than just this loop.
        alltags = u[0].childNodes[0].nodeValue;                                 //Selects the the first tag (u[0]...) and saves it in alltags. Because "u" has all tags in one big list.
            if(i < x.length){                                                   //Makes sure the program doesn't look for more tag than it is in the database that the product has.
                id = x[i].childNodes[0].nodeValue;
                name = y[i].childNodes[0].nodeValue;                            //Saves name as the tag the product already has on it. This value changes for each loop.
            }else{
                name=null;
            }
        all_id = Exx[i].childNodes[0].nodeValue;                                //For each loop it changes the value of all_id to the id that is on the position "i" in the array.
        all_name = Exy[i].childNodes[0].nodeValue;                              //For each loop it changes the value of all_name to the name that is on the position "i" in the array.
            if(alltags.includes(name)){                                         //Checkes if the value of "name" excists in alltags(all tags in the database).
            alreadyadded_selected[i] = name;                                    //Adds name to the list alreadyadded_selected at position "i".
                document.getElementById("tag_selecter").innerHTML += "<option value='" + id + "' selected>" + name + "</option>";           //Writes out id and tags the selected product has to the html file. Selected.

                if(alreadyadded_selected.includes(all_name)==false){                                                                        //So it doesn't skip the tags between the values.
                alreadyadded[i] = all_name;
                document.getElementById("tag_selecter").innerHTML += "<option value='" + all_id + "'>" + all_name + "</option>";
                }
            }else{

                if(alreadyadded_selected.includes(all_name)==false){
                alreadyadded[i] = all_name;
                document.getElementById("tag_selecter").innerHTML += "<option value='" + all_id + "'>" + all_name + "</option>";
                }
            }


    }
    $(".chosen-select").trigger("chosen:updated");
  }
    };
    xhttp.open("GET", "http://lon17druz01.pythonanywhere.com/productTags?product_no="+str, true);
  xhttp.send();
}
// function to show products on add tags page

$(document).ready(function() {
    $('#dropdown').change(function() {
        document.getElementById('tags_select').style.display = "block";
		$(".chosen-select").chosen({no_results_text: "Oops, nothing found!"});
    });
});

// Nav Bar

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });


// Deselect if radio-button 'no' is pressed

$("#clothing_no").click(function(){ // when the radio-button with the ID clothing_no gets select by the user, call this function
  $('option', $('#clothing')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#clothing").multiselect('refresh');
});
$("#makeup_no").click(function(){
  $('option', $('#makeup')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#makeup").multiselect('refresh');
});
$("#skincare_no").click(function(){
  $('option', $('#skincare')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#skincare").multiselect('refresh');
});
$("#jewelry_no").click(function(){
  $('option', $('#jewelry')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#jewelry").multiselect('refresh');
});
$("#reading_no").click(function(){
  $('option', $('#reading')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#reading").multiselect('refresh');
});
$("#games_no").click(function(){
  $('option', $('#games')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#games").multiselect('refresh');
});
$("#tech_no").click(function(){
  $('option', $('#tech')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#tech").multiselect('refresh');
});
$("#deco_no").click(function(){
  $('option', $('#deco')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#deco").multiselect('refresh');
});
$("#quirky_no").click(function(){
  $('option', $('#quirky')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#quirky").multiselect('refresh');
});
$("#health_no").click(function(){
  $('option', $('#health')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#health").multiselect('refresh');
});
$("#giftcard_no").click(function(){
  $('option', $('#giftcard')).each(function(element) {
    $(this).removeAttr('selected').prop('selected', false);
  });
  $("#giftcard").multiselect('refresh');
});

// questionnaire checkboxes
$(function() {
    $('input.clothing').on('change', function() {
        $('input.clothing').not(this).prop('checked', false);
    });
    $('input.makeup').on('change', function() {
        $('input.makeup').not(this).prop('checked', false);
    });
    $('input.skincare').on('change', function() {
        $('input.skincare').not(this).prop('checked', false);
    });
    $('input.reading').on('change', function() {
        $('input.reading').not(this).prop('checked', false);
    });
    $('input.jewelry').on('change', function() {
        $('input.jewelry').not(this).prop('checked', false);
    });
    $('input.games').on('change', function() {
        $('input.games').not(this).prop('checked', false);
    });
    $('input.tech').on('change', function() {
        $('input.tech').not(this).prop('checked', false);
    });
    $('input.deco').on('change', function() {
        $('input.deco').not(this).prop('checked', false);
    });
    $('input.quirky').on('change', function() {
        $('input.quirky').not(this).prop('checked', false);
    });
    $('input.health').on('change', function() {
        $('input.health').not(this).prop('checked', false);
    });
    $('input.giftcard').on('change', function() {
        $('input.giftcard').not(this).prop('checked', false);
    });

});
$(function() {
    $('#clothing').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#makeup').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#skincare').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#reading').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#jewelry').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#games').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#tech').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#deco').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#tech').multiselect({
        includeSelectAllOption: true
    });
});

$(function() {
    $('#health').multiselect({
        includeSelectAllOption: true
    });
});


$('#clothing_yes').click(function() {

    $("#id_checked_clothes").show();
});
$('#clothing_no').click(function() {
    $("#id_checked_clothes").hide();

});

$('#makeup_yes').click(function() {

    $("#id_checked_makeup").show();
});
$('#makeup_no').click(function() {
    $("#id_checked_makeup").hide();

});

$('#skincare_yes').click(function() {

    $("#id_checked_skincare").show();
});
$('#skincare_no').click(function() {
    $("#id_checked_skincare").hide();

});

$('#jewelry_yes').click(function() {

    $("#id_checked_jewelry").show();
});
$('#jewelry_no').click(function() {
    $("#id_checked_jewelry").hide();

});

$('#reading_yes').click(function() {

    $("#id_checked_reading").show();
});
$('#reading_no').click(function() {
    $("#id_checked_reading").hide();

});

$('#games_yes').click(function() {

    $("#id_checked_games").show();
});
$('#games_no').click(function() {
    $("#id_checked_games").hide();

});

$('#tech_yes').click(function() {

    $("#id_checked_tech").show();
});
$('#tech_no').click(function() {
    $("#id_checked_tech").hide();

});
$('#deco_yes').click(function() {

    $("#id_checked_deco").show();
});
$('#deco_no').click(function() {
    $("#id_checked_deco").hide();

});
//$('#quirky_yes').click(function() {

//    $("#id_checked_quirky").show();
//});
//$('#quirky_no').click(function() {
//    $("#id_checked_quirky").hide();

//});
$('#health_yes').click(function() {

    $("#id_checked_health").show();
});
$('#health_no').click(function() {
    $("#id_checked_health").hide();

});
//$('#giftcard_yes').click(function() {
//    $("#id_checked_giftcard").show();
//});
//$('#giftcard_no').click(function() {
//    $("#id_checked_giftcard").hide();
//});