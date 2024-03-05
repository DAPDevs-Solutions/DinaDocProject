// document.querySelector('.burger-menu').addEventListener('click', function () {
//     this.classList.toggle('active');
//     document.querySelector('.navigation').classList.toggle('open');
//
// })

document.querySelector('.burger-menu').addEventListener('click', function() {
  document.querySelector('.navigation').classList.toggle('active');
  document.querySelector('.burger-menu').classList.toggle('active');
});

// document.addEventListener("DOMContentLoaded", function() {
//     document.getElementById("burger").addEventListener("click", function() {
//         document.querySelector(".user_nav--menu").classList.toggle("open")
//     })
// })
