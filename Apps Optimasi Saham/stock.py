# Load package
import pandas_datareader
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data

# Mengakses harga saham
dataFrame = data.DataReader(
    ['APLN.JK', 'PWON.JK'],
    'yahoo',
    start='2021/01/01',
    end='2022/01/01'
)

# # Uncomment baris dibawah untuk menampilkan
# # seluruh dataframe saham
# print(dataFrame)

# Mengakses harga saham, hanya mengambil harga closing saja
hargaClosing = dataFrame['Close']
print(hargaClosing)