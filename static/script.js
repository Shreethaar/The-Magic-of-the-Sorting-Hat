document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const jsonData = {};
    formData.forEach((value, key) => jsonData[key] = value);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        let output = `
            <h2>Prediction Result</h2>
            <p><strong>Hometown:</strong> ${jsonData.hometown}</p>
            <p><strong>GPA:</strong> ${jsonData.gpa}</p>
            <p><strong>Co-curriculum Activities:</strong> ${jsonData.activities}</p>
            <p><strong>Inasis:</strong> ${jsonData.inasis}</p>
            <p><strong>Household Income:</strong> ${jsonData.income}</p>
            <p><strong>Hobbies:</strong> ${jsonData.hobbies}</p>
            <p><strong>Number of Friends:</strong> ${jsonData.friends}</p>
            <p><strong>Leadership:</strong> ${jsonData.leadership}</p>
            <p><strong>Prediction:</strong> ${data.prediction}</p>
        `;
        document.getElementById('output').innerHTML = output;
        document.getElementById('output').style.display = 'block';
        document.getElementById('outputLabel').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});

