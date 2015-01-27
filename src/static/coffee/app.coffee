(() ->
    # Add all large modules here
    angular.module 'app', [
        'app.config',
        'app.routes',
        'app.layout',
        'app.authentication',
        'app.utils',
    ]

    # Global app module declarations here
    angular.module 'app.routes', ['ui.router']
    angular.module 'app.config', ['ui.bootstrap', 'ngCookies']

    run = ($http) ->
        'ngInject'
        $http.defaults.xsrfHeaderName = 'X-CSRFToken'
        $http.defaults.xsrfCookieName = 'csrftoken'
        return

    angular.module('app').run(run)
)()
