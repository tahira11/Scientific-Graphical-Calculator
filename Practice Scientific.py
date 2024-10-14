import streamlit as st
import math

# Streamlit app title
st.title("Scientific Calculator")

# Dropdown for selecting the operation
operation = st.selectbox(
    "Select an operation:",
    ["Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Exponentiation", "Logarithm",
     "Sine", "Cosine", "Tangent", "Factorial"]
)

# Input fields based on the selected operation
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    num1 = st.number_input("Enter the first number:", step=1.0, format="%.4f")
    num2 = st.number_input("Enter the second number:", step=1.0, format="%.4f")
elif operation in ["Square Root", "Logarithm", "Factorial"]:
    num1 = st.number_input("Enter the number:", step=1.0, format="%.4f")
elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter the angle in degrees:", step=1.0, format="%.4f")

# Calculate based on operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.write("Error! Division by zero.")

    elif operation == "Square Root":
        if num1 >= 0:
            result = math.sqrt(num1)
            st.write(f"Result: √{num1} = {result}")
        else:
            st.write("Error! Square root of a negative number is not real.")

    elif operation == "Exponentiation":
        result = num1 ** num2
        st.write(f"Result: {num1} ^ {num2} = {result}")

    elif operation == "Logarithm":
        if num1 > 0:
            result = math.log(num1)
            st.write(f"Result: log({num1}) = {result}")
        else:
            st.write("Error! Logarithm of non-positive number is not defined.")

    elif operation == "Sine":
        result = math.sin(math.radians(angle))
        st.write(f"Result: sin({angle}°) = {result}")

    elif operation == "Cosine":
        result = math.cos(math.radians(angle))
        st.write(f"Result: cos({angle}°) = {result}")

    elif operation == "Tangent":
        result = math.tan(math.radians(angle))
        st.write(f"Result: tan({angle}°) = {result}")

    elif operation == "Factorial":
        if num1 >= 0 and num1 == int(num1):
            result = math.factorial(int(num1))
            st.write(f"Result: {int(num1)}! = {result}")
        else:
            st.write("Error! Factorial of negative or non-integer number is not defined.")
