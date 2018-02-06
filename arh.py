import os
import shutil

for foldernames in os.listdir(path= r'\\10.56.141.46\d$\NET1\АРХИВ_СКАН'):
    #print(foldernames+'\n')
    print(foldernames+'\n')
    file_handler = open("D:\\с диска S\log.txt", "a")
    file_handler.write(foldernames+'\n')
    #тут надо производить запись либо в конце
    a = foldernames[:5]
    b = foldernames[6:13]
    #с = a + b + foldernames[14:]
    #формируем путь
    if a != foldernames[:5]:
        a = foldernames[:5]
    if b != foldernames[6:13]:
        b = foldernames[6:13]
    path1 = r'\\10.56.141.46\d$\NET1\АРХИВ_СКАН'+'\\'+ foldernames
    path = r'\\10.56.141.46\d$\NET1\АРХИВ_СКАН'+'\\'+ a +'\\'+ a+'_'+b+'\\'+foldernames
    #shutil.copytree(str(path1), str(path))
    shutil.move(str(path1), str(path)) 
        #print(foldernames[:5]+'-a '+foldernames[7:13]+'-b '+foldernames[14:]+'\n')
        #shutil.copytree('D:\\с диска S\jobi', 'D:\\с диска S\jobnew\'+'str(a)')
    file_handler.close()  
        
