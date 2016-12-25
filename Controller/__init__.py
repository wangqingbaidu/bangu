from Model import model
from Model.ModelDB import error_enum
from datetime import datetime
def putErrorlog2DB(error_thread, e, db = model):
    error_id = 1
    for i in error_enum:
        if i['thread'] == error_thread:
            error_id = i['id']
            break
    if db:
        log = {}
        log['e'] = repr(e)
        log['error_type'] = error_id
        log['datetime'] = datetime.now()
        db.insert_errorlog(log)
    
if __name__ == '__main__':
    putErrorlog2DB('ThreadUpdateWeather2DB', 'None')