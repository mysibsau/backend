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
    print('Создание архива...')
    c.run('cp -r src deploy')
    c.run('rm -rf deploy/media')
    c.run('rm -rf deploy/tests')

    c.run('tar -cjf deploy.bz2 deploy')
    c.run('rm -rf deploy')
    print('Создание архива окончено')

    print('Загрузка архива...')
    server.put('deploy.bz2')
    c.run('rm deploy.bz2')

    server.run('tar -xf deploy.bz2')
    server.run('rm deploy.bz2')

    server.run(f'cp -r {PATH}/media deploy/')
    print('Загрузка архива окончена')

    print('Загрузка системных ресурсов...')
    server.put('.env.prod', 'env.deploy')
    server.put('Pipfile')
    server.put('Pipfile.lock')
    print('Загрузка системных окончена')


    # server.run('mv server server_old')
    # server.run('mv deploy server')
