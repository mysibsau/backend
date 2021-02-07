from core.config.environ import env
from sentry_sdk.integrations.django import DjangoIntegration


if env.bool('SENTRY'):
    import sentry_sdk

    sentry_sdk.init(
        dsn=env.str('DSN'),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
