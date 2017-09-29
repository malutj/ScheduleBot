from os import getenv

from .base import *

if os.getenv("SERVER_ENVIRONMENT") == "PRODUCTION_ENV":
    from .production_settings import *
else:
    from .development_settings import *

try:
    from .local_settings import *
except:
    pass