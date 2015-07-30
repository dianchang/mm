var $mainWap = $('#main-wap');

$mainWap.on('click', '.btn-switch-to-simple', function () {
    $mainWap.find('.piece .details').hide();
    $(this).addClass('active').siblings().removeClass('active');
});

$mainWap.on('click', '.btn-switch-to-details', function () {
    $mainWap.find('.piece .details').show();
    $(this).addClass('active').siblings().removeClass('active');
});
