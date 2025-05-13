import json 

db_path = "db.json"

def get_info_from_db(db_path):
    call_db = open(db_path, "r")
    data = json.load(call_db)
    return data

data = {"5001": 'pepe'}
call_db = open(db_path, "w")
json.dump(data, call_db)
call_db.close()

a =  get_info_from_db(db_path)
print(a)


