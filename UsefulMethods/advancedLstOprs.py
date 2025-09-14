# Advanced List Operations : uzun uzun yapılan liste işlemleirni daha kısa ve nalaşılır kodlarla yapmamızı sağlarlar.
# uzun uzun bir string değerini for ile bir lsteye eklemek yerine kısa yol 

elemanlar =[element for element  in "Huseyin_Karadag"]
print(elemanlar)

# DİKKAT elemnt for element buradaki elemnt adlandirmları aynı olmalı 

sonuclar = [num ** 2 for num in list(range(2,10,2))]
print(sonuclar) 
