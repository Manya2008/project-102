import os
import shutil

source = "G:/My Drive/pleasures/coding/coding(whitehat)/projects/Project102"
desination1 = "C:/Users/Manya Manikandan/Documents/document_files"
desination2 = "C:/Users/Manya Manikandan/Documents/image_files"

files = os.listdir(source)
#print(files)

for file_name in files :
    name,extension = os.path.splitext(file_name)
    #print(name,extension)
    if extension == '':
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path_1 = source + '/' + file_name
        path_2 = desination1
        path_3 = desination1 + '/' + file_name
        
        #print(f"path 1: {path_1}" )
        #print(f"path 3: {path_3}" )
        
        if os.path.exists(path_2):
            print("Moving " + file_name + ".....")

            # Move from path1 ---> path3
            shutil.move(path_1, path_3)

        else:
            os.makedirs(path_2)
            print("Moving " + file_name + ".....")
            shutil.move(path_1, path_3)

    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path_1 = source + '/' + file_name
        path_2 = desination2
        path_3 = desination2 + '/'+ file_name
        
        #print(f"path 1: {path_1}" )
        #print(f"path 3: {path_3}" )
        
        if os.path.exists(path_2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path_1, path_3)

        else:
          os.makedirs(path_2)
          print("Moving " + file_name + ".....")
          shutil.move(path_1, path_3)
    