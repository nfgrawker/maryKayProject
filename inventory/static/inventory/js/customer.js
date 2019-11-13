window.onload = function () {
    let selectDropDown = $('#selectCustomer');
    selectDropDown.change(function () {
        if (selectDropDown.val() == "new"){
            $('.btn-info').text("Submit")
        }
        else{
            $('.btn-info').text("Change")

        }
    })
};