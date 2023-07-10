import pandas 

csvfile = pandas.read_csv('employees.csv')
print(csvfile)


data = [
    ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID'],
    ['198', 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '21-JUN-07', 'SH_CLERK', '2600', '-', '124', '50'],
    ['199', 'John', 'Smith', 'JSMITH', '123.456.7890', '15-JUL-07', 'SA_REP', '5000', '0.1', '123', '60'],
    ['200', 'Jane', 'Doe', 'JDOE', '987.654.3210', '01-AUG-07', 'IT_PROG', '4000', '-', 'NULL', '40']
]

df = pandas.DataFrame(data)

df.to_csv('employees.csv', index=False)

print("Data written to employees.csv file.")