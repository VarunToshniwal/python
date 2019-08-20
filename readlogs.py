import time, os,re
filename = "C:/Program Files/Pitney Bowes/Spectrum/server/app/repository/logs/wrapper.log" 
file = open(filename,'r')
print("started")
#Find the size of the file and move to the end
st_results = os.stat(filename)
print(st_results)
st_size = st_results[6]
print(st_size)
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    #print(re.search ("Pitney Bowes Spectrum(TM) Technology Platform (Version 0-SNAPSHOT \d) Started",line ))
    x=re.findall ("^Pitney Bowes Spectrum\(TM\) Technology Platform \(Version 0-SNAPSHOT [0-9]{1,4}\) Started$",line)
    if (x) :
        print("server started")
        break
    elif not line:
        time.sleep(1)
        file.seek(where)
    else:
        print( line) # already has newline
        
