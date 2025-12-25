"""
    1. Configure Database URI
    2. Configure Track Modifications
"""

import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URI = os.getenv("POSTGRES_URI")

#   DATABASE URI & TRACK MODIFICATIONS

SQLALCHEMY_DATABASE_URI = POSTGRES_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
