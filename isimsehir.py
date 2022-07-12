#Sırayla kullanıcıdan iki adet şehir girilir. Girilen ilk şehrin son karakteri ile diğerinin 
# ilk karakteri uyumluysa bunu bozana kadar devam eden bir şehir oyunu python ile yazınız. 
#NOT: Kuralı bozan şehir dışında diğer şehirleri listeye yazdırın. Kuralı bozan şehri ayrı olarak gösterin

liste = []
se1 = input("Şehir Adı giriniz:  ")
se2 = input ("Diger Şehri Giriniz:  ") 
if(se1[-1] == se2[0] ):
       liste.append(se1)
       liste.append(se2)
       while (True):
        se3 =input("Yeni Şehir Giriniz:  ")
        if(se2[-1] == se3[0] ):
             se4 =se3
             se2 =se4
            
             liste.append(se3)
        else:
          print()
          print("Dongüyü bozan şehir  :",se3)
          print(liste)
          exit(0)   
else:
    print()
    print("Dongüyü bozan şehir  :",se2)   
    exit(0)