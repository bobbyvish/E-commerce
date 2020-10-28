
var updatebtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updatebtns.length; i++){
  updatebtns[i].addEventListener('click', function () {
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log(productId, action)
    console.log(user)
    if (user) {
      updateUserOrder(productId,action)

    } else {

      location.href="/login"
    }
  })
}

function updateUserOrder(productId, action) {
  console.log('user log send dta')
  var url = '/update_item/'
  fetch(url, {
    method:'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'productId':productId,'action':action})
  })
    .then((response) => {
      return response.json()
    })
    .then((data) => {
      console.log('data:', data)
      location.reload()
  })
}