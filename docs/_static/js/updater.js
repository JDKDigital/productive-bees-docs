$(document).ready(function () {

    console.log('ready');

    $('p.caption ~ ul').addClass('menu-list');

    var pList = $('p.caption');
    pList.addClass('menu-label');
    pList.removeClass('caption');
});