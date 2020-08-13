# Author 张楚潼
# 2020/7/26

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("salary需为数字形式！")

# 格式化输出
# information ="""
# -------info of %s-------
# Name: %s
# Age: %d
# Job: %s
# Salary: %.2f
# ---------end------------
# """ % (name, name, age, job, salary)
# print(information)

print("-------info of %s-------\nName: %s\nAge: %d\nJob: %s\nSalary: %.2f\n---------end------------"\
      % (name, name, age, job, salary))
