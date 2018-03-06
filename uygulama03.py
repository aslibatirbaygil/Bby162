__author__ = "Aslı Batırbaygil"
#Meyvelerle renklerini gösteren liste ve sözlük

meyveler= ["Elma", "Şeftali", "Muz", "Üzüm", "Ananas", "Çilek"]

print(meyveler)

meyveler_dict  = {"Elma" : "Kırmızı/Yeşil", "Şeftali" : "Turuncu", "Muz" : "Sarı", "Üzüm" : "Mor/Yeşil", "Ananas" : "Sarı", "Çilek" : "Kırmızı"}

print(meyveler_dict)

print("Ananas" in meyveler_dict)

print(meyveler_dict.values())

print(meyveler_dict[input("Meyve yazınız(ilk harf büyük):")])
