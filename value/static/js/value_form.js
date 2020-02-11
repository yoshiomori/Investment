var id_date = document.querySelector('#id_date');
id_date.pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}$";
id_date.placeholder = '##/##/####';
id_date.oninput = function() {
     this.value = this
     .value
     .replace(/^(\d{2})(\d)$/, '$1/$2')
     .replace(/^(\d{2})\/(\d{2})(\d)$/, '$1/$2/$3')
     .replace(/^(\d{2})(\d{2})(\d{4})$/, '$1/$2/$3');
};

 var id_price = document.querySelector('#id_price');
 id_price.placeholder = '###.##'
 id_price.pattern = '[0-9]+.?[0-9]*'
