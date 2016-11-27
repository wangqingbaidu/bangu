# -*- coding: UTF-8 -*- 
'''
utils.ParserCityJson is a part of the project bangu.
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

import json, os
class ParserCityJson:
    """
    This class is used to convert city json file to dict type.
    Path to json file must contains three columns id, cityEn, countryCode
        id stands for the city id.
        cityEn stands for English name of this city.
        countryCode stands for short name of country which this city belongs to.
    Parameters
    -------------
    @jsonFile: Path to city json file.
    """
    cities = None
    def __init__(self, jsonFile = '../city.json'):
        self.jsonFile = jsonFile
        
    def parser_city_json(self):
        self.cities = []
        if not os.path.exists(self.jsonFile):
            print 'Json city file %s not exists!' %self.jsonFile
        else:
            json_str = open(self.jsonFile).read()
            for item in json.loads(json_str):
                self.cities.append({'id':item['id'], 
                                    'cityEn':item['cityEn'], 
                                    'countryCode': item['countryCode']})
    
    def get_cities(self):
        if self.cities == None:
            self.parser_city_json()
        return self.cities
                
if __name__ == '__main__':
    ParserCityJson('../city.json')