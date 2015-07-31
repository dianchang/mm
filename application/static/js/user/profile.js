//var $mainWap = $('#main-wap');
//
//$mainWap.on('click', '.list-group-channels .channel', function (e) {
//    var id = $(this).data('id');
//
//    if (e.target.tagName !== 'A' && $(e.target).parents('a').length === 0) {
//        window.location = urlFor('channel.view', {uid: id});
//    }
//});

var $mainWap = $('#main-wap');

// 跳转到channel
$mainWap.on('click', '.channel', function (e) {
    var href = $(this).data('href');

    if (e.target.tagName !== 'A' && $(e.target).parents('a').length === 0) {
        window.location = href;
    }
});

