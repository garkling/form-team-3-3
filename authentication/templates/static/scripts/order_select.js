
document.addEventListener('DOMContentLoaded', function() {
  const elem = document.querySelectorAll('select');
  const instance = M.FormSelect.init(elem);

  const orderButton = document.getElementById('order-button');
  const orderSelect = document.getElementById('select-period')
  orderButton.addEventListener('click', function () {
    orderButton.style.display = 'none'
    orderSelect.style.display = 'block'
  });
});
