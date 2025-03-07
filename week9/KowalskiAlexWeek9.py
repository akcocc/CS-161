class Student:
    name: str
    age: int
    grade: int

    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name;
        self.age = age;
        self.grade = grade;

class Staff:
    name: str
    department: str
    role: str
    salary: int

class Teacher(Staff):
    age: int
    def __init__(self, name: str, department: str, salary: int, age: int) -> None:
        self.name = name;
        self.department = department;
        self.role = "Teacher";
        self.salary = salary;
        self.age = age;

class Square:
    side_length: int

    def __init__(self, side_length: int) -> None:
        self.side_length = side_length;

    def area(self) -> int:
        return self.side_length**2;

    def perimiter(self) -> int:
        return self.side_length*4;

if __name__ == "__main__":
    jeffery = Student("jeffery", 13, 7);
    print("Student:")
    print("Name: ", jeffery.name);
    print("Age: ", jeffery.age);
    print("Grade: ", jeffery.grade, "\n");
    johnson = Teacher("johnson", "Science", 60_000, 57);

    print("Teacher:")
    print("Name: ", johnson.name);
    print("Age: ", jeffery.age);
    print("Grade: ", jeffery.grade, "\n");
    print(johnson.age);
    print(johnson.role);

    square1 = Square(30);
    print("Square 1:");
    print("Area:", square1.area())
    print("Perimiter:", square1.perimiter(), "\n")

    square2 = Square(200);

    print("Square 2:");
    print("Area:", square2.area())
    print("Perimiter:", square2.perimiter(), "\n")

