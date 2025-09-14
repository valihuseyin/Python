# range :Belirlenen sınırlar dahilinde liste oluşturur. 
r = range(20)
print(range(20))
#range(0,20)
lst = list(r) #0  dahil başlanır, 19 dahil biter, 20 tane eleman oluşturur.
print(lst)
#range(baslamadegeri,bitisDegeri,artisDegeri)
print(list(range(3,33,3)))
for  val in list(range(3,33,3)):
	print(val)

