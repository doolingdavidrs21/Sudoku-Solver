import pandas as pd
import numpy as np

normal_board = """ \t\t\t\t\t\t\t\t\t\t---------------------------------
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


def matrix_to_df(matrix,M):
    df = pd.DataFrame(matrix, columns=np.arange(1, M+1))
    df.index = np.arange(1, len(df) + 1)
    return df