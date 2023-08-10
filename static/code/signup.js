document.addEventListener('DOMContentLoaded', function() {
    const phone = document.querySelector('.phone-number input');
    const cpf = document.querySelector('.cpf input');
  
    phone.addEventListener('input', formatPhoneNumber);
    cpf.addEventListener('input', formatCPF);
  
    function formatPhoneNumber() {
      let digit = phone.value.replace(/\D/g, '');
      digit = digit.replace(/^(\d{2})(\d{2})(\d{5})(\d{4})$/, '+$1 ($2) $3.$4');
      phone.value = digit;
    }
  
    function formatCPF() {
      let digit = cpf.value.replace(/\D/g, '');
      digit = digit.replace(/(\d{3})(\d)/, '$1.$2');
      digit = digit.replace(/(\d{3})(\d)/, '$1.$2');
      digit = digit.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
      cpf.value = digit;
    }
  });
  
//   Regex code for auto formatting
