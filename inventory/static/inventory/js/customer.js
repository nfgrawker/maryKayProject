window.onload = function () {
    let selectDropDown = $('#selectCustomer');
    selectDropDown.change(function () {
        if (selectDropDown.val() == "new") {
            $('.button').text("Submit")
        } else {
            $('.button').text("Change");
        }

    });
    $('.button').click(function () {
        jsonObjectToSend = {};
        $("input").each(function (index) {
            jsonObjectToSend[$(this).attr("name")] = $(this).val();
        });
        let csrftoken = $("[name=csrfmiddlewaretoken]").val();
        console.log(jsonObjectToSend)
    })
};