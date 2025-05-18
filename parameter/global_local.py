
y = 2
def fun():
    x = 1
    y = 1
    print(x)

print(y)
# print(x)


x = 2
def fun():
    global x
    x = 1
fun()
print(x)