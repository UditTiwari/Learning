work_hours = [('emp_x',100),('emp_y',300),('emp_z',500)]


def employee_check(work_hours):
    current_max = 0
    emp_of_month = ''
    
    for employee,hours in work_hours:
        if hours> current_max:
            current_max = hours
            emp_of_month = employee
        else:
            pass
    return current_max,emp_of_month
    
    
print(employee_check(work_hours))


