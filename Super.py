# What can we archieve by use of super keyword 
# 1. If there is a method in the parent class that we want our child to share some of the functionality of. 
# 2. if we want our Child class to inherit a method from the parent and then augment it in some way.

class User:
    def log_in(self):
        print("User.log_in() called.")
        

class Student(User):
    def log_in(self):
        print("Student.log_in() called.")
        super().log_in()
        
# oneil = Student()
# oneil.log_in()

# the super keyword will call on the log_in() method as defined in the superclass. 
# Then, the additional code that we're adding into our Student.log_in() method will also run.
# therefore we have supercharged our log_in() method, for the Student class.



# Calling super with arguments

class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name

   

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade

    

oneil = Student("O'neil", 10)
print(oneil.__dict__)

# Here We call super with an argument from the Student.__init__ method, 
# which will call the User.__init__ method with that argument.
# both the Student and User classes define a name instance variable 
# and set it when the class is instantiated. This not particularly DRY
# Ideally, we'd like to be able to call the __init__ method on the User class when a new student is created.