import json
import os
Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
with open(Base_dir+"/data/upload_android.json",mode='r',encoding='utf-8') as f:
    init_json=json.load(f)
    print(init_json["udr"]["d"][0])
    data=init_json["udr"]["d"][0]
    j=1
    while j <=349:
        init_json["udr"]["d"].append(data)
        j+=1
with open (Base_dir+"/data/repeat_cunsumer.json",mode='w',encoding='utf-8') as f:
    f.write(json.dumps(init_json))
print(init_json)




