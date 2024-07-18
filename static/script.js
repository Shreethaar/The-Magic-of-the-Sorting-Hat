document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const hometown = document.getElementById('hometown').value;
    const gpa = document.getElementById('gpa').value;
    const activities = document.getElementById('activities').value;
    const inasis = document.getElementById('inasis').value;
    const income = document.getElementById('income').value;
    const hobbies = document.getElementById('hobbies').value;
    const friends = document.getElementById('friends').value;
    const leadership = document.getElementById('leadership').value;
    let output = `
        <h2>Prediction Result</h2>
        <p><strong>Hometown:</strong> ${hometown}</p>
        <p><strong>GPA:</strong> ${gpa}</p>
        <p><strong>Co-curriculum Activities:</strong> ${activities}</p>
        <p><strong>Inasis:</strong> ${inasis}</p>
        <p><strong>Household Income:</strong> ${income}</p>
        <p><strong>Hobbies:</strong> ${hobbies}</p>
        <p><strong>Number of Friends:</strong> ${friends}</p>
        <p><strong>Leadership:</strong> ${leadership}</p>
    `;
    document.getElementById('output').innerHTML = output;
    document.getElementById('output').style.display = 'block';
    document.getElementById('outputLabel').style.display = 'block';
});

