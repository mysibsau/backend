from fabric import task, Connection
from os import getenv
from time import time
from invoke import Responder


connect_kwargs = {'password': getenv('SERVER_PASSWORD')}
server = Connection(
    getenv('SERVER'),
    connect_kwargs=connect_kwargs
)
PATH = getenv('SERVER_PATH')


def _get_time():
    return int(time() * 1000)


def _media_backup(c):
    print('\tbackup media...')
    c.run(f'tar -cf media_{_get_time()}.tar.gz {PATH}media')
    print('\tOK media\n')


def _db_backup(c):
    print('\tbackup database...')
    db_password = Responder(
        pattern='Password:',
        response=f'{getenv("DATABASE_PASSWORD")}\n',
    )
    c.run(
        f'pg_dump -h 127.0.0.1 -U {getenv("DATABASE_USER")} -F t'
        f' -f dump_db_{_get_time()}.tar {getenv("DATABASE_NAME")}',
        watchers=[db_password]
    )
    print('\tOK database')


@task
def backup(c):
    """
    Создание резервных копий
    """
    print('Run backup...')

    _media_backup(server)
    _db_backup(server)

    print('OK')
