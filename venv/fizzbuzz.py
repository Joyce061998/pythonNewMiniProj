for i in range(1,16):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    elif  i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)


"""
scanner in = ne

"""

n = [5, 10, 15, 20, 25, 30]
fn = list(filter(lambda x: x > 15, n))
print(fn)



