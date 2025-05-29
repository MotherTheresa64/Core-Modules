// Form submission handler
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registration-form');

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastName').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const agree = document.getElementById('agree').checked;

    if (firstName && lastName && email && password && agree) {
      // Simulate adding to a table
      const table = document.querySelector('table tbody');
      const row = table.insertRow();
      row.insertCell(0).textContent = firstName;
      row.insertCell(1).textContent = lastName;
      row.insertCell(2).textContent = email;

      // Reset form
      form.reset();
    } else {
      alert('Please complete all required fields and agree to the terms.');
    }
  });
});
