class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls, parameter):
        # Phương thức thuộc về lớp có thể truy cập cls (là lớp) và class_variable
        print(f"Class variable: {cls.class_variable}")
        print(f"Parameter: {parameter}")

# Sử dụng phương thức thuộc về lớp
MyClass.class_method("Hello")
