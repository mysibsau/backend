AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = (
    'apps.user.odoo_backend_auth.OdooBackend',
)
