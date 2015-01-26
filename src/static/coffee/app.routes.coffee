(() ->
    routes = ($stateProvider, $urlRouterProvider) ->
        'ngInject'
        $urlRouterProvider.otherwise '/'

        $stateProvider
        .state 'index', {
            url: "/",
            controller: 'IndexController as vm',
            templateUrl: '/static/templates/layout/index.html',
        }
        .state 'register', {
            url: "/register",
            controller: 'RegisterController as vm',
            templateUrl: '/static/templates/authentication/register.html',
        }
        .state 'login', {
            url: "/login",
            controller: 'LoginController as vm',
            templateUrl: '/static/templates/authentication/login.html',
        }

        return

    angular.module('app.routes').config(routes)
)()
