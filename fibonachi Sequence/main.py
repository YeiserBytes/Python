fib = [0, 1]
last_term = int(abs(float(input("Enter the last term: ")))) - 2;
for i in range(last_term):
    fib.append(fib[i] + fib[i+1])

print(fib)