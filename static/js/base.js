var menuBar = $('body > header:nth-child(1) > nav:nth-child(1)');
menuBar.addClass('navbar  navbar-expand-lg navbar-light bg-light');
var menuBarA = menuBar.find('a:not(.dropdown-toggle)');
menuBarA.addClass('nav-link');
menuBarA.wrap('<li class="nav-item"></li>');
menuBar.find('li').wrapAll('<ul class="navbar-nav mr-auto"></ul>');
menuBar.find('ul').wrapAll('<div class="collapse navbar-collapse" id="navbarSupportedContent"></div>');
menuBar.prepend('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"></button>');
menuBar.find('button').prepend('<svg class="bi bi-list" width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.5 13.5A.5.5 0 015 13h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5zm0-4A.5.5 0 015 9h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5zm0-4A.5.5 0 015 5h10a.5.5 0 010 1H5a.5.5 0 01-.5-.5z" clip-rule="evenodd"></path></svg>');
menuBar.find(`ul > li:has(a[href="${window.location.pathname}"])`).addClass('active');
function moveAQueryToDropdownMenu(aQuery, liQuery) {
    aQuery.removeClass('nav-link');
    aQuery.addClass('dropdown-item');
    liQuery.children('.dropdown-menu').append(aQuery);
}
menuBarA.each(
    function() {
        var group = this.classList[0];
        if (group != 'None') {
            var liQuery = $('nav li').filter(
                function () {
                    return $(this).children('a.dropdown-toggle').html() == group;
                }
            );
            if (!liQuery.length) {
                var liQuery = $(`nav li:has(> a.${group})`);
                var firstLiQuery = liQuery.first();
                firstLiQuery.addClass('dropdown');
                firstLiQuery.append(
                    `<a data-toggle="dropdown" class="nav-link dropdown-toggle" href="#">${group}</a>`
                );
                firstLiQuery.append('<div class="dropdown-menu"></div>');
                var aQuery = firstLiQuery.children(`a.${group}`);
                moveAQueryToDropdownMenu(aQuery, firstLiQuery);
            }
            else {
                var aQuery = $(this);
                var parentAQuery = aQuery.parent();
                moveAQueryToDropdownMenu(aQuery, liQuery);
                if (parentAQuery.hasClass('active')) {
                    liQuery.addClass('active');
                }
                parentAQuery.remove();
            }
        }
    }
);

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

$('select').each(
    function() {
        $(this).addClass('form-control');
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
$('td.invalid-feedback').removeClass('invalid-feedback');
$('button[type="submit"]').addClass('btn btn-primary pull-right');

$('main').addClass('container');

$('body > header:nth-child(1) > nav:nth-child(2) > ol:nth-child(1)').addClass('breadcrumb');
$('.breadcrumb > li').addClass('breadcrumb-item');
$('.breadcrumb > li:last-child').addClass('active');
