(() ->
    navigation = () ->
        'ngInject'
        templateUrl: '/static/templates/layout/navigation.html'
        replace: false
        transclude: false
        restrict: 'E'
        scope: {}
        link: (scope, elem, attrs) ->
            return

    angular
    .module 'app.layout.directives'
    .directive 'navigation', navigation
)()
