import os

list_dir = os.listdir()

with  open('list_file.txt','a') as file_txt:
    print(list_dir,file=file_txt)
    file_txt.close