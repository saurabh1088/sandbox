class Employee:
    def __init__(this_can_be_any_name_other_than_self_also, name, age):
        this_can_be_any_name_other_than_self_also.name = name
        this_can_be_any_name_other_than_self_also.age = age

    def display_info(this_can_be_any_name_other_than_self_also):
        print(f"Name: {this_can_be_any_name_other_than_self_also.name}, Age: {this_can_be_any_name_other_than_self_also.age}")


employee_one = Employee("Alice", 30)
employee_one.display_info()