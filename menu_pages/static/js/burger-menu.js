// document.querySelector('.burger-menu').addEventListener('click', function () {
//     this.classList.toggle('active');
//     document.querySelector('.navigation').classList.toggle('open');
//
// })

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("burger").addEventListener("click", function () {
        document.querySelector(".navigation").classList.toggle("open");
    });
});
