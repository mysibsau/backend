from fabric import task, Connection
from os import getenv
from time import time
from invoke import Responder


connect_kwargs = {'password': getenv('SERVER_PASSWORD')}
server = Connection(
    getenv('SERVER'),
    port=getenv('SERVER_PORT'),
    connect_kwargs=connect_kwargs
)
sudo_password = Responder(
        pattern=r'\[sudo\] password:',
        response=f'{getenv("SERVER_PASSWORD")}\n',
    )
PATH = getenv('SERVER_PATH')


def _get_time():
    return int(time() * 1000)


def _media_backup(c):
    print('\tbackup media...')
    c.run(f'tar -cf backups/media_{_get_time()}.tar.gz {PATH}/media')
    print('\tOK media\n')


def _db_backup(c):
    print('\tbackup database...')
    db_password = Responder(
        pattern='Password:',
        response=f'{getenv("DATABASE_PASSWORD")}\n',
    )
    c.run(
        f'pg_dump -h 127.0.0.1 -U {getenv("DATABASE_USER")} -F t'
        f' -f backups/dump_db_{_get_time()}.tar {getenv("DATABASE_NAME")}',
        watchers=[db_password]
    )
    print('\tOK database')


def _load_configs(c):
    server.sudo(
        'mv /etc/systemd/system/gunicorn.service /etc/systemd/system/gunicorn_old.service',
        watchers=[sudo_password]
    )
    server.put('gunicorn.service')
    server.sudo(
        'mv gunicorn.service /etc/systemd/system/gunicorn.service',
        watchers=[sudo_password]
    )
    server.sudo(
        'systemctl restart gunicorn.service',
        watchers=[sudo_password]
    )


@task
def backup(c):
    """
    Создание резервных копий
    """
    print('Run backup...')
    server.run('mkdir -p backups')
    _media_backup(server)
    _db_backup(server)

    print('OK')


@task
def deploy(c):
    print('Удаление старых версий...')
    server.run('rm -rf server_old')
    server.sudo(
        'rm rm /etc/systemd/system/gunicorn_old.service',
        watchers=[sudo_password]
    )

    print('Создание архива...')
    c.run('cp -r src deploy')
    c.run('rm -rf deploy/media')
    c.run('rm -rf deploy/tests')

    c.run('tar -cjf deploy.bz2 deploy')
    c.run('rm -rf deploy')

    print('Загрузка архива...')
    server.put('deploy.bz2')
    c.run('rm deploy.bz2')

    server.run('tar -xf deploy.bz2')
    server.run('rm deploy.bz2')

    print('Перенос папки медиа...')
    server.run(f'cp -r {PATH}/media deploy/')

    print('Загрузка системных ресурсов...')
    server.put('.env.prod', '.env')
    server.put('Pipfile.lock')

    print('Установка пакетов...')
    server.run('python3 -m pipenv sync')

    print('Перенос папки проекта')
    server.run('mv server server_old')
    server.run('mv deploy server')

    print('Накатываение миграций...')
    with server.cd('server/'):
        server.run('python3 -m pipenv run python manage.py migrate')

    print('Загрузка конфигов...')
    _load_configs(c)


@task
def cancel(c):
    print('Откат папки проекта...')
    server.run('rm -rf server')
    server.run('mv server_old server')

    print('Откат конфигов')
    server.sudo(
        'rm /etc/systemd/system/gunicorn.service',
        watchers=[sudo_password]
    )
    server.sudo(
        'mv /etc/systemd/system/gunicorn_old.service /etc/systemd/system/gunicorn.service',
        watchers=[sudo_password]
    )
    server.sudo(
        'systemctl restart gunicorn.service',
        watchers=[sudo_password]
    )
