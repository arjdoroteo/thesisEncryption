import datetime
from datetime import datetime
import pathlib
now = datetime.now()
date_time = now.strftime("%m/%d/%Y")
pathsss = pathlib.Path().resolve()
print(pathsss)
print(date_time)
temp = 69
co = 6969
gas = 696969
local_Date = str(pathsss) + "/" + now.strftime("%m-%d-%Y") + ".csv"
f = open(local_Date, 'a')
f.write("{}, {}, {}, {}".format(date_time, temp, co, gas))
f.close
