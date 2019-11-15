window.onload = function () {
    let selectDropDown = $('#selectCustomer');
    selectDropDown.change(function () {
        if (selectDropDown.val() == "new") {
            $('.button').text("Submit");
            window.type = 'Submit'
        } else {
            $('.button').text("Change");
            attributesInSelectedObject = {};
            window.type = "Change";
            let id = $(this).children(":selected");
            console.log(id);
            id[0].attributes.forEach(element=>{
               attributesInSelectedObject[element.nodeName] = element.nodeValue
            });
            console.log(attributesInSelectedObject)

        }

    });
    $('.button').click(function () {
        jsonObjectToSend = {};
        $("input").each(function (index) {
            if ($(this).attr("name") != "csrfmiddlewaretoken") {
                jsonObjectToSend[$(this).attr("name")] = $(this).val();
            }
        });
        let csrftoken = $("[name=csrfmiddlewaretoken]").val();
        console.log(jsonObjectToSend);
        jsonObjectToSend["type"] = window.type;
        $.ajax({
            type: "POST",
            url: "/inventoryHome/submitCustomer/",
            data: JSON.stringify(jsonObjectToSend),
            contentType: "application/json",
            headers: {
                "X-CSRFToken": csrftoken
            },
            dataType: "json"
        }).then(response => {
            if (response['status'] == 1) {
                window.reload()
            }
        })
    })
};