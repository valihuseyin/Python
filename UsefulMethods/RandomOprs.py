# Random Rastgele br veri üretimi i,çin gelen bir modül olup import ile çalışmaya dahil ederiz. 
#rastgele sayı üretme :randint
from random import randint

print(randint(9,100))
#  choice verilen listeden rastgele eleman secimi yapar.
from random import choice

lst =[1,2,4,1.56,"Huseyin"]
print(choice(lst))
#shuffle :listenin elemanları karıştırır

from random import shuffle
print(lst)
shuffle(lst)
print(lst)