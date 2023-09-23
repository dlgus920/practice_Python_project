

def sum_numbers(num1,num2):
    return num1 + num2

def mult_numbers(num1,num2):
    return num1* num2

list_n = []
list_n.append(90)

print(list_n)

a = 1
b = 2
a+=b

print(a)
print(b)

s= "i have{0} pen" .format(a)
s.upper()
print(s.upper())

arr1 =[]
arr2 = []


for i in range(10):
    arr1.append(i)
    
for i in range(10):
    arr2.append(arr1)
    
for i in range(10):
 
    print(arr2[i])
    
    
t1 = (1,2,3,4)

print(t1)

val1 = "Lee"
val2 = "teach"

map_ = {'name':val1,'Roll':val2}

map_["name"] = "me"

def get_listkey(key):
    return map_[key]

def add_listval(key, val):
    if(map_.get(key) != None):
        print('can not add value')
    else:
        map_[key] = val
    
def change_key_value(key, val):
    if(key in map_):
        map_[key] = val
    else:
        print("can not change the value " "key '%s'" %(key))
        
add_listval('name', 'myname')
add_listval('Not_my_name','your_name')
    
print (get_listkey('name'))

change_key_value("x",'x')

print (get_listkey('name'))


list_orggin = [1,2,3,4]
list_replica = list_orggin

list_orggin.append(1)

print(list_replica)

orgin_id = id(list_orggin)
repli_id = id(list_replica)

print(orgin_id)
print(repli_id)

list_replica = list_orggin[:]

list_replica.append(1)

print(list_replica)
orgin_id = id(list_orggin)
repli_id = id(list_replica)
print(orgin_id)
print(repli_id)

print("Git!")

Git_ = True

if(Git_):
    print("Git! sucesss!")