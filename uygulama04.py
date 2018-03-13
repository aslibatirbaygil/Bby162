__author__ = "Aslı Batırbaygil"

kadinadi = input("Bir kadın adı giriniz...:")
erkekadi = input("Bir erkek adı giriniz...:")
misra    = int(input("Mısra sayısı giriniz...Maksimum 10 mısra yazdırılabilir.."))

print("-"*60)

print("")

siir     = [erkekadi + " ceylan gözlü "+ kadinadi +" sırma saçlı", "Al yanaklı, mor sümbüllü " + kadinadi ,"Kalbinden geçen duyguları ifade etmeye sözcükler yetmezdi","Onu görünce pır pır eder yüreği", erkekadi + " naif " + kadinadi + " özler hep temiz duyguları","Çakmak çakmak bakan " + kadinadi + ", daha önce hiç sevilmemişcesine","Çok yüce sever.", "Konuşulmayan duygular daha güzeldir. " + kadinadi + " özledikçe",erkekadi + " Sırılsıklam aşık, sevmek ne kelime, delicesine " + kadinadi + " Yanıp tutuşmalı belki de,","Ecel gelip ayırsa bir gün " + kadinadi + "  yarini hiç unutur mu?"]

for olusturulacak_siir in siir[:misra]:
    print(olusturulacak_siir)

print("")

print("-"*60)

if misra > 10:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10") # 10'den büyük bir değer girilmesi durumunda, 10 mısraya kadar yazdırıldığından hep 10 yazacak.

else:
    print("Yazdırılan mısra sayısı:", misra)

