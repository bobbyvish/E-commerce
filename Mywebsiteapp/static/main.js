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

$(document).ready(function () {
  var total = $('.total-price')
  // console.log("total price is :" + total);
  console.log("total" + total);
  var subtotal = 0
  for (var i = 0; i < total.length; i++) {
    subtotal = subtotal + parseInt(total[i].innerHTML);

    console.log(total[i].innerHTML);
  }
  document.getElementById('subtotal').innerHTML = subtotal + " Rs";
  document.getElementById('shipping').innerHTML = 50 + " Rs";
  document.getElementById('total').innerHTML = subtotal + 50 + " Rs";

})
//  function for quantityChanged
$('.quantity-input').on('change', function () {
  var quantityInput = document.getElementsByClassName("quantity-input");
  // alert("changed")

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
  var id = this.id.slice(8, );
  document.getElementById('price' + id).innerHTML = document.getElementById('unit-price' + id).innerHTML * this.value + " Rs";
  var total = $('.total-price')

  console.log("total" + total);
  var subtotal = 0
  for (var i = 0; i < total.length; i++) {
    subtotal = subtotal + parseInt(total[i].innerHTML);

    console.log(total[i].innerHTML);
  }
  document.getElementById('subtotal').innerHTML = subtotal + " Rs";
  document.getElementById('shipping').innerHTML = 50 + " Rs";
  document.getElementById('total').innerHTML = subtotal + 50 + " Rs";


}