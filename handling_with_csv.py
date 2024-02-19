from faker import Faker
import csv
import random


no_of_records=int(input("enter the records that you want to create:"))
csv_file_path="/home/surya/Downloads/PincodeDetails.csv"
csv_file_path1="/home/surya/Downloads/ganesh_date.csv"

k={}
s=""

product1 = ["ACE1", "Quick1", "Prudent", "GEM", "KV", "KP"]
mode1 = ["ATA", "ATD", "DTA", "DTD"]
weight_divisor1 = [6000, 5000, 4500, 3600, 2700]
payment_mode1 = ["Cash", "Credit/debit card", "Credit"]
required_temperature1 = ["-20°C", "2-8°C", "15-25°C"]

with open(csv_file_path,mode="r") as file:
    file_reader=csv.reader(file)
    next(file_reader,None)
    for a in file_reader:
        k[a[0]]=a[1]
                         


def generate_pin_code():
    while True:
        pincode = str(random.randint(100000, 999999))
        if pincode in k.keys():
            return pincode 
        else:
            continue

def generate_volume_weight(le,br,he,no,divi):
    k=str((le*br*he*no)/divi)
    v=k[:k.index(".")]
    if(k[k.index(".")+1]=="0"):
        return int(v)
    v=int(v)+1
    return v
    

def generate_random_phone_no():
    s=""
    for _ in range(10):
        s+=str(random.randint(0,9))
    return s
    # else:
    #     for a in range(len(s),12):
    #         s+=str(random.randint(1,9))
    #     return s
    
def generate_reference_no():
    v=""
    for a in range(17):
        k=random.randint(0,9)
        if (k%2==0):
            v+=str(k)
        else:
            h=random.randint(65,90)
            v+=chr(h)
    v=v[:16]
    return v

def generate_consignment_no():
    cons_str=""
    for a in range(11):
        if a==0:
            cons_str+=str(random.randint(1,3))
        else:
            cons_str+=str(random.randint(1,9))
    return cons_str 

def required_temperature_gen(product):
    if product=="KV" or product=="KP":
        return required_temperature1[random.randint(0,(len(required_temperature1)-1))]
    else:
        return 0

csv_file_path = "/home/surya/Downloads/Shipment_Ingestion1.csv" 
csv_file_path1 = "/home/surya/Downloads/ganesh_cs.csv"  
headers_fields=[]
with open(csv_file_path, mode="r", newline="", encoding='ISO-8859-1') as file:
    csv_reader = csv.reader(file)
    for a in csv_reader:
        headers_fields=a
        break

fake = Faker('en_IN')

with open(csv_file_path1,mode="a") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(headers_fields)


data_items=[headers_fields]

p=1
for a in range(no_of_records):
    id=p
    consignment_no=generate_consignment_no()
    first_name=fake.name()
    last_name=fake.name()
    email_id=fake.email()
    phone_no=generate_random_phone_no()
    address=fake.address()
    pincode=generate_pin_code()
    city_name=k[pincode]
    zipcode=pincode
    product=product1[random.randint(0,(len(product1)-1))]
    consignment_type="GCR"
    consignment_subtype="General"
    mode=mode1[random.randint(0,(len(mode1)-1))]
    no_of_packages=random.randint(1,30)
    le=random.randint(1,90)
    br=random.randint(1,90)
    he=random.randint(1,90)
    divi=weight_divisor1[random.randint(0,(len(weight_divisor1)-1))]
    volume=generate_volume_weight(le,br,he,no_of_packages,divi)
    # volume_weight=volume
    weight_units="kg"
    # weight_divisor=divi
    weight_per=random.randint(1,50)
    total_weight=no_of_packages*weight_per
    chargeable_weight=max(round(total_weight),round(volume))
    total_chargeable_weight=max(round(total_weight),round(volume))
    currency="INR"
    invoice_reference_no=generate_reference_no()
    consignment_value=random.randint(1,100000)
    payment_mode=payment_mode1[random.randint(0,(len(payment_mode1)-1))]
    remarks=fake.text()
    
    dimension_units="cms"
    weight_per_package=weight_per
    required_temperature=required_temperature_gen(product)
    p+=1

    every_list=[id,consignment_no,first_name,last_name,email_id,phone_no,address,city_name,zipcode,product,consignment_type,consignment_subtype,mode,no_of_packages,volume,weight_units,divi,total_weight,chargeable_weight,total_chargeable_weight,currency,invoice_reference_no,consignment_value,payment_mode,remarks,le,br,he,dimension_units,weight_per_package,required_temperature]
    with open(csv_file_path1,mode="a") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(every_list)


# print(data_items)

  
