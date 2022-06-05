import os
from typing import List

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
if os.path.exists(".env"):
    env.read_env()

SENTRY_DSN: str = env("CERTN_SENTRY_DSN", default=None)
