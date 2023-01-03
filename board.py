import pandas as pd
import numpy as np

four_board = """\t\t\t\t\t\t\t\t\t\t\t-----------------
\t\t\t\t\t\t\t\t\t\t\t|  0  0  |  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t|  0  0  |  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t-----------------
\t\t\t\t\t\t\t\t\t\t\t|  0  0  |  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t|  0  0  |  0  0  | 
\t\t\t\t\t\t\t\t\t\t\t-----------------"""

six_board = """\t\t\t\t\t\t\t\t\t\t\t----------------------
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t----------------------
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  | 
\t\t\t\t\t\t\t\t\t\t\t----------------------
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  | 
\t\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  
\t\t\t\t\t\t\t\t\t\t\t----------------------"""

nine_board = """ \t\t\t\t\t\t\t\t\t\t---------------------------------
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t---------------------------------
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t---------------------------------
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t|  0  0  0  |  0  0  0  |  0  0  0  |
\t\t\t\t\t\t\t\t\t\t---------------------------------"""

def matrix_to_df(matrix,n):
    df = pd.DataFrame(matrix, columns=np.arange(1, n+1))
    df.index = np.arange(1, n+1)
    return df
