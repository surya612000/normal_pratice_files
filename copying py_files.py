

from ironpdf import *

import sys
import os

source_file_path_name=sys.argv[1]


destination_file_path_name=sys.argv[2]

dir_list = os.listdir(source_file_path_name)



result_files=[]

for a in dir_list:
    p=os.path.splitext(a)
    p=list(p)
    if p[-1]==".pdf":
        result_files.append(a)



# with open(destination_file_path_name, 'w') as fp:
#     for a in result_files:
#         fp.write(a)

# /home/surya/Desktop/sample_folder

print(result_files)

for path, dirs,files in os.walk(destination_file_path_name):
    for file_name in result_files:
        p=os.path.join(path, file_name)
        des_file = open(p, 'w')
        k=open(f'{source_file_path_name}/{file_name}','r')
        for j in k:
            des_file.write(j)


des_file.close()
k.close()



        
        

    

