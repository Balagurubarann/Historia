"""
    1. Configure Database URI
    2. Configure Track Modifications
"""

import os
from urllib.parse import quote_plus

password = "kuhan@11"
db_host = "192.168.100.59"
db_password = quote_plus(password)

"""
    DATABASE URI & TRACK MODIFICATIONS
"""
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://postgres:{db_password}@{db_host}:5432/historia_db"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
