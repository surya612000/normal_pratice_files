import csv
import random
import string
from faker import Faker



csv_file_path = "/home/surya/Documents/common_practice1.csv"


product = ["ACE1", "Quick1", "Prudent", "GEM", "KV", "KP"]
mode = ["ATA", "ATD", "DTA", "DTD"]
weight_divisor = [6000, 5000, 4500, 3600, 2700]
payment_mode = ["Cash", "Credit/debit card", "Credit"]
required_temperature = ["-20°C", "2-8°C", "15-25°C"]

le=[]
br=[]


max_rows = int(input())



data_lists = {
    "Product": product[random.randint(0,len(product)-1)],
    "Mode": mode[random.randint(0,len(mode)-1)],
    "weight_divisor": weight_divisor[random.randint(0,len(weight_divisor)-1)],
    "payment_mode": payment_mode[random.randint(0,len(payment_mode)-1)],
    "required_temperature": required_temperature[random.randint(0,len(required_temperature)-1)],
    "length": random.randint(1,90),
    "breadth": random.randint(1,90),
    "height": random.randint(1,90),
    "no_of_packages": random.randint(1,30),  
    "weight_per_package": random.randint(1,30)
}




fake = Faker()




def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters, k=length))




def generate_random_integer(min_val, max_val):
    return random.randint(min_val, max_val)



def calculate_volume_weight(length, breadth, height, no_of_packages, weight_divisor, weight_per_package):
    if weight_divisor == 0:
        return 0  
    else:
        return (length * breadth * height * no_of_packages) // weight_divisor

def calculate_total_weight( weight_per_package,no_of_packages):
    return no_of_packages * weight_per_package

def calculate_chargeable_weight(volume_weight, total_weight):
    return max(volume_weight, total_weight)

def calculate_total_chargeable_weight(volume_weight,total_weight):
    return max(volume_weight,total_weight)






header_functions = {
    "consignment_no": " ",
    "id": generate_random_integer(1, 200),
    "last_name": fake.name(),
    "email_id": fake.email(),
    "first_name": fake.name(),
    "address": fake.address(),
    "consignment_type": "GCD",
    "consignment_subtype": "General",
    "weight_units": "kg",      
    "currency": "inr",
    "invoice_reference_no": generate_random_string(10),
    "consignment_value": " ",
    "remarks": generate_random_string(10),
    "dimension_units": "cms",
    "volume_weight": calculate_volume_weight,
    "total_weight": calculate_total_weight,
    "chargeable_weight": calculate_chargeable_weight(data_lists["volume_weight"],data_lists["total_weight"]),
    "total_chargeable_weight": calculate_total_chargeable_weight(data_lists["volume_weight"],data_lists["total_weight"]),
}





for header, func in header_functions.items():
    if header not in data_lists:
        if callable(func):  
            if  header=="volume_weight":
                data_lists[header] = [func(data_lists["length"], data_lists["breadth"], data_lists["height"],
                                           data_lists["no_of_packages"], data_lists["weight_divisor"], data_lists["weight_per_package"])]
            elif header=="total_weight":
                data_lists[header]=[func(data_lists["weight_per_package"],data_lists["no_of_packages"])]
            elif header=="chargeable_weight":
                data_lists[header]=[func(data_lists["volume_weight"],data_lists["total_weight"])]
            elif header == "total_chargeable_weight":
                data_lists[header] = [func(data_lists["volume_weight","total_weight"])]
            else:
                data_lists[header]=func()
                
        else:
            data_lists[header] = [func for _ in range(max_rows)]


with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data_lists.keys())

    for row in data_lists.values():
        print(row)




