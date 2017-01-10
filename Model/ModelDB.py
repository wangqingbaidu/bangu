# -*- coding: UTF-8 -*- 
'''
Model.ModelDB is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.types import CHAR, Integer, String, Float, DateTime
BaseModel = declarative_base()
from utils.ParserCityJson import ParserCityJson
from datetime import timedelta, datetime

error_enum = [{'id':1, 'thread':'Unknown', 
               'suggestion':'Unknown error!'},
              {'id':2, 'thread':'ThreadUpdateWeather2DB', 
               'suggestion':'Can not get weather info, maybe network is not connected!'},
              {'id':3, 'thread':'ThreadWeatherLEDFlicker', 
               'suggestion':'Red or Green or Yellow LED not set!'},
              {'id':4, 'thread':'ThreadIndoorTmpHum2DB', 
               'suggestion':'Command is not executed successfully!'},
              {'id':5, 'thread':'ThreadLCDTemperatureHumidity', 
               'suggestion':'Can not get Tmp and Hum data from db!'},
              {'id':6, 'thread':'ThreadPushImage2Phone', 
               'suggestion':'Push message error, Check appid or secret!'}]

class ModelDB:
    """
    This class is used to define all operations when contact to database.
    Class XXX which based on @BaseModel is abstract database data. 
    Parameters
    -------------
    @echo: whether to display the execute sql.
    
    Methods
    -------------
    @insert_XXX: insert XXX data to db.
    @get_XXX: get XXX data from db. 
    """
    def __init__(self,
                 echo = False):
        DB_CONNECT_STRING = 'sqlite:///%s/bangu.db' %GetBanguHome.getHome()
        self.engine = create_engine(DB_CONNECT_STRING, echo=echo)
        self.session = sessionmaker(bind=self.engine)()
#         self.flush_db()
        self.init_db()
        
    def init_db(self):
        BaseModel.metadata.create_all(bind = self.engine)
        
    def flush_db(self):
        BaseModel.metadata.drop_all(bind = self.engine)
        
    def insert_cities(self, cities):
        self.session.execute(City.__table__.insert(), cities)
        self.session.commit()
        
    def insert_weather(self, weather):
        self.session.execute(Weather.__table__.insert(), weather)
        self.session.commit()
    
    def insert_tmphum(self, tmphum):
        self.session.execute(TmpHum.__table__.insert(), tmphum)
        self.session.commit()
        
    def insert_error(self, error):
        self.session.execute(Error.__table__.insert(), error)
        self.session.commit()   
        
    def insert_errorlog(self, errorlog):
        self.session.execute(ErrorLog.__table__.insert(), errorlog)
        self.session.commit()
        
    def insert_audio_token(self, access_token):
        self.session.execute(AudioToken.__table__.insert(), access_token)
        self.session.commit()
        
    def get_latest_weather(self):
        return self.session.query(Weather).order_by(Weather.id.desc()).first()
    
    def get_latest_tmphum(self):
        return self.session.query(TmpHum).order_by(TmpHum.id.desc()).first()

    def get_log(self, delta = None):
        toTime = datetime.now()
        if not delta:
            delta = 87600
        fromTime = datetime.now() - timedelta(hours = delta)  
        return self.session.query(ErrorLog).filter(ErrorLog.datetime >= fromTime, \
                ErrorLog.datetime <= toTime).order_by(ErrorLog.datetime.desc()).all()
    
    def get_latest_audio_token(self):
        return self.session.query(AudioToken).order_by(AudioToken.id.desc()).first().access_token
        
        
class City(BaseModel):    
    __tablename__ = 'city'
    id  = Column(CHAR(20), primary_key=True)    
    cityEn  = Column(CHAR(50))
    countryCode  = Column(CHAR(20))

class Weather(BaseModel):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    city = Column(CHAR(20))
    country = Column(CHAR(20))
    datetime  = Column(DateTime)    
#     humidity  = Column(CHAR(10))
    tmp_max = Column(Float)
    tmp_min = Column(Float)
#     pm25 = Column(Float)
    desc = Column(Integer)
    descCN = Column(String)
#     suggestion = Column(String)
#     comf = Column(String)
#     flu = Column(String)
#     drsg = Column(String)
    
class TmpHum(BaseModel):
    __tablename__ = 'tmphum'
    id = Column(Integer, primary_key=True)
    tmp = Column(Float)
    hum = Column(Float)
    datetime  = Column(DateTime) 

class Error(BaseModel):
    __tablename__ = 'error'
    id = Column(Integer, primary_key=True)
    thread = Column(String)
    suggestion = Column(String)
    
class ErrorLog(BaseModel):
    __tablename__ = 'errorlog'
    id = Column(Integer, primary_key=True)
    error_type = Column(Integer, ForeignKey('error.id'))
    e = Column(String)
    datetime  = Column(DateTime)     

class AudioToken(BaseModel):
    __tablename__ = 'audio_token'
    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    session_key = Column(String)
    scope = Column(String)
    refresh_token = Column(String)
    session_secret = Column(String)
    expires_in = Column(String)
    datetime  = Column(DateTime)         

def init_db(db = ModelDB()):
    c = ParserCityJson()
    db.insert_cities(c.get_cities())
    db.insert_error(error_enum)

if __name__ == '__main__':
    init_db()
#     m.insert_cities(c.get_cities())