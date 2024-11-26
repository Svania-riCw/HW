# a = ['YP', 'YP', 'RP', 'RP', 'YP', 'YP', 'GU', 'GU', 'OP', 'OP', 'BU', 'BU', 'BP', 'BP', 'YU', 'YU', 'BU', 'RP', 'OP', 'BP', 'GP', 'YP', 'RU', 'OU', 'YU', 'YU', 'YU', 'OU', 'OU', 'OP', 'OP', 'RU', 'RU', 'GU', 'GU', 'YU', 'GP', 'OP', 'RP']
# print(list(map(lambda x: (x[0], x[1]), a)))


# s = "AB"
# print((s[0], s[1]))

# n, p = int(input()), 0
# wishColor, wishPattern = input().split()
# colors, patterns = input(), input()
# turtles = [None] * 9
# removes = []


# def pull_turtles():
#     global p, n
#     for i in range(9):
#         if p >= n or p >= len(colors):
#             return
#         if turtles[i] is None:
#             turtles[i] = (colors[p], patterns[p])
#             p += 1
#             if turtles[i] == (wishColor, wishPattern):
#                 n += 1


# def three_of_kind():
#     global n
#     for i in [0, 1, 2]:
#         n += 5 if (turtles[i] is not None) and len(set(turtles[i:9:3])) == 1 else 0
#     for i in [0, 3, 6]:
#         n += 5 if (turtles[i] is not None) and len(set(turtles[i:i + 3])) == 1 else 0
#     n += 5 if (turtles[4] is not None) and len(set([turtles[i] for i in [0, 4, 8]])) == 1 else 0
#     n += 5 if (turtles[4] is not None) and len(set([turtles[i] for i in [2, 4, 6]])) == 1 else 0


# def pairs():
#     global n
#     mark = False
#     for i in range(8):
#         if turtles[i] is None:
#             continue
#         for j in range(i + 1, 9):
#             if turtles[i] == turtles[j]:
#                 n += 1
#                 removes.append(turtles[i])
#                 removes.append(turtles[j])
#                 turtles[i] = turtles[j] = None
#                 mark = True
#                 break
#     return mark


# while True:
#     flag = False
#     pull_turtles()
#     if (None not in turtles) and len(set(turtles)) == 9:
#         n += 5
#         removes.extend(turtles)
#         turtles = [None] * 9
#         flag = True
#     else:
#         three_of_kind()
#         flag = pairs()
#     if (p >= n or p >= len(colors)) and not flag:
#         break

# print(removes + [i for i in turtles if i is not None])


# list_1 = [1,2,2,2,3,3,4]
# list_2 = [2,3,4]
# list_3 = set(list_1) - set(list_2)
# print(list_3)


