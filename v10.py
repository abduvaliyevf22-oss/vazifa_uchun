import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="blue")

plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(True)

plt.savefig("oquvchilar_natijasi.png")
plt.show()

eng_kop = max(ballar)
eng_kam = min(ballar)
ortacha = sum(ballar) / len(ballar)

print("Eng yuqori ball:", eng_kop)
print("Eng past ball:", eng_kam)
print("O'rtacha ball:", round(ortacha, 2))
print("Eng yuqori ball olgan:", ismlar[ballar.index(eng_kop)])
print("Eng past ball olgan:", ismlar[ballar.index(eng_kam)])