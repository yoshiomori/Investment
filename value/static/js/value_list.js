var id_date__gte = document.querySelector('#id_date__gte');
id_date__gte.pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}$";
id_date__gte.placeholder = '##/##/####';
id_date__gte.oninput = function() {
     this.value = this
     .value
     .replace(/^(\d{2})(\d)$/, '$1/$2')
     .replace(/^(\d{2})\/(\d{2})(\d)$/, '$1/$2/$3')
     .replace(/^(\d{2})(\d{2})(\d{4})$/, '$1/$2/$3');
};
var id_date__lte = document.querySelector('#id_date__lte');
id_date__lte.pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}$";
id_date__lte.placeholder = '##/##/####';
id_date__lte.oninput = function() {
     this.value = this
     .value
     .replace(/^(\d{2})(\d)$/, '$1/$2')
     .replace(/^(\d{2})\/(\d{2})(\d)$/, '$1/$2/$3')
     .replace(/^(\d{2})(\d{2})(\d{4})$/, '$1/$2/$3');
};