import os
import re
Base_dir = os.path.dirname(os.path.dirname(__file__))
with open(Base_dir + "/data/1234.txt", mode="r") as f:
    with open(Base_dir + "/data/result.txt",mode="a") as f2:
        for i in f.readlines():
            print(i)
            pattern="2020-08-11 17:13:52.*"
            if re.match(pattern,i):
                f2.write(i)

