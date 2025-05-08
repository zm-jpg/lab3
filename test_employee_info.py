import employee_info as info

def test_get_employees_by_age_range():
    result=info.get_employees_by_age_range(20,30)
    expected=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    assert(result==expected)

def test_calculate_average_salary():
    info.employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 100000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 69000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    average=info.calculate_average_salary()

    assert(average==69166.666666666666)

def test_get_employees_by_dept():
    info.employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    department="Sales"
    result=info.get_employees_by_dept(department)
    expected=[{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert(result==expected)




