window.onload = function () {
    $("#postProduct").click(function () {
        parent = $("#postProduct").parent().parent();
        let allListElements = $("input");
        let inputs = $(parent).find(allListElements);
        let objectToSend = {};
         let arrayForInput = [""];
        inputs.each(function () {
            if ($(this).attr("id") == undefined) {
                console.log("skipping token")
            } else {
                objectToSend[$(this).attr("id")] = $(this).val()
                arrayForInput.push($(this).val())
            }
        });
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
            if(response['status'] == 1){
                let newRow = $("<tr>")
                arrayForInput.forEach(function(val,idx){
                    let tableData = $("<td>")
                    tableData.append(val)
                    newRow.append(tableData)
                });
                $(".mainInventoryTable").append(newRow)
            }
        });
        console.log(objectToSend)
    })
};