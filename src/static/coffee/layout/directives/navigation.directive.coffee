(() ->
    navigation = (Authentication) ->
        'ngInject'
        templateUrl: '/static/templates/layout/navigation.html'
        replace: false
        transclude: false
        restrict: 'E'
        scope: {}
        link: (scope, elem, attrs) ->
            logout = () ->
                Authentication.logout()

            scope.logout = logout
            scope.authenticated = Authentication.isAuthenticated()
            scope.authenticated_user = Authentication.getAuthenticatedAccount()

            return

    angular
    .module 'app.layout.directives'
    .directive 'navigation', navigation
)()
