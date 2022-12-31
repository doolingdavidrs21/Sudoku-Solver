import re
import streamlit as st
import pandas as pd
import numpy as np
from board import normal_board, six_board, matrix_to_df
from solve_sudoku import solve_sudoku_, input_valid, output

style = """
<style>

div[class*="stSelectbox"] label {
  font-size: 20px;
}

div[class*="stTextArea"] label {
  font-size: 20px;
}
</style>
"""
st.write(style, unsafe_allow_html=True)


st.title("Sudoku Solver")

type = st.selectbox(
    'Select the type of Sudoku to be solved',
    ('Normal','6X6')
)

if (type == 'Normal'):
    board = normal_board
    size=350
    M=9
elif (type == '6X6'):
    board = six_board
    size=300
    M=6

input_data = st.text_area(
    label="Enter the sudoku in the below board", value=board, height=size
)

input = []

for line in input_data.split("\n"):
    if not "-" in line:
        vals = re.findall("[0-M]", line.rstrip())
        val = [int(x) for x in vals]
        input.append(val)

input1 = matrix_to_df(input,M)

if st.button("Solve!"):
    st.header('Solution')
    if (type == 'Normal'):
        msg,check=input_valid(input)
        if(check):
            if(solve_sudoku_(input)):
                st.write(matrix_to_df(input,M))
            else: st.write("Invalid Sudoku!!")
        else: 
            st.write("""### """, msg)
    elif (type == '6X6'):
        pass
else:
    st.header('Board Layout')
    st.write(matrix_to_df(input,M))
