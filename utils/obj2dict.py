# -*- coding: UTF-8 -*- 
'''
utils.obj2dict is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
def obj2dict(obj, ept = []):
    """
    summary: Convert object to dict except callable method and private attributes.
    """
    memberlist = [m for m in dir(obj)]
    _dict = {}
    for m in memberlist:
        if m[0] != "_" and not callable(getattr(obj,m)) and not m in ept:
#             print getattr(obj,m)
            _dict[m] = getattr(obj,m)
    return _dict

