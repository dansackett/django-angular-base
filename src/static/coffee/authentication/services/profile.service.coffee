(() ->
    Profile = ($http) ->
        'ngInject'

        #######################################################################
        ## Destroy Profile
        #######################################################################
        destroy = (profile) ->
            $http.delete "/api/v1/accounts/#{profile.id}/"

        #######################################################################
        ## Get profile
        #######################################################################
        get = (username) ->
            $http.get "/api/v1/accounts/#{username}/"

        #######################################################################
        ## Update profile
        #######################################################################
        update = (profile) ->
            $http.put "/api/v1/accounts/#{profile.username}/", profile

        #######################################################################
        ## Master keys
        #######################################################################
        destroy: destroy
        get: get
        update: update

    angular
    .module 'app.authentication.services'
    .factory 'Profile', Profile
)()
