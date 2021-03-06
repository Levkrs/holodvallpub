"use strict";

let _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
let quantityArr = [];
let priceArr = [];
let $orderTotalQuantityDOM;

// $('.order_total_quantity').html('');
// document.querySelector('.order_total_quantity').innerHTML = '';

let totalForms;
let orderTotalQuantity;
let orderTotalCost;
let $orderForm;


function parseOrderForm() {
    for (let i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        console.log(_quantity);
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantityArr[i] = _quantity;
        priceArr[i] = (_price) ? _price : 0;
    }
}

function orderSummaryUpdate(deltaQuantity) {
    orderTotalQuantity = orderTotalQuantity + deltaQuantity;
    $orderTotalQuantityDOM.html(orderTotalQuantity.toString());
}

function deleteOrderItem(row) {
    let targetName = row[0].querySelector('input[type="number"]').name;
    orderitemNum = parseInt(targetName.replace('orderitems-', '').replace('-quantity', ''));
    deltaQuantity = -quantityArr[orderitemNum];
    orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
}

function updateTotalQuantity() {
    for (let i = 0; i < totalForms; i++) {
        orderTotalQuantity += quantityArr[i];
        orderTotalCost += quantityArr[i] * priceArr[i];
    }
    $orderTotalQuantityDOM.html(orderTotalQuantity.toString());
    $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
}

window.onload = function () {
    $orderTotalQuantityDOM = $('.order_total_quantity');
    totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    orderTotalQuantity = parseInt($orderTotalQuantityDOM.text()) || 0;
    orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    $orderForm = $('.order_form');

    parseOrderForm();

    if (!orderTotalQuantity) {
        updateTotalQuantity();
    }

    $orderForm.on('change', 'input[type="number"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-quantity', ''));

            orderitemQuantity = parseInt(event.target.value);
            deltaQuantity = orderitemQuantity - quantityArr[orderitemNum];
            quantityArr[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(deltaQuantity);

    });

    $orderForm.on('change', 'input[type="checkbox"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (event.target.checked) {
            deltaQuantity = -quantityArr[orderitemNum];
        } else {
            deltaQuantity = quantityArr[orderitemNum];
        }
        orderSummaryUpdate(deltaQuantity);
    });

    $('.formset_row').formset({
        addText: '???????????????? ??????????????',
        deleteText: '??????????????',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

    // $orderForm.on('change', 'select', function (event) {
    //     let target = event.target;
    //     console.log(target);
    // });

};