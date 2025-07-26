
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_popcorn'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:car152141711081@db.lmmsxpwbxwwgwbzdnsan.supabase.co:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
