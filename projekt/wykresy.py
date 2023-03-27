import chardet as chardet
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('display.max_columns', None)

headlines = ("glebokosc", "numer_ukladanki", "strategia", "piorytet", "dlugosc_rozw", "odwiedzone", "przetworzone", "max_rekurencja", "czas")
with open('wszystkiedane.csv', 'rb') as f:
    enc = chardet.detect(f.read())
f.close()

df = pd.read_csv("wszystkiedane.csv", encoding=enc['encoding'], delimiter=' ', names = headlines)

#grouping of dataframe against relevant criteria
dfs = df.loc[df["strategia"] == "dfs"]
bfs = df.loc[df["strategia"] == "bfs"]
astr = df.loc[df["strategia"] == "astr"]

bfs_rdul = bfs.loc[bfs["piorytet"] == "rdul"]
bfs_rdlu = bfs.loc[bfs["piorytet"] == "rdlu"]
bfs_drul = bfs.loc[bfs["piorytet"] == "drul"]
bfs_drlu = bfs.loc[bfs["piorytet"] == "drlu"]
bfs_ludr = bfs.loc[bfs["piorytet"] == "ludr"]
bfs_lurd = bfs.loc[bfs["piorytet"] == "lurd"]
bfs_uldr = bfs.loc[bfs["piorytet"] == "uldr"]
bfs_ulrd = bfs.loc[bfs["piorytet"] == "ulrd"]

dfs_rdul = dfs.loc[dfs["piorytet"] == "rdul"]
dfs_rdlu = dfs.loc[dfs["piorytet"] == "rdlu"]
dfs_drul = dfs.loc[dfs["piorytet"] == "drul"]
dfs_drlu = dfs.loc[dfs["piorytet"] == "drlu"]
dfs_ludr = dfs.loc[dfs["piorytet"] == "ludr"]
dfs_lurd = dfs.loc[dfs["piorytet"] == "lurd"]
dfs_uldr = dfs.loc[dfs["piorytet"] == "uldr"]
dfs_ulrd = dfs.loc[dfs["piorytet"] == "ulrd"]

astr_hamm = astr.loc[astr["piorytet"] == "hamm"]
astr_manh = astr.loc[astr["piorytet"] == "manh"]


#calculation of average values for the relevant criterion

criterion = "czas"

dfs2 = dfs.groupby("glebokosc")[criterion].mean()
bfs2 = bfs.groupby("glebokosc")[criterion].mean()
astr2 = astr.groupby("glebokosc")[criterion].mean()

dfs_log = np.log10(dfs2)
bfs_log = np.log10(bfs2)
astr_log = np.log10(astr2)

bfs_rdul2 = bfs_rdul.groupby("glebokosc")[criterion].mean()
bfs_rdlu2 = bfs_rdlu.groupby("glebokosc")[criterion].mean()
bfs_drul2 = bfs_drul.groupby("glebokosc")[criterion].mean()
bfs_drlu2 = bfs_drlu.groupby("glebokosc")[criterion].mean()
bfs_ludr2 = bfs_ludr.groupby("glebokosc")[criterion].mean()
bfs_lurd2 = bfs_lurd.groupby("glebokosc")[criterion].mean()
bfs_uldr2 = bfs_uldr.groupby("glebokosc")[criterion].mean()
bfs_ulrd2 = bfs_ulrd.groupby("glebokosc")[criterion].mean()

dfs_rdul2 = dfs_rdul.groupby("glebokosc")[criterion].mean()
dfs_rdlu2 = dfs_rdlu.groupby("glebokosc")[criterion].mean()
dfs_drul2 = dfs_drul.groupby("glebokosc")[criterion].mean()
dfs_drlu2 = dfs_drlu.groupby("glebokosc")[criterion].mean()
dfs_ludr2 = dfs_ludr.groupby("glebokosc")[criterion].mean()
dfs_lurd2 = dfs_lurd.groupby("glebokosc")[criterion].mean()
dfs_uldr2 = dfs_uldr.groupby("glebokosc")[criterion].mean()
dfs_ulrd2 = dfs_ulrd.groupby("glebokosc")[criterion].mean()

astr_hamm2 = astr_hamm.groupby("glebokosc")[criterion].mean()
astr_manh2 = astr_manh.groupby("glebokosc")[criterion].mean()

#define the bar width
bar_width = 0.25
bar_width1 = 0.085
bar_width2 = 0.5

#create the x-axis tick labels
xticklabels = ['1', '2', '3', '4', '5', '6', '7']

#create the figure and axes
fig, ax = plt.subplots(figsize=(7, 5))

#plot the bars for data frames (exercise 1)
#ax.bar(np.arange(len(dfs2)), dfs2.values, width=bar_width, align="center", label="DFS")
#ax.bar(np.arange(len(bfs2)) + bar_width, bfs2.values, width=bar_width, align="center", label="BFS")
#ax.bar(np.arange(len(astr2)) + 2*bar_width, astr2.values, width=bar_width, align="center", label="A*")

#plot the bars for data frames (exercise 2 and 3)
#ax.bar(np.arange(len(bfs_rdul2)), bfs_rdul2.values, width=bar_width1, align="center", label="RDUL")
#ax.bar(np.arange(len(bfs_rdlu2)) + bar_width1, bfs_rdlu2.values, width=bar_width1, align="center", label="RDLU")
#ax.bar(np.arange(len(bfs_drul2)) + 2*bar_width1, bfs_drul2.values, width=bar_width1, align="center", label="DRUL")
#ax.bar(np.arange(len(bfs_drlu2)) + 3*bar_width1, bfs_drlu2.values, width=bar_width1, align="center", label="DRLU")
#ax.bar(np.arange(len(bfs_ludr2)) + 4*bar_width1, bfs_ludr2.values, width=bar_width1, align="center", label="LUDR")
#ax.bar(np.arange(len(bfs_lurd2)) + 5*bar_width1, bfs_lurd2.values, width=bar_width1, align="center", label="LURD")
#ax.bar(np.arange(len(bfs_uldr2)) + 6*bar_width1, bfs_uldr2.values, width=bar_width1, align="center", label="ULDR")
#ax.bar(np.arange(len(bfs_ulrd2)) + 7*bar_width1, bfs_ulrd2.values, width=bar_width1, align="center", label="ULRD")

#plot the bars for data frames (exercise 4)
ax.bar(np.arange(len(astr_hamm2)), astr_hamm2.values, width=bar_width, align="center", label="Hamming")
ax.bar(np.arange(len(astr_manh2)) + bar_width, astr_manh2.values, width=bar_width, align="center", label="Manhattan")

#set the x-axis tick locations and labels
ax.set_xticks(np.arange(len(dfs2)) + 0.11)
ax.set_xticklabels(xticklabels)

#set the y-ticks
plt.yticks(np.arange(0, 1.2, 0.1))
#ytickslabels = ['10^0','10^1','10^2','10^3','10^4','10^5','10^6']
#ax.set_yticklabels(ytickslabels)
#ax.set_yscale('log')

#set the x-axis and y-axis labels
ax.set_xlabel("Głębokość rozwiązania")
ax.set_ylabel("Czas trwania procesu obliczeniowego w ms")

#set the legend and title
#ax.legend(bbox_to_anchor=(0.96, 1.1), loc='upper left', borderaxespad=0.)
ax.legend()
plt.title("A*")

#show the plot
plt.show()






