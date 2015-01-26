(() ->
    Authentication = ($http, $cookies) ->
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
        loginError = () ->
            console.error 'Epic failure!'
            return

        loginSuccess = (data, status, headers, config) ->
            setAuthenticatedAccount data.data
            window.location = '/'
            return

        login = (email, password) ->
            $http.post('/api/v1/auth/login/', {
                email: email,
                password: password
            }).then loginSuccess, loginError

        #######################################################################
        ## Logout
        #######################################################################
        logoutError = () ->
            console.error 'Epic failure!'
            return

        logoutSuccess = (data, status, headers, config) ->
            unauthenticate()
            window.location = '/'
            return

        logout = () ->
            $http.post('/api/v1/auth/logout/').then logoutSuccess, logoutError

        #######################################################################
        ## Register
        #######################################################################
        registerError = () ->
            console.error 'Epic failure!'
            return

        registerSuccess = (data, status, headers, config) ->
            Authentication.login email, password
            return

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
