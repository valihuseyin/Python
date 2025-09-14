# Enumerate : İlgilenen eleman/ların index bilgisini veya bilgilerini listeyeleyen bir metot.
#listeler 0. index ile başlar ve sıra ile devam eder. Enumerate metotdu 0 dan başlayarak sıra ile listeler. 
lst = list(range(0,10))
print(enumerate(lst))
for x in enumerate(lst):
	print(x)

#'-' * 10 -->10 tane - yaz demek ---------
for (index,val) in enumerate(lst):
	print(f"| listemizde {index}.index de bulunan eleman: {val} |")
	print("-_-" * 15)