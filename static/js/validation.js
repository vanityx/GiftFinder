
// Questionnaire validation
    function validateFULLQ() {

        var gender = document.getElementById("gender");
        if(gender.value == "") {
            document.getElementById("gendermsg").style.display=""
                document.querySelector('#gendermsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("gendermsg").style.display="none";
        }
        var age = document.getElementById("age");
        if(age.value == "") {
            document.getElementById("agemsg").style.display="";
                document.querySelector('#agemsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("agemsg").style.display="none";
        }
        var priceRange = document.getElementById("priceRange");
        if(priceRange.value == "") {
            document.getElementById("pricemsg").style.display=""
                document.querySelector('#pricemsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("pricemsg").style.display="none";
        }
        var specEvent = document.getElementById("specEvent");
        if(specEvent.value == "") {
            document.getElementById("eventmsg").style.display=""
                document.querySelector('#eventmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("eventmsg").style.display="none";
        }
        var clothing = document.getElementById("clothing");
        var clothing_no = document.getElementById("clothing_no");
        if(clothing.value == "" && clothing_no.checked == false) {
            document.getElementById("clothingmsg").style.display=""
                document.querySelector('#clothingmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("clothingmsg").style.display="none";
        }
        var makeup = document.getElementById("makeup");
        var makeup_no = document.getElementById("makeup_no");
        if(makeup.value == "" && makeup_no.checked == false) {
            document.getElementById("makeupmsg").style.display=""
                document.querySelector('#makeupmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("makeupmsg").style.display="none";
        }
        var skincare = document.getElementById("skincare");
        var skincare_no = document.getElementById("skincare_no");
        if(skincare.value == "" && skincare_no.checked == false) {
            document.getElementById("skincaremsg").style.display=""
                document.querySelector('#skincaremsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("skincaremsg").style.display="none";
        }
        var jewelry = document.getElementById("jewelry");
        var jewelry_no = document.getElementById("jewelry_no");
        if(jewelry.value == "" && jewelry_no.checked == false) {
            document.getElementById("jewelrymsg").style.display=""
                document.querySelector('#jewelrymsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("jewelrymsg").style.display="none";
        }
        var reading = document.getElementById("reading");
        var reading_no = document.getElementById("reading_no");
        if(reading.value == "" && reading_no.checked == false) {
            document.getElementById("readingmsg").style.display=""
                document.querySelector('#readingmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("readingmsg").style.display="none";
        }
        var games = document.getElementById("games");
        var games_no = document.getElementById("games_no");
        if(games.value == "" && games_no.checked == false) {
            document.getElementById("gamesmsg").style.display=""
                document.querySelector('#gamesmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("gamesmsg").style.display="none";
        }
        var tech = document.getElementById("tech");
        var tech_no = document.getElementById("tech_no");
        if(tech.value == "" && tech_no.checked == false) {
            document.getElementById("techmsg").style.display=""
                document.querySelector('#techmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("techmsg").style.display="none";
        }
        var deco = document.getElementById("deco");
        var deco_no = document.getElementById("deco_no");
        if(deco.value == "" && clothing_no.checked == false) {
            document.getElementById("decomsg").style.display=""
                document.querySelector('#decomsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("decomsg").style.display="none";
        }
        var health = document.getElementById("health");
        var health_no = document.getElementById("health_no");
        if(health.value == "" && health_no.checked == false) {
            document.getElementById("healthmsg").style.display=""
                document.querySelector('#healthmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("healthmsg").style.display="none";
        }
        var quirky = document.getElementById("quirky");
        if(quirky.value == "") {
            document.getElementById("quirkymsg").style.display=""
                document.querySelector('#quirkymsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("quirkymsg").style.display="none";
        }
        var giftcard = document.getElementById("giftcard");
        if(giftcard.value == "") {
            document.getElementById("cardmsg").style.display=""
                document.querySelector('#cardmsg').scrollIntoView({
                  behavior: 'smooth'
                });
            return false;
        }else{
            document.getElementById("cardmsg").style.display="none";
        }
        return true
    }
    function validateAddComp() {
        var company_name = document.getElementById("company_name");
        if(company_name.value == "") {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }

    // Database Query Input Validation
    function validateDelComp() {
        var company_no = document.getElementById("company_no");
        if(company_no.checked == false) {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }
    function validateAddProd() {
        var product_name = document.getElementById("product_name");
        var product_desc = document.getElementById("product_desc");
        var product_price = document.getElementById("product_price");
        var product_url = document.getElementById("product_url");
        var product_img = document.getElementById("product_img");
        var company_name = document.getElementById("company_name");

        if(product_name.value == "" || product_desc.value == "" || product_price.value == "" || product_url.value == "" || product_img.value == "" || company_name.value == "") {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }
    function validateAddTag() {
        var tag_name = document.getElementById("tag_name");
        if(tag_name.value == "") {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }
    function validateAmendProd() {
        var product = document.getElementById("product");
        var selectid = document.getElementById("selectid");
        var newValue = document.getElementById("newValue");

        if(product.value == "" || selectid.value == "" || newValue.value == "") {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }
    function validateDelProd() {
        var product = document.getElementById("product");
        if(product.value == "") {
            document.getElementById("msg").style.display=""
            return false;
        }
        return true
    }





















