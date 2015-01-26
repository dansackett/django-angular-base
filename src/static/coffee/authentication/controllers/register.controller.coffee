(() ->
    RegisterController = ($scope, $location, Authentication) ->
        'ngInject'
        vm = this

        register = () ->
            Authentication.register vm.email, vm.password, vm.username

        activate = () ->
            if Authentication.isAuthenticated()
                $location.url('/')
            return

        vm.register = register
        activate()

        return

    angular
    .module 'app.authentication.controllers'
    .controller 'RegisterController', RegisterController
)()
