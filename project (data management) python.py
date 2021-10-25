#student data management program

class student:
    def __init__(self,name,rollno,age): ## need two underscore __
      self.name = name
      self.rollno = rollno
      self.age = age

    def create(self,name,rollno,age):
      ob = student(name,rollno,age)
      ls.append(ob)


#function to display the list of students detail
    def display(self,ls):
      print("name:",ls.name)
      print("rollno:",ls.rollno)
      print("age:",ls.age)
      print("\n")


#create a list to add students data
ls = []

#creating a object for the student class
obj = student("Swara",1,10)
print("operation used...\n")
print("1.add the students detail \n2.diplay the student detail \n3.exit")

obj.create("swara",16,14)
obj.create("alex",23,16)
obj.create("Chaka",0,1)

print("\n")
print("list of students detail")
for i in range(ls.__len__()): # two underscore
    obj.display(ls[i])
    print("data added successfully......")               


          


      
