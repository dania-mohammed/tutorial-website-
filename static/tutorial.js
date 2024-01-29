// function to calculate age
function calculateAge() {
    const dobInput = document.getElementById("dob");
    const dob = new Date(dobInput.value);
    const now = new Date();
  
    const ageInSeconds = Math.floor((now - dob) / 1000);
  
    const resultElement = document.getElementById("result");
    resultElement.textContent = `Your age in seconds is: ${ageInSeconds}`;
  }
  
  function saveInput() {
    const userInput = document.getElementById('userInput').value;
    localStorage.setItem('userInput', userInput);
    displayInput();
}

function displayInput() {
    const savedInput = localStorage.getItem('userInput');
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = savedInput;
}

// Call displayInput() on page load to show any previously saved input
displayInput();
