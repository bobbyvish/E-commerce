let removeCartItemButton = document.getElementsByClassName('delete-cart')
for (let i = 0; i < removeCartItemButton.length; i++) {
  let button = removeCartItemButton[i]
  button.addEventListener('click', removecartitem)
}

let quantityInput = document.getElementsByClassName("quantity-input");
for (i = 0; i < quantityInput.length; i++) {
  let input = quantityInput[i]
  input.addEventListener('change', quantityChanged);
}

function removecartitem(event) {
  let buttonClicked = event.target;
  buttonClicked.parentElement.parentElement.remove()
  updateCartTotal()
}

function quantityChanged(event) {
  let input = event.target
  if (isNaN(input.value) || input.value <= 0) {
    input.value = 1;
  }
  updateCartTotal()
}

function updateCartTotal() {
  let cartItemContainer = document.querySelector('.click-cart');
  let cartRows = cartItemContainer.querySelectorAll('.cart-details');
  let total = 0
  for (let i = 0; i < cartRows.length; i++) {
    let cartRow = cartRows[i]
    let priceElement = cartRow.querySelector('.cart-price');
    let quantityElement = cartRow.querySelector('.quantity-input');
    let price = parseFloat(priceElement.innerText)
    let quantity = quantityElement.value
    total = total + (price * quantity)

  }
  total = Math.round(total * 100) / 100
  document.querySelector('.cart-total-price').innerText = total;
}