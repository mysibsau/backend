from fabric import task, Connection
from os import getenv
from time import time


connect_kwargs = {'password': getenv('SERVER_PASSWORD')}
server = Connection(
    getenv('SERVER'),
    connect_kwargs=connect_kwargs
)
PATH = getenv('SERVER_PATH')


def _get_time():
    return int(time() * 1000)


@task
def backup(c):
    """
    Создание резервных копий
    """
    print('Run backup...')
    print('\tbackup media...')
    server.run(f'tar -cf media_{_get_time()}.tar.gz {PATH}media')
    print('\tOK media')
    print('OK')
