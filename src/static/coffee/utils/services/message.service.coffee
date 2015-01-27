(() ->
    Message = ($rootScope) ->
        'ngInject'
        create = (type, message) ->
            $rootScope.$broadcast 'messageCreated', {
                type: type,
                message: message
            }

        create: create

    angular
    .module 'app.utils.services'
    .factory 'Message', Message
)()
