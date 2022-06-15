# person 클래스를 터미널에 input 해서 넣는 과정 

people = []
class Person_input:
    def __init__(self,*args):
        while True:
            self.name = input("이름은:")
            self.id = input("ID:")
            self.age = int(input("나이는:"))
            self.height = int(input("키는:"))
            self.weight = int(input("몸무게가 왜 궁금할까:"))
            people.append(Person_input(self.name, self.id, self.age, self.height, self.weight))

            if self.name == "끝":
                break

a = Person_input()
print(a)
    

    
