# Django-Angular-Base

This provides a good base for a standalone Django application using AngularJS
as the driving application force. It provides a server configuration, log
collection, and uses an internal Django-Rest-Framework API which is consumed
in AngularJS. An authentication system and custom user model is provided which
can be extended for personal use.

## Compiling Frontend and Static Files

When working with this project, we will want to place all working files within
the `src/static` directory. Here we can write our CoffeeScript and our SCSS
files as well as create the templates for AngularJS portions of the app. Our
third-party apps are sent here as well.

When you want to build the static files and compile the CoffeeScript and SCSS
files we use fabric to do so:

    $ fab compile

This command will collect all static files from `src/static` and send them to
`var/www/static`. Once there, Gulp will compile the CoffeeScript, compile the
SCSS, collect and minify the third-party files, and remove the .coffee and
.scss files from distribution. This will give you an up to date view of the
frontend application.
