// var removeCartItemButton = document.getElementsByClassName('devare-cart')
// for (var i = 0; i < removeCartItemButton.length; i++) {
//   var button = removeCartItemButton[i]
//   button.addEventListener('click', removecartitem)
// }

// var quantityInput = document.getElementsByClassName("quantity-input");
// for (i = 0; i < quantityInput.length; i++) {
//   var input = quantityInput[i]
//   input.addEventListener('change', quantityChanged);
// }

// function removecartitem(event) {
//   var buttonClicked = event.target;
//   buttonClicked.parentElement.parentElement.remove()
//   updateCartTotal()
// }

// function quantityChanged(event) {
//   var input = event.target
//   if (isNaN(input.value) || input.value <= 0) {
//     input.value = 1;
//   }
//   updateCartTotal()
// }

// function updateCartTotal() {
//   var cartItemContainer = document.querySelector('.click-cart');
//   var cartRows = cartItemContainer.querySelectorAll('.cart-details');
//   var total = 0
//   for (var i = 0; i < cartRows.length; i++) {
//     var cartRow = cartRows[i]
//     var priceElement = cartRow.querySelector('.cart-price');
//     var quantityElement = cartRow.querySelector('.quantity-input');
//     var price = parseFloat(priceElement.innerText)
//     var quantity = quantityElement.value
//     total = total + (price * quantity)

//   }
//   total = Math.round(total * 100) / 100
//   document.querySelector('.cart-total-price').innerText = total;
// }

$(".delete-cart").click(function () {
  var id = $(this).attr("id");
  // alert(id);
  $.ajax({

    URL: "cart",
    data: "id=" + id,


    success: function (data) {
      // console.log(deleted);
      alert(data);
      window.location.reload();

    }


  })
})

// $(document).ready(function () {
//   $("#quantity").on('input', function () {
//     var item_total = 0;
//     var quantity = $("#quantity").val();
//     // console.log(quantity)
//     var item_price = document.getElementById("cart-item-price").innerText;
//     var item_price_remove_rs = item_price.split("Rs").join("");
//     // console.log(remove_rs);
//     item_total = quantity * item_price_remove_rs;
//     // alert(item_total);
//     document.getElementById("item-price").innerText = item_total + " Rs";
//   })
// })

$('#quantity').on('change', function () {
  var quantityInput = document.getElementsByClassName("quantity-input");
  for (i = 0; i < quantityInput.length; i++) {
    let input = quantityInput[i];
    input.addEventListener('change', quantityChanged);
  }
})

function quantityChanged(event) {
  var input = event.target
  if (isNaN(input.value) || input.value <= 0) {
    input.value = 1;
  }
  updateCartTotal()
}

function updateCartTotal() {
  var cartItemContainer = document.getElementsByClassName('click-cart')
  var cartRows = cartItemContainer.getElementsByClassName('cart-details');
  var item_total = 0;
  var total = 0;
  for (var i = 0; i < cartRows.length; i++) {
    var cartRow = cartRows[i];
    var item_price = cartRow.getElementsByClassName("cart-price")

    // var item_price_remove_rs = item_price.innerText.replace('Rs', '');
    alert(item_price_remove_rs);
    var quantityElement = cartRow.getElementsByClassName('quantity-input')
    var quantity = quantityElement.value
    console.log(quantity);
    item_total = quantity * item_price;
    alert(item_total);
    cartRow.getElementsByClassName("item-price").innerText = item_total;
    var priceElement = cartRow.querySelector('#item-price')



    total = total + item_total;

  }
  total = Math.round(total * 100) / 100
  document.querySelector('.cart-total-price').innerText = total;
}