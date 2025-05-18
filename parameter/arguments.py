def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)
report('Ben', 80, 90, 85)


def info(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k, v)
info('Mike', age=24, country='China', education='bachelor')

