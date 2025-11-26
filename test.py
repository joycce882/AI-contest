class Tanyanshu:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce_print(self):
        print(f"大家好，我是{self.name}，今年{self.age}岁。")

tanyanshu = Tanyanshu("探研树",18)

tanyanshu.introduce_print()