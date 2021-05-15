import matplotlib.pyplot as plt
import pandas as pd

# データの読み込み
f = open("j120196_0507_100Hz_実験１.txt", "r")
hoge = pd.read_table(f)
f.close()

hoge.plot()