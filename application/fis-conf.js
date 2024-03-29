fis.config.set('project.include', ['templates/**', 'static/**']);
fis.config.set('project.exclude', ['static/**.less']);
fis.config.set('modules.postpackager', 'simple');
fis.config.set('pack', {
    'pkg/libs.js': [
        "/static/js/libs/respond.min.js",
        "/static/js/libs/jquery.min.js",
        "/static/js/libs/bootstrap.min.js",
        "/static/js/libs/module.js",
        "/static/js/libs/hotkeys.js",
        "/static/js/libs/uploader.js",
        "/static/js/libs/simditor.js",
        "/static/js/libs/marked.min.js",
        "/static/js/libs/to-markdown.js",
        "/static/js/libs/simditor-markdown.js",
        "/static/js/libs/highlight.pack.js",
        "/static/js/init.js"
    ],
    'pkg/libs.css': [
        'static/css/libs/*.css'
    ],
    'pkg/layout.css': [
        'static/css/bootstrap.theme.css',
        'static/css/common.css',
        'static/css/macros/*.css',
        'static/css/layout.css'
    ]
});
