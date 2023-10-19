document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
      event.preventDefault();
      const destination = document.querySelector('#destination').value;
      const checkin = document.querySelector('#checkin').value;
      const checkout = document.querySelector('#checkout').value;
      const rooms = document.querySelector('#rooms').value;
      console.log(destination, checkin, checkout, rooms);
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
      event.preventDefault();
      const checkInDate = document.querySelector('#check-in').value;
      const checkOutDate = document.querySelector('#check-out').value;
      const numGuests = document.querySelector('#guests').value;
      alert(`Thank you for booking your trip to ${destination}! Check-in date: ${checkInDate}, check-out date: ${checkOutDate}, number of guests: ${numGuests}`);
  });
});


