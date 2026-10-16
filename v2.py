from matplotlib import pyplot as plt


fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

plt.plot(ballar,fanlar)
plt.ylabel("ballar")
plt.xlabel("fanlar")
plt.grid(True)
plt.title("fan baholar")
plt.show()