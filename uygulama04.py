__author__ = "Aslı Batırbaygil"

kadinadi = input("Bir kadın adı giriniz...:")
erkekadi = input("Bir erkek adı giriniz...:")
misra    = int(input("Mısra sayısı giriniz...Maksimum 14 mısra yazdırılabilir.."))

print("-"*60)

print("")

siir     = [erkekadi + " ceylan gözlü "+ kadinadi +" sırma saçlı", "Al yanaklı, mor sümbüllü " + kadinadi ,"Kalbinden geçen duyguları ifade etmeye sözcükler yetmezdi","Onu görünce pır pır eder yüreği", erkekadi + " naif " + kadinadi + " özler hep temiz duyguları","Çakmak çakmak bakan " + kadinadi + ", daha önce hiç sevilmemişcesine","Çok yüce sever.", "Konuşulmayan duygular daha güzeldir. " + kadinadi + " özledikçe",erkekadi + " zeki " + kadinadi + " sever,","Sırılsıklam aşık, sevmek ne kelime, delicesine,","Hep nazı geçen,","Çok yüce sever,","Yanıp tutuşmalı belki de,","Ecel gelip ayırsa bir gün " + kadinadi + "  yarini hiç unutur mu?"]

for olusturulacak_siir in siir[:misra]:
    print(olusturulacak_siir)

print("")

print("-"*60)

if misra > 14:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 14") # 14 den büyük bir değer girildiğinde 14 mısraya kadar yazdırıldığı için her zaman 14 yazacak.

else:
    print("Yazdırılan mısra sayısı:", misra)

