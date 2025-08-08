import numpy as np
import pandas as pd

# การใช้ DataFrame ของ Pandas

# pd_data = [ [10,50,80,567],
#             [5,25,75,432],
#             [15,30,60,777],
#             [10,40,70,555]]

# df = pd.DataFrame(pd_data,
#                     index = list('ABCD'),
#                     columns=['One','Two','Three','Four'])

# print(df)
# OUTPUT
#    One  Two  Three  Four
# A   10   50     80   567
# B    5   25     75   432
# C   15   30     60   777
# D   10   40     70   555


# อีกแบบ

# data = {'Col1':[110,111,112,113],
#         'Col2':[210,211,212,213],
#         'Col3':[310,311,312,313]}
# df = pd.DataFrame(data, index =['p1','p2','p3','p4'])

# print(df) 
# # OUTPUT :
#     Col1  Col2  Col3
# p1   110   210   310
# p2   111   211   311
# p3   112   212   312
# p4   113   213   313
