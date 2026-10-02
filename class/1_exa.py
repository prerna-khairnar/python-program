class demo:
  num=100;
  def display():
    print("this is class function")

d = demo
d.display()
print("value of num is : ",d.num)   

#by using self
class demo:
    num = 100

    def display(self):
        print("this is class function")
        print("value of num is :", demo.num)


# object creation
d = demo()
d.display()
