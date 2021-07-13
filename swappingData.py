def swapData() :
	with open("D:/deepthi projects/C98/myfile1.txt","r") as a :
		data_1 = a.read()
		a.close()
	with open("D:/deepthi projects/C98/myfile2.txt","r") as a :
		data_2 = a.read()
		a.close()
	print("Before swapping the data")
	print("file 1 - ",data_1)
	print("file 2 - ",data_2)
	print(" ")
	with open("D:/deepthi projects/C98/myfile1.txt","w") as a :
		print(a.write(data_2))
	with open("D:/deepthi projects/C98/myfile2.txt","w") as a :
		print(a.write(data_1))

def ex():
	
	file1 = open("D:/deepthi projects/C98/myfile1.txt","r+")
	file1_data = file1.read()
	file2 = open("D:/deepthi projects/C98/myfile2.txt","r+")
	file2_data = file2.read()
	print("Before swapping the data")
	print("file 1 - ",file1_data)
	print("file 2 - ",file2_data)
	print(" ")
	file1_writeData = file1.write(file2_data)
	file2_writeData = file2.write(file1_data)
	print("After Swapping The Data")
	print("file 1 - ",file1_writeData)
	print("file 2 - ",file2_writeData)
	file1.close()
	file2.close()

swapData()
