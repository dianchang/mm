var $mainWap = $('#main-wap');

// 跳转频道
$mainWap.on('click', '.channel', function (e) {
    var href = $(this).data('href');

    window.location = href;
});
