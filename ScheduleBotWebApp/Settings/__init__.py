from os import getenv

from .base import *

if os.getenv("SERVER_ENV") == "PRODUCTION_ENV":
    from .production import *
else:
    from .development import *

try:
    from .local_settings import *
except:
    pass