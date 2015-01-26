from fabric.api import env, run, cd, local, sudo, prefix

env.use_ssh_config = True
env.hosts = [
    # 'webfaction',
]
VENV = 'django-angular-base'


def deploy():
    """Deploy Application"""
    test()
    push()
    pull()
    install_reqs()
    update_db()
    collectstatic()


def test():
    """Run Test Suite"""
    local('py.test')


def push():
    """Push repo remotely"""
    local('git push origin master')


def pull():
    """Pull from remote"""
    with prefix('workon {venv}'.format(venv=VENV)):
        run('git pull origin master')


def install_reqs():
    """Install reqs on server"""
    with prefix('workon {venv}'.format(venv=VENV)):
        run('pip install -r reqs/prod.txt')


def update_db():
    """Update remote database"""
    with prefix('workon {venv}'.format(venv=VENV)):
        run('django-admin.py migrate')


def collectstatic():
    """Collect Static Files"""
    with prefix('workon {venv}'.format(venv=VENV)):
        run('django-admin.py collectstatic')


def compile():
    """Compile static files"""
    local('django-admin.py collectstatic')
    local('gulp')
    local('rm -rf var/www/static/coffee')
    local('rm -r var/www/static/css/*.scss')
