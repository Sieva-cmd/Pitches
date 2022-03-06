import os
class Config:
  
    UPLOADED_PHOTOS_DEST ='app/static/photos'
       # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True



class TestConfig(Config):
    #  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sieva@localhost/watchlist_test'
    pass

           
class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sieva@localhost/pitches'
    DEBUG =True
    
    
config_options ={
        'development':DevConfig, 
        'production':ProdConfig,
        'test':TestConfig
         }  

#email configurations
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 587
# MAIL_USE_TLS = True
# MAIL_USERNAME = os.environ.get("sieva.musyoka@student.moringaschool.com")
# MAIL_PASSWORD = os.environ.get("sieva_md5")


