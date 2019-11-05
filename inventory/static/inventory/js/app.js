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
                objectToSend[$(this).attr("id")] = $(this).val();
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
            console.log(response);
            if(response['status'] == 1){
                console.log("adding")
                let newRow = $("<tr>");
                arrayForInput.forEach(function(val,idx){
                    let tableData = $("<td>");
                    tableData.append(val);
                    newRow.append(tableData)
                    console.log("appending")
                    console.log(tableData)
                });
                $(".mainInventoryTable").prepend(newRow)
            }
        });
        console.log(objectToSend)
    });
    $("#changeProduct").click(function(){
        parent = $("#postProduct").parent().parent();
        url = "/changeProduct";
        let allListElements = $("input");
        let inputs = $(parent).find(allListElements);
        inputs.each(function () {
            if ($(this).attr("id") == undefined) {
                console.log("skipping token")
            } else {
                objectToSend[$(this).attr("td")] = $(this).val()
            }

        });
            keyList = Object.keys(objectToSend);
            paramsList = [];
        keyList.forEach(function(val,idx){
            if (idx == 0){
                url += "?"+val+"="+objectToSend[val]
            }
            else{
                url += "&"+val+"="+objectToSend[val]
            }
        });
        $.get(url,function(response){
            console.log(response)
        })
    })
};