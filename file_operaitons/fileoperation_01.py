# first file operaitons
#create file and wirte sth. in it

f = open("file_test_101.txt","w+")
f.write("Hi, this is  my first text file in python.")
f.close()

#open file read 
f = open("file_test_101.txt","r")
data =f.read()
f.close()
print(data)

