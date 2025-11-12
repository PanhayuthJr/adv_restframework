// Basic alert for add to cart/wishlist (expand as needed)
document.querySelectorAll('.btn-primary, .btn-secondary').forEach(button => {
    button.addEventListener('click', () => {
        alert('Item added!');
    });
});