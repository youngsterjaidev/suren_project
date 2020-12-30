from fs import open_fs

#with open_fs('~/') as home_fs:
   # with home_fs.open('index.html') as fuck:
        #print(fuck.read())


#home_fs = open_fs("~/")
#home_fs.writetext('goo.txt', 'fuck off')
#home_fs.close()
#with home_fs.open('goo.txt') as goo:
   #print(goo.read())
   
data = data2 = "" 
  
# Reading data from file1 
home = open_fs('~/log')
with home.open('jaidev.txt') as fp: 
        data = fp.read() 
  
# Reading data from file2 
with home.open('fuck.txt') as fp: 
        data2 = fp.read()
        data += "\n"
        data += data2 
  
with home.open ('jaidev.txt', 'w') as fp: 
    fp.write(data) 