# profit = input()
# profit_list = profit.split ()
# float_list = []#浮点数格式的列表
# for i in profit_list:
#     new = float(i)
#     float_list.append(new)
# number = int (input())#问题个数
# def find_min(lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         min_num = lists[0]
#         for num_1 in lists:
#             if num_1 < min_num:
#                 min_num = num_1
#         print (float(min_num)) 
# def find_max(lists):
#     if len(lists)== 0: 
#         print ("Querying on empty list! ")
#     else:
#         max_num = lists[0]
#         for num_2 in lists:
#             if num_2 > max_num:
#                 max_num = num_2
#         print (float(max_num))
# def compute_ave(lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         ave_profit = sum (lists)/len(lists)
#         print (float(ave_profit))
# def compute_all(lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         sum_profit = sum(lists)
#         print (float(sum_profit)) 
# def reorder_asc (lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         asc_lists = sorted(lists)
#         float_list[start:end:step] = asc_lists
#         print (float_list)
# def reorder_desc (lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         desc_list = sorted(lists,reverse=True)
#         float_list[start:end:step] = desc_list
#         print (float_list)
# def reorder_rev(lists):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         rev = reversed (lists)
#         rev_list = list (rev)
#         float_list[start:end:step] = rev_list
#         print (float_list)
# def index_1(lists):
#     index_list = []
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         for i in range(start,end,step):
#             j = int (i) 
#             index_list.append(float(lists[j]))
#         if len(index_list) == 0:
#             print ("Querying on empty list!")
#         else:
#             print (index_list)
# def index_2(lists,i):
#     if len(lists)== 0:
#         print ("Querying on empty list! ")
#     else:
#         i = int (i)
#         if i >= len(lists):
#             print ("Querying on empty list!")
#         else:
#             print (float(lists[i]))
# for i in range(number):
#     order = input()
#     slice_list = []#记录切片情况的列表
#     digit_str = ''
#     count = 0  
#     is_number = False 
#     for char in order:
#         if char.isdigit():
#             if not is_number:
#                 is_number = True
#         else:
#             if is_number:    
#                 count = count + 1   
#                 is_number = False
#     if count >= 2:     
#         for char in order:
#             if char.isdigit()or char == '-' :
#                 digit_str = digit_str + char
#             else:
#                 if digit_str:
#                     slice_list.append(float(digit_str))
#                     digit_str = ''
#         if digit_str:
#             slice_list.append(float(digit_str))
#         start = int (slice_list[0])
#         end = int (slice_list[1])
#         step = int (slice_list[2])
#         if "find, min" in order:
#             find_min (float_list[start:end:step])
#         elif "find, max" in order:
#             find_max (float_list[start:end:step])  
#         elif "compute, avg" in order:
#             compute_ave (float_list[start:end:step])
#         elif "compute, all" in order:
#             compute_all (float_list[start:end:step])
#         elif "reorder, asc" in order:
#             reorder_asc (float_list[start:end:step])
#         elif "reorder, desc" in order:
#             reorder_desc (float_list[start:end:step])
#         elif "reorder, rev" in order:
#             reorder_rev (float_list[start:end:step])
#         elif "index, slice, " in order:
#             index_1(float_list)       
#     else:
#         start = int(0)
#         end = int (len(float_list))
#         step = 1
#         if "find, min" in order:
#             find_min (float_list) 
#         elif "find, max" in order:
#             find_max (float_list)   
#         elif "compute, avg" in order:
#             compute_ave (float_list)
#         elif "compute, all" in order:
#             compute_all (float_list)
#         elif "reorder, asc" in order:
#             reorder_asc (float_list)
#         elif "reorder, desc" in order:
#             reorder_desc (float_list)
#         elif "reorder, rev" in order:
#             reorder_rev (float_list)
#         elif "index, " in order:
#             order_list = order.split(", ")
#             i = int (order_list[1])
#             index_2(float_list,i)




# a = "-1"
# b = a.isdigit()
# print(b)


# a = "1"
# print("\t",id(a))


# def a(i, j=1):
#     return i + j

# print(a(1, 3))


# dict1 = {"name":"ming", "age":18}
# # [print(i) for i in a]
# dict1["height"] = 175
# dict1['name'] = 'xi'
# dict1.update({'age': 20})
# print(dict1)


# tup = (1, 2, [3, 4])
# tup[2][0] = 5
# print(tup)

# a = "golong"
# b = [1, 2, 3, a]
# a = 'python'
# print(b)

# def a(x):
#     if x == 3:
#         return x*2
#     y = x*5
#     return y

# print(a(1))

# if True:
#     pass
# else:
#     print('False')

# letters={'g': 1,'o': 2,'d': 1}
# # print(letters['o'])
# print(letters.keys)
# for letter in letters.keys():
#     # for i in range(letters[letter]):
#         print(letter)

#         print(letter,end = '')#######################     不换行操作！！！！！！！




# ans = 12
# print('ans=' + str(ans))

# L = ['1', '2', '3', '4', "f"]
# print(range(0,4))
# [print(f'{i} ',end = '') for i in L] ########################3打印列表里的所有元素
# test = ', '.join(L)
# print(test)

