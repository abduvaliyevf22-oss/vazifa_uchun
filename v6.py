import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color="green")

plt.title("Do'konning bir haftalik savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.show()

