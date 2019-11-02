window.onload = function () {
    $("#postProduct").click(function () {
        parent = $("#postProduct").parent().parent();
        let allListElements = $("input");
        let inputs = $(parent).find(allListElements);
        let objectToSend = {};
        inputs.each(function () {
            if ($(this).attr("id") == undefined) {
                console.log("skipping token")
            } else {
                objectToSend[$(this).attr("id")] = $(this).val()
            }
        });
        const sleep = (milliseconds) => {
            return new Promise(resolve => setTimeout(resolve, milliseconds))
        }
        let successMessage = function (response) {
            console.log(response)
            location.reload()
        };
        let csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: "addInventory/",
            data: JSON.stringify(objectToSend),
            contentType: "application/json",
            headers: {
                "X-CSRFToken": csrftoken
            },
            dataType: "json"
        }).then(response => {
            console.log(response)
        });
        console.log(objectToSend)
        location.reload()
    })
};