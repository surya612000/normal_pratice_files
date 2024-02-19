# import csv
# import random
# import copy
import itertools
from datetime import datetime,timedelta

# importing datetime


# importing timezone from pytz module
from pytz import timezone,country_timezones
# # list_of_lists = [[[{"g1": "v1", "g2": "v2"},{"p1": "v3", "p4": "v4"}],[(5,9,8,7,4,6),
# #             {"name":"surya","email":"surya612000@gmail.com","phone":9133437789}]],[[{"x1": "v9", "x2": "v10"},{"m1": "v11", "m2": "v12"}]]]

# # csv_file_path="/home/surya/Downloads/ganesh_cs.csv"


# list_of_lists=[[[{"g":"v","g1":"v"},{"g1":"v1","g2":"v2"}],[(1,2,3,4),(1,2,3,4)]],
#                [[(1,2,3,4,5,6),(7,8,9,0)],[{"name":"surya","profession":"software developer"}]],
#                [[("surya","manam"),("suyra","manma")],[{"g":"v","gl":"0"}]]]


# p=[1,2,3,4]
# q=[5,6,7,8]


# k=itertools.product("abc",repeat=2)
# print(k)


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
#                 list_of_lists2[a][q][w]=generate_random_list()
#             else:
#                 print(str(list_of_lists[a][q][w]),"Other datatypes items")


# print(list_of_lists)
# print(list_of_lists2)







# multi_nested_list = [[["surya" for i in range(4)] for j in range(4)] for k in range(4)]


# multi_nested_list2=[[[multi_nested_list[k][j][i] for i in range(4)]for j in range(4)] for k in range(4)]

# print(multi_nested_list)

#date===========================================================15/2/24================================================

#program to count the items based on the datatype and then store those items in there datatypes


# count_od_dict={}
# count_of_list=0
# count_of_tuple=0

# for a in list_of_lists:
#     for q in a:
#         for w in q:
#             if isinstance(w,dict):
#                 count_od_dict["dictvalues"]=w
#             elif isinstance(w,list):
#                 count_of_list+=1
#             elif isinstance(w,tuple):
#                 count_of_tuple+=1
#             else:
#                 pass

# print("count_of_dict: ",str(count_od_dict)+"\n","count_of_list:",str(count_of_list)+"\n")

#program to miantain items in dictionary with the format item as a key and the index of the item as the value

indexs_of_items={}

# for a in range(len(list_of_lists)):
#     for q in range(len(list_of_lists[a])):
#         for w in range(len(list_of_lists[a][q])):
#             if isinstance(list_of_lists[a][q][w],dict):
#                 for z,x in list_of_lists[a][q][w].items():
#                     indexs_of_items[(z,x)]=(str(a),str(q),str(w))
#             elif isinstance(w,tuple):
#                 for z in list_of_lists[a][q][w]:
#                     indexs_of_items[z]=(str(a),str(q),str(w))
                
#                 # print(str(list_of_lists[a][q][w]),"Other datatypes items")

        

# print(indexs_of_items)


#program to append all the elements into there datatypes 



# items_of_tuples=[]


# for a in range(len(list_of_lists)):
#     for q in range(len(list_of_lists[a])):
#         for w in range(len(list_of_lists[a][q])):
#             if isinstance(list_of_lists[a][q][w],dict):
                
#                 indexs_of_items.update(list_of_lists[a][q][w])
#             elif isinstance(list_of_lists[a][q][w],tuple):
#                 # for z in list_of_lists[a][q][w]:

#                 items_of_tuples.append(list_of_lists[a][q][w])
                
#                 # print(str(list_of_lists[a][q][w]),"Other datatypes items")

# print(indexs_of_items)
# print(items_of_tuples)


#program to iterate over the list items

# k=(list(itertools.chain.from_iterable(list_of_lists)))


# print(len(k))
# print(k)



# for a in range(3):
#     sudlayer=[]
#     for q in range(3):
#         k=list(map(int,input().split(" ")))
#         sudlayer.append(k)
#     list_of_lists.append(sudlayer)
        
# k=list(map(int,input().split(" ")))
# print(k)


#program to transpose the matrix

# list_of_lists=[[[12, 85, 20], [74, 95, 70], [45, 25, 40]], [[85, 96, 30], [95, 15, 80], [25, 75, 50]], [[20, 30, 10], [70, 80, 90], [40, 50, 60]]]
# list_of_lists2=copy.deepcopy(list_of_lists)






# for a in range(3):
#     for q in range(3):
#         for e in range(3):
            
#             list_of_lists2[a][q][e]=list_of_lists[a][e][q]



# print(list_of_lists)

# print(list_of_lists2)


#program if we have the multi dimensional values like this give below
 

