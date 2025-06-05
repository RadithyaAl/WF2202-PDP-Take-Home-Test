import pdpcore


number_of_equation = int(input("Number of Equation : "))
inputs_data = [0 for i in range(number_of_equation)]
koefficients = [[0 for i in range(number_of_equation)] for i in range(number_of_equation)]
eq_result = [0 for i in range(number_of_equation)]

for i in range(number_of_equation):
    user_input = list(map(int, input(f"Enter the linear equation {i+1} separated by space:").split()))
    inputs_data[i] = user_input
    for j in range(len(inputs_data)):
        print(inputs_data[j])


# taking the koefficients from the input
for i in range(len(inputs_data)):
    for j in range(number_of_equation):
        koefficients[i][j] = inputs_data[i][j]


# taking the right hand side of the matrix
for i in range(len(inputs_data)):
    eq_result[i] = inputs_data[i][-1]



print("=============================== Matrix form ====================================")
for i in range(len(koefficients)):
    print(f"{koefficients[i]} x{i+1} = {eq_result[i]}")

command = str(input("Proceed to gauss elimination(y/n)?"))
if command in ['y', '']:
    result = pdpcore.gauss_eliminate(koefficients, eq_result)
    print(f"calculation result :")
    for i in range(len(result)):
        print(f"x{i+1} = {result[i]}")
else:
    print("operation cancelled")
    

