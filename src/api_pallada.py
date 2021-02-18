import xmlrpc.client


class API:
    def __init__(self, database: str, login: str, password: str):
        self.db = database
        self.login = login
        self.password = password
        self.url = f'https://{database}.pallada.sibsau.ru'
        self.uid = self.__get_uid(self.login, self.password)

        self.__dict__ = {
            **self.__dict__,
            'read': self.__do('read'),
            'search': self.__do('search'),
            'count': self.__do('search_count'),
            'fields_get': self.__do('fields_get'),
            'search_read': self.__do('search_read'),
        }

    def __get_uid(self, login, password) -> int:
        common = xmlrpc.client.ServerProxy(self.url + '/xmlrpc/2/common')
        return common.authenticate(
            self.db,
            login,
            password,
            {},
        )

    def __do(self, method: str):
        def tmp(model_name: str, args: list, kwargs: dict):
            models = xmlrpc.client.ServerProxy(self.url + '/xmlrpc/2/object')
            return models.execute_kw(
                self.db,
                self.uid,
                self.password,
                model_name,
                method,
                args,
                kwargs,
            )
        return tmp
