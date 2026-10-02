class my_data:
    def __init__(self,name,per):
        self.n = name
        self.p = per

    def display(self):
        print(f"my name is : {self.n}")
        print(f"my percentage is : {self.p}")

obj = my_data("riyoo" , 88.9)
obj.display()
        