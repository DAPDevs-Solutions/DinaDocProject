const curLang = document.getElementById('lang_blockID')
const languagesChanger = document.getElementById('dropdown__langmenu')
const arrow = document.getElementById('lang-arrow')
let isLangBlockVisible = false
if (arrow != null) {
    curLang.addEventListener("click", () => {
        arrow.classList.toggle('rotate')
        if (isLangBlockVisible) {
            languagesChanger.classList.remove('show')
        } else {
            languagesChanger.classList.add('show')
        }
        isLangBlockVisible = !isLangBlockVisible;
    })
}


