import streamlit as st

def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        return 'Invalid Operation'

st.title("Simple Calculator")

operation = st.selectbox("Choose an operation:", ['Add', 'Subtract', 'Multiply', 'Divide'])
num1 = st.number_input("Enter first number", step=0.01)
num2 = st.number_input("Enter second number", step=0.01)

if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f'Result: {result}')
