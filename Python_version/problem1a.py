import pdpcore


number_of_equation = int(input("Number of Equation : "))
koefficients = [[0 for i in range(number_of_equation)] for i in range(number_of_equation)]
eq_result = [0 for i in range(number_of_equation)]

for i in range(number_of_equation):
    koefficients[i] = list(map(float, input(f"Enter the linear equation koefficients {i+1} separated by space:").split()))
    for j in range(number_of_equation):
        print(koefficients[j])

eq_result = list(map(float, input("Enter the linear equation results separated by space:").split()))

print("=============================== Matrix form ====================================")
for i in range(len(koefficients)):
    print(f"{koefficients[i]} x{i+1} = {eq_result[i]}")

command = int(input("solving method (1 = gauss_elimination/2 = gauss_seidel)? : "))

if command == 1:
    result = pdpcore.gauss_eliminate(koefficients, eq_result)
    print("solution by gauss elimination method")
    for i in range(len(result)):
        print(f"x{i+1} = {result[i]}")
elif command == 2:
    result = pdpcore.gauss_seidel(koefficients, eq_result)
    print("solution by gauss-seidel method")
    for i in range(len(result)):
        print(f"x{i+1} = {result[i]}")
else:
    print("invalid command")


