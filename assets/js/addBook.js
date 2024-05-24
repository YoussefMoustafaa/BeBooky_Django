document.getElementById('upImg').addEventListener('change', function() {
    var file = this.files[0];
    var formData = new FormData();
    formData.append('upImg', file);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "upload_image" %}', true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.url) {
                document.getElementById('img').src = response.url;
            } else {
                console.error('Failed to load image:', response.error);
            }
        }
    };
    xhr.send(formData);
});