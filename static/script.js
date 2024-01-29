// function to calculate age
function calculateAge() {
    const dobInput = document.getElementById("dob");
    const dob = new Date(dobInput.value);
    const now = new Date();
  
    const ageInSeconds = Math.floor((now - dob) / 1000);
  
    const resultElement = document.getElementById("result");
    resultElement.textContent = `Your age in seconds is: ${ageInSeconds}`;
  }
  

