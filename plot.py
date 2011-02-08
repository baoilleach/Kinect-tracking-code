from pylab import *

data = [[], [], []]
for line in open("tmp.txt", "r"):
    t = eval(line)
    for i in range(3):
        data[i].append(t[i])

for i in range(3):
    subplot(310 + i)
    plot(data[i][500:2000])
show()
    
