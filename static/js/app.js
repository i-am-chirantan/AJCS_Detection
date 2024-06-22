document.getElementById('detectButton').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('file', file);

        fetch('/detect/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            var output = '';
            switch (data.result) {
                case 0:
                    output = 'Person has COVID-19 disease';
                    break;
                case 1:
                    output = 'No lung disease detected';
                    break;
                case 2:
                    output = 'Person has Tuberculosis';
                    break;
                case 3:
                    output = 'Person has Pneumonia';
                    break;
                default:
                    output = 'Unknown result';
            }
            document.getElementById('output').innerText = output;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please select a file first.');
    }
});
