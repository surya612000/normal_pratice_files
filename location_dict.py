import csv


csv_file_path="/home/surya/Downloads/PincodeDetails.csv"

k={}

with open(csv_file_path,mode="r") as file:
    file_reader=csv.reader(file)
    next(file_reader,None)
    for a in file_reader:
        k[a[0]]=a[1] 
print(k)