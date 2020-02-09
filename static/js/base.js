$('nav').addClass('navbar  navbar-expand-lg navbar-light bg-light');
$('nav a').addClass('nav-link');
$('nav a').wrap('<li class="nav-item"></li>');
$('nav li').wrapAll('<ul class="navbar-nav mr-auto"></ul>');
$('nav ul').wrapAll('<div class="collapse navbar-collapse" id="navbarSupportedContent"></div>');
$('nav').prepend('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"></button>');
$('nav button').prepend('<svg class="bi bi-list" width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.5 13.5A.5.5 0 015 13h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5zm0-4A.5.5 0 015 9h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5zm0-4A.5.5 0 015 5h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5z" clip-rule="evenodd"></path></svg>');
console.log(window.location.pathname);
$(`nav ul > li:has(a[href="${window.location.pathname}"])`).addClass('active');
$('input').each(
    function() {
        var $element = $(this);
        switch (this.type) {
            case 'text':
            case 'password':
            case 'number':
                $element.addClass('form-control');
            break;
            default:
            break;
        }
    }
);

$('tr:has(input)').addClass('form-group');
$('.helptext').addClass('form-text text-muted');
$('td:has(> .errorlist)').filter('td:has(> input)').each(function(){
    var $this = $(this);
    $(this).children('.form-control').addClass('is-invalid');
    var $errorlist = $this.children('.errorlist');
    $this.append($errorlist);
    $this.addClass('invalid-feedback');
});
$('td:has(> .errorlist)').filter('td:not(> input)').each(function(){
    $(this).addClass('text-danger');
});
$('button[type="submit"]').addClass('btn btn-primary pull-right');
