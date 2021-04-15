student = {'name':'John','age':24, 'courses':['Math','CS']}
print(student)
# student['phone'] = '5555-555'
# student['name'] = 'Jane'
# print(student)

# OR
student.update({'name':'Jane','age':26,'phone-number':'+91-982828291'})
print(student)

# del student['age']
# print(student)


# age = student.pop('age')
# print(student, "\n", age)

# print(len(student))
# print(student.keys())
# print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)

