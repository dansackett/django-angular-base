(() ->
    message = ($rootScope) ->
        'ngInject'
        templateUrl: '/static/templates/utils/message.html'
        replace: false
        transclude: false
        restrict: 'A'
        scope: {}
        link: (scope, elem, attrs) ->
            scope.show = false

            $rootScope.$on 'messageCreated', (event, args) ->
                scope.show = true
                scope.type = args.type
                scope.message = args.message

            scope.close = () ->
                scope.show = false

            return

    angular
    .module 'app.utils.directives'
    .directive 'message', message
)()
