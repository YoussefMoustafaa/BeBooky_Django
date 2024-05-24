document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.cta-explore').addEventListener('click', function(event) {
        event.preventDefault();
        const title = document.getElementById('search-input').value;
        if (title) {
          window.location.href = `{% url 'search_books' %}?search=${encodeURIComponent(title)}`;
        } else {
            alert('Please enter a title to search.');
        }
    });
});