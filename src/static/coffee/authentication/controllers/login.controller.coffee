(() ->
    LoginController = ($scope, $location, Authentication) ->
        'ngInject'
        vm = this

        login = () ->
            Authentication.login vm.email, vm.password

        activate = () ->
            if Authentication.isAuthenticated()
                $location.url('/')
            return

        vm.login = login
        activate()

        return

    angular
    .module 'app.authentication.controllers'
    .controller 'LoginController', LoginController
)()
