(function () {
    // Flash message
    setTimeout(showFlash, 200);
    setTimeout(hideFlash, 2000);

    // 代码高亮
    hljs.initHighlightingOnLoad();

    /**
     * Show flash message.
     */
    function showFlash() {
        $('.flash-message').slideDown('fast');
    }

    /**
     * Hide flash message.
     */
    function hideFlash() {
        $('.flash-message').slideUp('fast');
    }
})();
