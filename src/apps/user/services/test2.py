import xmlrpc.client
from pprint import pprint
from time import time


url = 'https://portfolio.pallada.sibsau.ru'
db = 'portfolio'
username = '18731006'
password = ',81MrhqJ+G'


common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
print(uid)
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# tmp = models.execute_kw(
#     db, uid, password, 'portfolio_science.grade_view', 'fields_get',
#     [], {'attributes': ['string', 'help', 'type']})


user = models.execute_kw(
    db, uid, password,
    'portfolio_science.grade_view', 'search',
    [[['ID_student', '=', username]]],
)


pprint(user)
