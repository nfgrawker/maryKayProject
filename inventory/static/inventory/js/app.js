window.onload = function () {
    $("#postProduct").click(function () {
        parent = $("#postProduct").parent().parent();
        let allListElements = $("input");
        let inputs = $(parent).find(allListElements);
        let objectToSend = {};
        let arrayForInput = [];
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
            if (response['status'] == 1) {
                console.log("adding");
                let newRow = $("<tr>");
                console.log("Array for input");
                console.log(arrayForInput);
                arrayForInput.forEach(function (val, idx) {
                    let tableData = $("<td>");
                    console.log(val);
                    tableData.text(val);
                    newRow.append(tableData);
                    console.log("appending");
                });
                $(".mainInventoryTable").append(newRow)
            }
        });
        console.log(objectToSend)
    });
    $("#typeSelector").change(function () {
        let price = $("input#priceSoldFor");
        let quantity = $("input#productQuantity");
        switch ($(this).val()) {
            case "sellStock":
                price.attr("placeholder", "Price Sold For");
                quantity.attr("placeholder", "Quantity Sold");
                break;
            case "addStock":
                price.attr("placeholder","Whole Sale Price");
                quantity.attr("placeholder","Quantity Purchased");
                // code block
                break;
            default:
            // code block
        }
    })
    $("#addToOrder").click(function(){
        let priceSold = $("#priceSoldFor").val()
        let productQuantity = $("#productQuantity").val()
        let productName =  $("#productName").children("option:selected").val()
        let productId =  $("#productName").children("option:selected").attr("id")

    })
};