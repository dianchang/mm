var $mainWap = $('#main-wap');

// 跳转到channel
$mainWap.on('click', '.channel', function (e) {
    var href = $(this).data('href');

    if (e.target.tagName !== 'A' && $(e.target).parents('a').length === 0) {
        window.location = href;
    }
});
