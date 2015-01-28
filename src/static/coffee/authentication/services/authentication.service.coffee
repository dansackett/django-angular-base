(() ->
    Authentication = ($http, $cookies, Message) ->
        'ngInject'

        #######################################################################
        ## Utils
        #######################################################################
        getAuthenticatedAccount = () ->
            if not $cookies.authenticatedAccount
                return
            JSON.parse $cookies.authenticatedAccount

        isAuthenticated = () ->
            if $cookies.authenticatedAccount then true else false

        setAuthenticatedAccount = (account) ->
            $cookies.authenticatedAccount = JSON.stringify account

        unauthenticate = () ->
            delete $cookies.authenticatedAccount

        #######################################################################
        ## Login
        #######################################################################
        loginError = (data, status, headers, config) ->
            Message.create 'danger', data.data.message

        loginSuccess = (data, status, headers, config) ->
            setAuthenticatedAccount data.data
            window.location = '/'

        login = (email, password) ->
            $http.post('/api/v1/auth/login/', {
                email: email,
                password: password
            }).then loginSuccess, loginError

        #######################################################################
        ## Logout
        #######################################################################
        logoutError = (data, status, headers, config) ->
            Message.create 'danger', data.data.message

        logoutSuccess = (data, status, headers, config) ->
            unauthenticate()
            window.location = '/'

        logout = () ->
            $http.post('/api/v1/auth/logout/').then logoutSuccess, logoutError

        #######################################################################
        ## Register
        #######################################################################
        registerError = (data, status, headers, config) ->
            Message.create 'danger', data.data.message

        registerSuccess = (data, status, headers, config) ->
            Authentication.login email, password

        register = (email, password, username) ->
            $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            }).then registerSuccess, registerError

        #######################################################################
        ## Master keys
        #######################################################################
        getAuthenticatedAccount: getAuthenticatedAccount
        isAuthenticated: isAuthenticated
        setAuthenticatedAccount: setAuthenticatedAccount
        unauthenticate: unauthenticate
        login: login
        logout: logout
        register: register

    angular
    .module 'app.authentication.services'
    .factory 'Authentication', Authentication
)()
