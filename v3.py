import matplotlib.pyplot as plt 
kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

plt.plot(kunlar,ali,color="blue",marker="o",label="ali")
plt.plot(kunlar,vali,color="yellow",marker="*",label="vali")
plt.grid(True)
plt.title("ikki odam natijasi")
plt.legend()
plt.show()