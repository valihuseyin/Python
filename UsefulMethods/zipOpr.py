# Zip : birden fazla listeyiindex sırasına göre birleştirmeye yarar 
#indexleri aynı olanalrı aynı gruba koyar temel mantığı budur. 
gunler = ["Pazartesi","Cuma"]
calismaSaatleri=[6,8]
calismaYerleri =["Ofis","Ev"]

outputLst = list(zip(gunler,calismaYerleri,calismaSaatleri))
print(outputLst)