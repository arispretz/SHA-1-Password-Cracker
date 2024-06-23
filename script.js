window.onload = function() {
    fetch('/results')
        .then(response => response.text())
        .then(data => {
            document.getElementById('results').innerHTML = data;
        })
        .catch(error => {
            document.getElementById('results').innerText = `Error: ${error.message}`;
        });
};
