function showTags(str) {
    document.getElementById("tag_selecter").innerHTML = "";
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {

    if (this.readyState == 4 && this.status == 200) {
    $(".chosen-select").trigger("chosen:updated");
    xmlDoc = this.responseXML;
    tag = "";
    x = xmlDoc.getElementsByTagName("id");
    y = xmlDoc.getElementsByTagName("name");
    Exx = xmlDoc.getElementsByTagName("all_id");
    Exy = xmlDoc.getElementsByTagName("all_name");
    u = xmlDoc.getElementsByTagName('extendedtags');
    for (i = 0; i < Exx.length; i++) {          // for tags in
        alltags = u[0].childNodes[0].nodeValue    // selects the tag
            if(i < x.length){
                id = x[i].childNodes[0].nodeValue
                name = y[i].childNodes[0].nodeValue
            }else{
                name=null;
            }
        all_id = Exx[i].childNodes[0].nodeValue
        all_name = Exy[i].childNodes[0].nodeValue
            if(alltags.includes(name)){ //if it is true
                document.getElementById("tag_selecter").innerHTML += "<option value='" + id + "' selected>" + name + "</option>";
            }else{
                document.getElementById("tag_selecter").innerHTML += "<option value='" + all_id + "'>" + all_name + "</option>";
            }
    }
    $(".chosen-select").trigger("chosen:updated");
  }
    };
    xhttp.open("GET", "http://lon17druz01.pythonanywhere.com/productTags?product_no="+str, true);
  xhttp.send();
}