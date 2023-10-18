// Wait for the DOM to finish loading
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.querySelector('form');
  
    // Attach a submit event listener to the form
    form.addEventListener('submit', function(event) {
      // Prevent the form from submitting
      event.preventDefault();
  
      // Get the input values
      const destination = document.querySelector('#destination').value;
      const checkin = document.querySelector('#checkin').value;
      const checkout = document.querySelector('#checkout').value;
      const rooms = document.querySelector('#rooms').value;
  
      // TODO: Implement search functionality using the input values
      console.log(destination, checkin, checkout, rooms);
    });
  });
// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.querySelector('form');
  
    // Add an event listener for the form submission
    form.addEventListener('submit', function(event) {
      // Prevent the default form submission behavior
      event.preventDefault();
  
      // Get the check-in date, check-out date, and number of guests from the form
      const checkInDate = document.querySelector('#check-in').value;
      const checkOutDate = document.querySelector('#check-out').value;
      const numGuests = document.querySelector('#guests').value;
  
      // Create an alert with the booking information
      alert(`Thank you for booking your trip to Paris! Check-in date: ${checkInDate}, check-out date: ${checkOutDate}, number of guests: ${numGuests}`);
    });
  });
  
  
        // Planet Highlighting
const planets = document.querySelectorAll('.planet');
planets.forEach((planet) => {
  planet.addEventListener('mouseenter', () => {
    planet.classList.add('highlight');
  });
  planet.addEventListener('mouseleave', () => {
    planet.classList.remove('highlight');
  });
});
