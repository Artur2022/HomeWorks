
from http.client import LENGTH_REQUIRED


expression = input("Write your expression")
lengthExpression = len(expression)

for i in range(lengthExpression):
    if(expression[i] == '+'):
        print(int(expression[i-1])+int(expression[i+1]))
    if(expression[i] == '-'):
        print(int(expression[i-1])-int(expression[i+1]))
    if(expression[i] == '*'):
        print(int(expression[i-1])*int(expression[i+1]))
    if(expression[i] == '/'):
        print(int(expression[i-1])/int(expression[i+1]))
