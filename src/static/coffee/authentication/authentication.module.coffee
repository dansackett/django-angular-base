(() ->
    angular.module 'app.authentication', [
      'app.authentication.services',
      'app.authentication.controllers'
    ]

    angular.module 'app.authentication.services', []
    angular.module 'app.authentication.controllers', []
)()
