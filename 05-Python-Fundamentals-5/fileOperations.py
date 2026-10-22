f = open("/Users/devanshshah/Developer/PrimeLab/05-Python-Fundamentals-5/sample.txt", "r") 
data = f.read()
print(data)
print(type(data))
f.close()
print("****")


f2 = open("/Users/devanshshah/Developer/PrimeLab/05-Python-Fundamentals-5/sample.txt", "r") 
data2 = f2.readline()
print(data2)
f2.close()

print("****")

f3 = open("/Users/devanshshah/Developer/PrimeLab/05-Python-Fundamentals-5/sample.txt", "r") 
data3 = f3.readlines()
print(data3)
f3.close()

print("****")

f4 = open("/Users/devanshshah/Developer/PrimeLab/05-Python-Fundamentals-5/sample.txt", "w+")
data4 = f4.write("Hellow Devansh")
print(data4)

f4.seek(0)
sampleText = f4.readline()
print(f"This is the Sample Text -> ",sampleText)
f4.close()