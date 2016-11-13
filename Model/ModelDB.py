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
import sys, os
sys.path.append(os.getenv('BANGUHOME', '~/bangu'))
reload(sys)

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import CHAR, Integer, String, Float, DateTime
BaseModel = declarative_base()
from utils.ParserCityJson import ParserCityJson

class ModelDB:
    """
    This class is used to define all operations when contact to database.
    Parameters
    -------------
    @echo: whether to display the execute sql.
    """
    def __init__(self,
                 echo = False):
        DB_CONNECT_STRING = 'sqlite:///%s/bangu.db' %os.getenv('BANGUHOME', '~/bangu')
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
    
    def get_latest_weather(self):
        return self.session.query(Weather).order_by(Weather.id.desc()).first()
        
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
    humidity  = Column(CHAR(10))
    tmp_max = Column(Float)
    tmp_min = Column(Float)
    pm25 = Column(Float)
    desc = Column(Integer)
    suggestion = Column(CHAR(100))

if __name__ == '__main__':
    m = ModelDB()
    c = ParserCityJson('../city.json')
#     m.insert_cities(c.get_cities())