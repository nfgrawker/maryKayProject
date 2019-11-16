window.onload = function () {
    let selectDropDown = $('#selectCustomer');
    selectDropDown.change(function () {
        if (selectDropDown.val() == "new") {
            $('.button').text("Submit");
            window.type = 'Submit'
            $("input").val("")
        } else {
            $('.button').text("Change");
            attributesInSelectedObject = {};
            window.type = "Change";
            let id = $(this).children(":selected");
            console.log(id);
            $.each(id[0].attributes, function (index, attr) {
                attributesInSelectedObject[attr.nodeName] = attr.nodeValue
            });
            for (let [key, value] of Object.entries(attributesInSelectedObject)) {
                obj = $('[name="'+key+'"]')
                obj.val(value)
                console.log(obj.attr('type'))
            }
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