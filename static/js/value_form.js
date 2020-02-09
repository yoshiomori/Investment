var id_date = document.querySelector('#id_date');
id_date.pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}$";
id_date.placeholder = '##/##/####';
id_date.oninput = function() {
     this.value = this
        .value
        .replace(
            /^[^\d]*$/g,
            ''
        )
        .replace(
            /^[^\d]*(\d)[^\d]*$/g,
            '$1'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d\/]$/g,
            '$1$2'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*$/g,
            '$1$2/$3'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d\/]*$/g,
            '$1$2/$3$4'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*$/g,
            '$1$2/$3$4/$5$6'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*$/g,
            '$1$2/$3$4/$5$6$7'
        )
        .replace(
            /^[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d)[^\d]*(\d).*$/g,
            '$1$2/$3$4/$5$6$7$8'
        );
 };

 var id_price = document.querySelector('#id_price');
 id_price.placeholder = '###.##'
 id_price.pattern = '[0-9]+.?[0-9]*'
