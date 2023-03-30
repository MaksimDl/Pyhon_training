num = int(input("Input the number"))

# 0,1,1,2,3,5,8,13
# num > 1
fib_n_1 = 1
fib_n_2 = 0
fib = 1
index = 2
while fib < num:
    fib = fib_n_1 + fib_n_2
    fib_n_2 = fib_n_1
    fib_n_1 = fib
    index += 1
    print("fib = ", fib)

#print("fibbbb=",fib)

if fib_n_1 == num:
    print("The number is fibonachi number, index = ", index)
else:
    print("-1")