# k=[[[{"a":{"b":"c","d1":"c1"},"b":{"b1":"c1","d2":"c2"}}],[{"a1":{"b2":"c2","d5":"c5"},"b1":{"b4":"c4","d6":"c6"}}]],[[{"a":{"b":"c","d1":"c1"},"b":{"b1":"c1","d2":"c2"}}],[{"a1":{"b2":"c2","d5":"c5"},"b1":{"b4":"c4","d6":"c6"}}]]]


# for a in k:
#     for w in a:
#         for e in  w:
#             o=e.values()
#             # for q,x in o.items():
#             #     print(q,x)
#             for y in o:
#                 for i,j in y.items():
#                     print(i,j)




#program to 



















#program on matrix 

# matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]


# class Solution:

#     def __init__(self,matrix,target):
#         self.matrix=matrix
#         self.target=target

#     def searchMatrix(self, matrix, target):
#         for a in matrix:
#             for q in a:
#                 if q==target:
#                     return True
#         return False

# target=1000

# a=Solution(matrix,target)


# p=a.searchMatrix(matrix,target)

# print(p)




# p=[[[1,2,3,4],[2,3,4,5]],[[5,6,7,8],[9,8,7,6]]]

# for a in p:
#     for w in a:
#         # for t in w:
#         print(w)



# p=[]

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



# k="I have 2 cars and 3 bikes"

# location={}
# p=[]

# for a in k:
#     if a.isdigit():
#         p.append(a)
        
#         location[k.index(a)]=a


# o=len(p)-1
# for a,j in location.items():
#     k=k[:a]+p[o]+k[a+1:]
#     o-=1

# print(k)


#program to access the dict values which are also dictionaries



# def func_for_print(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print(key, value)
#             func_for_print(value)
#     elif isinstance(data, list):
#         for item in data:
#             func_for_print(item)



# for item in k:
    # func_for_print(item)





# p="321"
# k="654"

# carry=0
# for a in k:
#     a=int(a)
#     carry=int(carry)
#     for w in p:
#         w=int(w)
#         # print(carry)
#         q=(a*w)+int(carry)
#         carry=0
#         q=str(q)
#         carry=q[0]
#         print(q[-1])


# k=list(map(int,input().split(" ")))
# p=int(input("Enter Index that you want to del"))


# k=k[:p]+k[p+1:]
# print(k)







# index_for_del=list(map(int,input().split(" ")))

# element=k[index_for_del[0]][index_for_del[1]][index_for_del[2]]

# k.delete(element)

# element1=k[index_for_del[0]][index_for_del[1]][index_for_del[2]]

# print(element1)



#rotate the list


# k=list(map(int,input().split(" ")))

# rotate=int(input())
# no_of_place_shift=rotate%len(k)


# sub_list=k[-no_of_place_shift:]

# attached_list=[]


# attached_list=k[:len(k)-no_of_place_shift]

# if(rotate==len(k)):
#     print(sub_list)
# else:
#     print(sub_list+attached_list)




#partition list



# k=list(map(int,input().split(" ")))

# enter_the_value=int(input())

# small_ele=[]
# order_ele=[]

# for a in k:
#     if a<enter_the_value:
#         small_ele.append(a)
#     else:
#         order_ele.append(a)

# print(small_ele+order_ele)


#program on reordering



# k=list(map(int,input().split(" ")))

# p=k[::-1]

# reorder=[]
# reorder_index=0
# normal_index=0

# for a in range(1,len(k)+1):
#     if(a%2==0):
#         reorder.append(p[reorder_index])
#         reorder_index+=1
#     else:
#         reorder.append(k[normal_index])
#         normal_index+=1

# print(reorder)





#program to identify the 























#program on the multi dimensional list




# k=list(map(int,input().split(" ")))


# pos=int(input())

# if(len(k)==0 or pos<0):
#     print("no cycle")

# else:
#     print("tail connects to node index {}".format(pos))


#programs on timedeta things

# p=timedelta(days=1,hours=12,seconds=120)

# print(datetime.now()+p)

# k=int(input())

# p=k%60

# no_of_minutes=timedelta(minutes=p)

# print(datetime.now()+no_of_minutes)


# format = "%Y-%m-%d %H:%M:%S %Z%z"

# converted_tz = pytz.timezone('US/Eastern')
# # print(pytz.all_timezones)
# # print("===============================================================================================")
# # print(pytz.country_timezones("US"))
# # print("===============================================================================================")
# # print(pytz.country_timezones("Indian"))




# # utc_now=datetime.now(timezone("UTC"))

# # now_asia = utc_now.astimezone(timezone('Asia/Kolkata'))

# # p


# current_time_us=datetime.now(converted_tz)





# print(current_time_us)











k=datetime.now()

print(k)

p=k.astimezone(country_timezones())

print(p)




