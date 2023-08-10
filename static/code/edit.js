document.addEventListener('DOMContentLoaded', function() {
    const phone = document.querySelector('.phone-number input');
  
    phone.addEventListener('input', formatPhoneNumber);
  
    function formatPhoneNumber() {
      let digit = phone.value.replace(/\D/g, '');
      digit = digit.replace(/^(\d{2})(\d{2})(\d{5})(\d{4})$/, '+$1 ($2) $3.$4');
      phone.value = digit;
    }
  });

//   Regex code for auto formatting
  