####################################################    二分法！！！！
# def bisection_root(x, episilon=0.00000001):
#     low = 0
#     high = x
#     guess = (high + low)/2.0
#     while abs(guess**2 - x) >= episilon:
#         if guess**2 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (high + low)/2.0
#     return guess

# print(bisection_root(123,0.5))
###################################################     isinstance 判别法

# a = [1, 2, 3]
# b = isinstance(a,list)
# print(b)

###################################################    python异常处理




# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except:
#     raise ValueError('hhhhhhhhhhh')
#     print('Bug in user input')  ############## 此行代码永远不会输出！！！！！！ raise后面



# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# add_five = outer(5)
# print(outer(5)(10))
# print(add_five(5))


# assert 1==0,'1不等于0'

# def test():
#     try :
#         a = 5.0 / 0.0
#         print('输出：我是try')
#         return 0
#     except :
#         print('输出：我是except')
#         return 1
#     else :
#         print('输出：我是else')
#         return 2
#     finally :
#         print('输出：finally')
# print('test: ',test())
# # 输出：我是except
# # 输出：finally
# # test: 1

#########################################################################

# [print(f'{i} ',end='') for i in range(5)]


# tup1 = (4,5,6),(7,8)
# print(tup1)   #############  ((4, 5, 6), (7, 8))
# tup2 = (1,)
# print(tup2)

# print(list(reversed(range(10))))

# a = (6,7,8)
# b = (1,)
# print(a+b)

# print(1,2,3)

# x=2/3
# print('{:.3f}'.format(x))

# def is_even(x):
#     return x%2 == 0
# print(is_even(10))
# s = 'a, b'
# k = s.split(', ')
# print(k)
# print(''.join(k))

# print(int('F',base=16))


# def is_even(b):
#         if b%2 == 0:
#             return True

# def apply(x,n):
#     a = []
#     for i in range(n+1):
#         if x(i):
#             a.append(i)

#     return a

# print(apply(is_even, 10))




# k = int(input())
# a = 0
# for i in range(1,3**k):
#     a += 1/i
#     if a > k:
#         print(i)
#         break


# s = input().split()
# b = int(input())
# num = 0
# for i in s:
#     if b + 30 >= int(i):
#         num += 1
# print(num)

# s = input().split()
# k = list('0'*10005)
# a = []
# for i in range(int(s[1])):
#     b = input().split()
#     a.append(b)
# for i in range(int(s[1])):
#     for j in range(int(a[i][0]),int(a[i][1])+1):
#         if k[j] == '1':
#             continue
#         if k[j] == '0':
#             k[j] = '1'
# num = 0
# for i in range(10004):
#     if k[i] == '1':
#         num+=1
# num1 = int(s[0])+1 - num
# print(num1)


# s1 = input().split()
# a1 = int(s1[0])+int(s1[1])
# s2 = input().split()
# a2 = int(s2[0])+int(s2[1])
# s3 = input().split()
# a3 = int(s3[0])+int(s3[1])
# s4 = input().split()
# a4 = int(s4[0])+int(s4[1])
# s5 = input().split()
# a5 = int(s5[0])+int(s5[1])
# s6 = input().split()
# a6 = int(s6[0])+int(s6[1])
# s7 = input().split()
# a7 = int(s7[0])+int(s7[1])
# a = [a1,a2,a3,a4,a5,a6,a7]
# b = max(a)

# if b<= 8:
#     print(0)
# else:
#       for i in range(len(a)):
#         if a[i] == b:
#             print(i+1)
#             break

# list1 = [1,2,3]
# list2 = list(reversed(list1))
# list3 = sorted(list1)
# print(list3)



def look(n):
    if n == 0:
        return ""
    
    result = ''
    count = 1
    if len(n) > 1:
        for i in range(len(n)-1):
            if n[i+1] == n[0]:
                count += 1
            else:
                result += str(count-1) + n[0]
                count = 1
        n = [i for i in n if i != n[0]]
    if len(n) == 1:
        result += str(1) + n[0]
    return result
n = input()
look(n)



