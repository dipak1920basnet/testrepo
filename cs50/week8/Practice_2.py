class Student:
    def __init__(self, name, address):
        if not name:
            raise ValueError("Missing name")
        if address not in ["Gryffindor","Huffliepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid address")
        self.name = name
        self.address = address
        
def main():
    student = get_student()
    print(f"Hello my name is {student.name} and I am from {student.address}")

def get_student():
    name = input("Enter the student name:")
    address = input("Enter the student address")
    return Student(name, address)

if __name__ == "__main__":
    main()