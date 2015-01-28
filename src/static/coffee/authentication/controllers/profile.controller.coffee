(() ->
    ProfileController = ($location, $stateParams, Authentication, Profile, Message) ->
        'ngInject'
        vm = this
        username = $stateParams.username

        update = () ->
            Profile.update vm.account
            Message.create 'success', 'Profile updated successfully!'

        profileSuccess = (data, status, headers, config) ->
            vm.account = data.data

        profileError = (data, status, headers, config) ->
            $location.url '/'

        activate = () ->
            if not vm.account or vm.account.username != username
                $location.url '/'

            Profile.get(username).then profileSuccess, profileError
            return

        vm.account = Authentication.getAuthenticatedAccount()
        vm.update = update
        activate()

        return

    angular
    .module 'app.authentication.controllers'
    .controller 'ProfileController', ProfileController
)()
