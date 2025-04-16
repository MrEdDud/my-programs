function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

const accordionHeaders = document.querySelectorAll('.accordion-header');

accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
        const content = header.nextElementSibling;
        content.classList.toggle('active');
    });
});