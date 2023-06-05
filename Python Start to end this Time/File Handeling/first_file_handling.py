
fin = open('D:\Python Start to end this Time\File Handeling\countries1.txt', 'w')
fin.write('Pakistan\n')
fin.write('India\n')
fin.write('Japan\n')
fin.close()


fin = open('D:\Python Start to end this Time\File Handeling\countries1.txt','a') 
fin.write('Germany')


fin = open('D:\Python Start to end this Time\File Handeling\countries1.txt','r') 
print(fin.read())

