# Base class for student and staff as both are persons
class Person:
    name: str
    age: int

# Student, as a subclass, has its own member 'grade' which the parent class
# does not have since not all `Person`'s will be students.
# Student _inherits_ all members/methods of its parent class and its inherited
# members/methods, if any.
class Student(Person):
    grade: int
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name;
        self.age = age;
        self.grade = grade;

# Base class for Teacher as teachers are staff members
class Staff(Person):
    role: str
    salary: int

# Teacher, as a subclass, has its own member 'department' which the parent class
# does not have since not all `Staff`'s will be teachers in a department.
# Teacher _inherits_ all members/methods of its parent class and its inherited
# members/methods, if any.
class Teacher(Staff):
    department: str
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

    # `self` defines the 'object' to operate on,
    # in this case we're using `self`'s `side_length` property to calculate
    # the area of a square.
    # `self` is also implicitly being passed into the `area()` function
    # whenever used as a method, i.e being used with the syntax: `object.method()`,
    # where `object` is the `self` argument which is implicitly passed into `method()`
    def area(self) -> int:
        return self.side_length**2;

    def perimiter(self) -> int:
        return self.side_length*4;

if __name__ == "__main__":
    # class initialization happens when a class name is used as a function,
    # returning an empty instance of the class (ex: `class_instance = ClassName()`).
    # Furthermore, how an instance of a class is initialized can be controlled
    # by having an optional `__init__()` method defined in the class's scope,
    # which is implicitly called after creating an empty instance of a class.
    # Additionally, the `__init__()` method can have arguments to be used
    # during the initialization of the instance. In total, the way an instance
    # of a class is initialized in python can look something like this:
    # ```
    # # an empty class instance is created by using the class's `__new__` function
    # # which returns an new instance of the class. Since `Student` doesn't
    # # define its own `__new__` function, calling `__new__()` on `Student`, just
    # # returns an empty instance of `Student`.
    # jeffery = Student.__new__(Student)
    #
    # # the `__init__()` method is called on the initial empty instance, passing
    # # the desired arguments in, as well as implicitly passing in the `jeffery`
    # # instance itself for the `self` argument, as is done with all class methods
    # # operating on an instance of a class.
    # jeffery = jeffery.__init__("jeffery", 13, 7)
    # ```
    #
    # However, you wouldn't really write actual code in this way, and
    # it can be simplified by doing the following instead:
    jeffery = Student("jeffery", 13, 7);
    print("Student:")
    # the members for an instance of a class, such as `jeffery` can be accessed
    # outside of the scope of the class itself using the following syntax: `object.parameter`
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
    # members are functions which operate on an instance of a class, such as
    # `square1`. Methods are usually used when the caller wants to modify the
    # a class instance outside of the Class's scope. However, a method may also
    # return additional data when called on an instance, and also isn't
    # necessarily required to modify the instance's data.
    #
    # In this case, the `area()` method, doesn't actually modify `square1`, and
    # just returns `square1`'s area by squaring its `side_length` member.
    print("Area:", square1.area())
    # A similar thing happens with the `perimiter()` method.
    print("Perimiter:", square1.perimiter(), "\n")

    square2 = Square(200);

    print("Square 2:");
    print("Area:", square2.area())
    print("Perimiter:", square2.perimiter())
