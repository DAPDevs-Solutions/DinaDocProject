document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll('.menu_list--list_items .item a');
    const liHref = window.location.pathname.replace(/\/$/, '');
    const cleanLiHref = liHref.replace(/^\/[a-z]{2}(\/|$)/, '/');

    function updateSelectedItem(clickedItem) {
        items.forEach(item => {
            const itemHref = item.getAttribute('href');
            const isCurrentPage = itemHref === cleanLiHref
            if (isCurrentPage) {
                item.style.color = '#794A83';
                item.style.textDecoration = 'underline'
            }
        });
    }

    updateSelectedItem(liHref);
});

