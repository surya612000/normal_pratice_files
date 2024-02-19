# import csv
import random
import copy
# list_of_lists = [[[{"g1": "v1", "g2": "v2"},{"p1": "v3", "p4": "v4"}],[(5,9,8,7,4,6),
#             {"name":"surya","email":"surya612000@gmail.com","phone":9133437789}]],[[{"x1": "v9", "x2": "v10"},{"m1": "v11", "m2": "v12"}]]]

# csv_file_path="/home/surya/Downloads/ganesh_cs.csv"


list_of_lists=[[[{"g":"v","g1":"v"},{"g1":"v1","g2":"v2"}],[(1,2,3,4),(1,2,3,4)]],
               [[(1,2,3,4,5,6),(7,8,9,0)],[{"name":"surya","profession":"software developer"}]],
               [[("surya","manam"),("suyra","manma")],[{"g":"v","g2":"0"},{"g1":"v1","g2":"v2"}]]]




# def unpack_dict(a="hi",b="raina"):
#     print(a," ",b)



# data={"a":"surya","b":"raina"}


# unpack_dict(**data)




# p={
#     "name":"surya","roll":20
# }

# k=p

# k["name"]="raina"

# print(k.items())

# p=[]

# for a in range(len(list_of_lists)):
#     for q in range(len(list_of_lists[a])):
#         for w in range(len(list_of_lists[a][q])):
#             if isinstance(list_of_lists[a][q][w],dict):
#                 for z,k in list_of_lists[a][q][w].items():
#                     if z=="g":
#                         list_of_lists[a][q][w].update({"g":"sutya"})
#             else:
#                 print(str(list_of_lists[a][q][w]),"Other datatypes items")



# print(list_of_lists)


# with open(csv_file_path,mode="a") as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(["name","Email","Phone"])



# for a in list_of_lists:
#     for q in a:
#         for w in q:
#             if isinstance(w,dict):
#                 li=[]
#                 for r,l in w.items():
#                     if r=="name" or r=="email" or r=="phone":
#                         li.append(l)
#                         if len(li)==3:
#                             with open(csv_file_path,mode="w") as file:
#                                 csv_writer=csv.writer(file)
#                                 csv_writer.writerow(li)
#                     else:
#                         print("I don't want this dictionary value")
#             elif isinstance(w,tuple):
#                 for r in w:
#                     print(str(r),"tuple")
#             else:
#                 for r in w:
#                     print(str(r),"list")




# print(list_of_lists[0][1][1])



# p=[]
# [p.append(a) for w in list_of_lists for q in w for a in q]

# for a in p:
#     if isinstance(a,dict):
#         print(a)

# # o=[]
    
# p=[]
# # w=0

# def access_fun(list_of_lists):
    
#     for a in list_of_lists:
#         if isinstance(a,list):
#             w=access_fun(a)
#         else:
#             p.append(a)
#     return p






# k=access_fun(list_of_lists)

# for a in k:
#     print(a)



# k={"name":"surya","profession":"software developer"}


# def dict_func(**kws):
#     print(kws)


# dict_func(name="surya",roll=10)

# dict_func()



# k=[[[int(input()) for b in range(4)] for c in range(3)] for w in range(2)]
# print(k)


# list_of_lists2=copy.copy(list_of_lists)


# def generate_random_list():
#     random_list=[]
#     for a in range(4):
#         random_list.append(random.randint(1,6))
#     return random_list




# for a in range(len(list_of_lists)):
#     for q in range(len(list_of_lists[a])):
#         for w in range(len(list_of_lists[a][q])):
#             if isinstance(list_of_lists[a][q][w],dict):
#                 continue
#             else:
#                 print(str(list_of_lists[a][q][w]),"Other datatypes items")


# print(list_of_lists)
# print(list_of_lists2)



# def generate_random():
#     s=[]
#     for a in range(1,4):
#         s.append(random.randint(1,9))
#     return s


# for a in list_of_lists:
#     for w in a:
#         for q in w:
#             if isinstance(q,dict):
#                 q=generate_random()
#                 print(q)
#             elif isinstance(q,tuple):
#                 print(q)


















































































p=[]

# o=[]

# def list_function(list_of_lists):
#     for a in list_of_lists:
#         if isinstance(a,list):
#             p.extend(list_function(a))
#         else:
#             o.append(a)
#     return o,p







# w=list_function(list_of_lists)

# # print(k)
# print(w)



# [p.append(d) for a in list_of_lists for b in a for d in b]

# print(p)'


