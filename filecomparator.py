
class student:
  def __init__(self, name, mobile):
    self.name = name
    self.mobile = mobile
    
  def my_name(self):
      return self.name
  
  def my_mobile(self):
      return self.mobile  
    
#p1 = Person("John", 36)

f1dict = {}
f2dict = {}


f1 = open("file1.csv", "r")
for x in f1:
  #employeeid,name,mobile
  x=x.rstrip();
  l1=x.split(",")
  if l1[0]!="employeeid" :
    p1=student(l1[1],l1[2])
    f1dict[l1[0]]=p1

#print(f1dict)

f1.close()


f2 = open("file2.csv", "r")
for x1 in f2:
  #name|mobile|employeeid
  x1=x1.rstrip()
  l2=x1.split("|")
  if l2[2]!="employeeid" :
    p2=student(l2[0],l2[1])
    f2dict[l2[2]]=p2

#print(f2dict)

f2.close()


for x in f1dict:
  #print(x)
  if f1dict[x].my_name() != f2dict[x].my_name():
     print (x + " name not matched")
  
  if f1dict[x].my_mobile() != f2dict[x].my_mobile():
     print (x + " mobile  not matched")
     
