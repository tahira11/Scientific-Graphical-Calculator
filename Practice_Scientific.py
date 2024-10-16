{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tahira11/Scientific-Graphical-Calculator/blob/main/Practice_Scientific.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "DtgsTyZ0JgWh",
        "outputId": "d8910d7c-c062-421b-8096-7a2a28d9963b"
      },
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Welcome to the Scientific Calculator\n",
            "Options:\n",
            "1. Addition (+)\n",
            "2. Subtraction (-)\n",
            "3. Multiplication (*)\n",
            "4. Division (/)\n",
            "5. Square Root (√)\n",
            "6. Exponentiation (^)\n",
            "7. Logarithm (log)\n",
            "8. Sine (sin)\n",
            "9. Cosine (cos)\n",
            "10. Tangent (tan)\n",
            "11. Factorial (!)\n",
            "12. Exit\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "def calculator():\n",
        "    print(\"Welcome to the Scientific Calculator\")\n",
        "    print(\"Options:\")\n",
        "    print(\"1. Addition (+)\")\n",
        "    print(\"2. Subtraction (-)\")\n",
        "    print(\"3. Multiplication (*)\")\n",
        "    print(\"4. Division (/)\")\n",
        "    print(\"5. Square Root (√)\")\n",
        "    print(\"6. Exponentiation (^)\")\n",
        "    print(\"7. Logarithm (log)\")\n",
        "    print(\"8. Sine (sin)\")\n",
        "    print(\"9. Cosine (cos)\")\n",
        "    print(\"10. Tangent (tan)\")\n",
        "    print(\"11. Factorial (!)\")\n",
        "    print(\"12. Exit\")\n",
        "\n",
        "    while True:\n",
        "        choice = input(\"\\nEnter choice (1-12): \")\n",
        "\n",
        "        if choice == '12':\n",
        "            print(\"Exiting the calculator. Goodbye!\")\n",
        "            break\n",
        "\n",
        "        if choice in ['1', '2', '3', '4', '6']:\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "            if choice == '1':\n",
        "                print(f\"{num1} + {num2} = {num1 + num2}\")\n",
        "            elif choice == '2':\n",
        "                print(f\"{num1} - {num2} = {num1 - num2}\")\n",
        "            elif choice == '3':\n",
        "                print(f\"{num1} * {num2} = {num1 * num2}\")\n",
        "            elif choice == '4':\n",
        "                if num2 != 0:\n",
        "                    print(f\"{num1} / {num2} = {num1 / num2}\")\n",
        "                else:\n",
        "                    print(\"Error! Division by zero.\")\n",
        "            elif choice == '6':\n",
        "                print(f\"{num1} ^ {num2} = {num1 ** num2}\")\n",
        "\n",
        "        elif choice == '5':\n",
        "            num = float(input(\"Enter number: \"))\n",
        "            if num >= 0:\n",
        "                print(f\"√{num} = {math.sqrt(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Square root of a negative number is not real.\")\n",
        "\n",
        "        elif choice == '7':\n",
        "            num = float(input(\"Enter number: \"))\n",
        "            if num > 0:\n",
        "                print(f\"log({num}) = {math.log(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Logarithm of non-positive number is not defined.\")\n",
        "\n",
        "        elif choice in ['8', '9', '10']:\n",
        "            angle = math.radians(float(input(\"Enter angle in degrees: \")))\n",
        "\n",
        "            if choice == '8':\n",
        "                print(f\"sin({angle}) = {math.sin(angle)}\")\n",
        "            elif choice == '9':\n",
        "                print(f\"cos({angle}) = {math.cos(angle)}\")\n",
        "            elif choice == '10':\n",
        "                print(f\"tan({angle}) = {math.tan(angle)}\")\n",
        "\n",
        "        elif choice == '11':\n",
        "            num = int(input(\"Enter a non-negative integer: \"))\n",
        "            if num >= 0:\n",
        "                print(f\"{num}! = {math.factorial(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Factorial of negative number is not defined.\")\n",
        "\n",
        "        else:\n",
        "            print(\"Invalid Input! Please choose a number between 1 and 12.\")\n",
        "\n",
        "# Run the calculator\n",
        "calculator()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "w9A55MofNr2e"
      },
      "outputs": [],
      "source": [
        "pip install streamlit\n",
        "streamlit run calculator.py\n",
        "import streamlit as st\n",
        "import math\n",
        "\n",
        "# Streamlit app title\n",
        "st.title(\"Scientific Calculator\")\n",
        "\n",
        "# Dropdown for selecting the operation\n",
        "operation = st.selectbox(\n",
        "    \"Select an operation:\",\n",
        "    [\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\", \"Square Root\", \"Exponentiation\", \"Logarithm\",\n",
        "     \"Sine\", \"Cosine\", \"Tangent\", \"Factorial\"]\n",
        ")\n",
        "\n",
        "# Input fields based on the selected operation\n",
        "if operation in [\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\", \"Exponentiation\"]:\n",
        "    num1 = st.number_input(\"Enter the first number:\", step=1.0, format=\"%.4f\")\n",
        "    num2 = st.number_input(\"Enter the second number:\", step=1.0, format=\"%.4f\")\n",
        "elif operation in [\"Square Root\", \"Logarithm\", \"Factorial\"]:\n",
        "    num1 = st.number_input(\"Enter the number:\", step=1.0, format=\"%.4f\")\n",
        "elif operation in [\"Sine\", \"Cosine\", \"Tangent\"]:\n",
        "    angle = st.number_input(\"Enter the angle in degrees:\", step=1.0, format=\"%.4f\")\n",
        "\n",
        "# Calculate based on operation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Addition\":\n",
        "        result = num1 + num2\n",
        "        st.write(f\"Result: {num1} + {num2} = {result}\")\n",
        "\n",
        "    elif operation == \"Subtraction\":\n",
        "        result = num1 - num2\n",
        "        st.write(f\"Result: {num1} - {num2} = {result}\")\n",
        "\n",
        "    elif operation == \"Multiplication\":\n",
        "        result = num1 * num2\n",
        "        st.write(f\"Result: {num1} * {num2} = {result}\")\n",
        "\n",
        "    elif operation == \"Division\":\n",
        "        if num2 != 0:\n",
        "            result = num1 / num2\n",
        "            st.write(f\"Result: {num1} / {num2} = {result}\")\n",
        "        else:\n",
        "            st.write(\"Error! Division by zero.\")\n",
        "\n",
        "    elif operation == \"Square Root\":\n",
        "        if num1 >= 0:\n",
        "            result = math.sqrt(num1)\n",
        "            st.write(f\"Result: √{num1} = {result}\")\n",
        "        else:\n",
        "            st.write(\"Error! Square root of a negative number is not real.\")\n",
        "\n",
        "    elif operation == \"Exponentiation\":\n",
        "        result = num1 ** num2\n",
        "        st.write(f\"Result: {num1} ^ {num2} = {result}\")\n",
        "\n",
        "    elif operation == \"Logarithm\":\n",
        "        if num1 > 0:\n",
        "            result = math.log(num1)\n",
        "            st.write(f\"Result: log({num1}) = {result}\")\n",
        "        else:\n",
        "            st.write(\"Error! Logarithm of non-positive number is not defined.\")\n",
        "\n",
        "    elif operation == \"Sine\":\n",
        "        result = math.sin(math.radians(angle))\n",
        "        st.write(f\"Result: sin({angle}°) = {result}\")\n",
        "\n",
        "    elif operation == \"Cosine\":\n",
        "        result = math.cos(math.radians(angle))\n",
        "        st.write(f\"Result: cos({angle}°) = {result}\")\n",
        "\n",
        "    elif operation == \"Tangent\":\n",
        "        result = math.tan(math.radians(angle))\n",
        "        st.write(f\"Result: tan({angle}°) = {result}\")\n",
        "\n",
        "    elif operation == \"Factorial\":\n",
        "        if num1 >= 0 and num1 == int(num1):\n",
        "            result = math.factorial(int(num1))\n",
        "            st.write(f\"Result: {int(num1)}! = {result}\")\n",
        "        else:\n",
        "            st.write(\"Error! Factorial of negative or non-integer number is not defined.\")\n",
        "streamlit run calculator.py\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/XBRYiY2iRw8A1CKNZtQm",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}