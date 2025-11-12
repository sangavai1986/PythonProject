class Person:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill

    def getskill(self):
        print("Hello I am",self.name)
        print("My age : ",self.age)
        print("My skill is ",self.skill)

p1 = Person("San",34,"Perl")
p1.getskill()
