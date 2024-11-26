# mysum = 0
# for i in range(5,11,2):
#     mysum += 1
#     if mysum == 6:
#         break
#         mysum += 1   
# print(mysum)         ##ctrl + / 多行注释

#########

# s = "demo loops-fruit loops"               #找字符串里的字母
# for char in s:
#     if char in "si":
#         print("there is an s or i")

########

# s = "abca"                                    #找不同字母的个数
# seen = ""   #空袋子 集合
# for char in s:
#     if char not in seen: # in 的强大用处
#         seen += char
# print(len(seen))

########

# a = int(input("you give a num:"))          #验证是否为完全平方数
# guess = 0
# while guess**2 < a:
#     guess = guess + 1
# if guess**2 == a:
#     print(a,"is a perfect square,","and its root is",guess)
# else:
#     print(a,"is not a perfect square")

########

# secret = 7
# found = False
# for i in range(1,7):
#     if i == secret:
#         print("yes,it's",i)
#         found = True
# if not found:
#     print("not found")

# secret = 7
# for i in range(1,7):
#     if i == secret:
#         print("yes,it's",i)
#     else:
#         print("not found")           #会输出很多次

# #########

# secret = 7
# for i in range(1,7):
#     while i == secret:
#         print("yes,it's",i)
#     print("not found")  
  
###########

# num = int(input("give me a number:"))    ######二进制和十进制转换，整数形式
# result = ""
# if num == 0:
#     result = "0"
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# print(result)

########

# A = int(input("give me a number1:"))
# B = int(input("give me a number2:"))
# c = A + B
# print(c)

#########

# x = input().split()
# print(int(x[0])+int(x[1]))

#########

# a = int(input())
# b = int(input())
# c = input()
# d = c
# for i in range(a):
#     print(d)
#     d = d + c*b

############                      题1，9.27 第一次作业开始！！！！！！！！！！！

# a = float(input())
# n = abs(int(input()))
# K = abs(int(input()))
# x = 1
# if a < 0:
#     a = abs(a)
# for i in range(K):
#     x = (a + (n-1)*x**n) / (n*x**(n-1))
# x = '{:.10f}'.format(x)
# result = pow(a,1/n)
# print(x)
# y = abs(float(x)-result)/result
# y = '{:.10f}'.format(y)
# print(y)



# a = abs(float(input()))
# n = abs(int(input()))
# K = abs(int(input()))
# x = 1
# for i in range(K):
#     x = (a + (n-1)*x**n) / (n*x**(n-1))
# x = '{:.10f}'.format(x)
# result = a**1/n
# y = abs(float(x)-result)/result
# y = '{:.10f}'.format(y)
# print(x,y,sep = ", ")

##########

# a = float(input())
# n = int(input())
# K = int(input())
# x = 1.0
# for i in range(K):
#     x = (a + (n-1)*x**n) / (n*x**(n-1))
# x = '{:.10f}'.format(x)                      ###########此处把x变成了字符串
# result = a**(1/n)
# y = abs(float(x)-result)/result              ###########此处再把x float会损失精度（虽然原理有点难懂）
# y = '{:.10f}'.format(y)
# print(x,y,sep = ", ")

#############   正解     题2 保留10位小数

# a = float(input())
# n = int(input())
# K = int(input())
# x = 1.0
# for i in range(K):
#     x = (a + (n-1)*x**n) / (n*x**(n-1))
# m = '{:.10f}'.format(x)
# result = a**(1/n)
# y = abs(x-result)/result
# y = '{:.10f}'.format(y)
# print(m,y,sep = ", ")

###############  

# ####把16进制数的每一位加起来，再转换为16进制数，一直重复，直到16进制数只剩个位数  题3    恶心题 debug 8+ hours

# a = input()
# m = len(a)
# z = 0
# for i in range(m):
#     v1 = a[i]
#     num = int(v1 , base = 16)
#     z = z + num
# m1 = hex(int(str(z),10))
# z = m1[2:]
# while len(z) >= 2:
#     z1 = 0
#     m = z
#     t = len(m)
#     for j in range(t):
#         v2 = m[j]
#         num1 = int(v2 , base = 16)
#         z1 = z1 + num1
#     m2 = hex(int(str(z1),10))
#     z = m2[2:]
# print(z1)                             

# q = len(a)
# p1 = "" 
# p2 = "" 
# p3 = ""
# p4 = ""
# for k in range(q):
#     v3 = a[k]
#     g = bin(int(v3,base = 16))
#     ##G1 = g.replace("b","0")
#     G2 = "0000"
#     G = G2 + g[2:]
#     p1 = G[-4] + p1
#     p2 = G[-3] + p2
#     p3 = G[-2] + p3
#     p4 = G[-1] + p4
# s1 = 0
# for char1 in p1:
#     if char1 in "1":
#         s1 += 1
# if s1 % 2 == 1:
#     s1 = 1
# else:
#     s1 = 0

# s2 = 0
# for char2 in p2:
#     if char2 in "1":
#         s2 += 1
# if s2 % 2 == 1:
#     s2 = 1
# else:
#     s2 = 0

# s3 = 0
# for char3 in p3:
#     if char3 in "1":
#         s3 += 1
# if s3 % 2 == 1:
#     s3 = 1
# else:
#     s3 = 0

# s4 = 0
# for char4 in p4:
#     if char4 in "1":
#         s4 += 1
# if s4 % 2 == 1:
#     s4 = 1
# else:
#     s4 = 0

# s1 = str(s1)
# s2 = str(s2)
# s3 = str(s3)
# s4 = str(s4)

# u = s1 + s2 + s3 + s4
# u_change = hex(int(u,base = 2))
# u_16 = u_change[2:].upper()
# print(u_16)

#################

# a = input()
# m = len(a)
# z = 0
# for i in range(m):
#     num = int(a[i] , base = 16)
#     z = z + num
# m1 = hex(int(str(z),10))
# z = m1[2:]
# while len(z) >= 2:
#     z1 = 0
#     m = z
#     t = len(m)
#     for j in range(t):
#         num1 = int(m[j] , base = 16)
#         z1 = z1 + num1
#     m2 = hex(int(str(z1),10))
#     z = m2[2:]
# print(z1)                             

# q = len(a)
# p1 = "" 
# p2 = "" 
# p3 = ""
# p4 = ""
# for k in range(q):
#     g = bin(int(a[k],base = 16))
#     G1 = g.replace("b","0")
#     G2 = "000"
#     G = G2 + G1
#     p1 = G[-4] + p1
#     p2 = G[-3] + p2
#     p3 = G[-2] + p3
#     p4 = G[-1] + p4
# s1 = 0
# for char1 in p1:
#     if char1 in "1":
#         s1 += 1
# if s1 % 2 == 1:
#     s1 = 1
# else:
#     s1 = 0

# s2 = 0
# for char2 in p2:
#     if char2 in "1":
#         s2 += 1
# if s2 % 2 == 1:
#     s2 = 1
# else:
#     s2 = 0

# s3 = 0
# for char3 in p3:
#     if char3 in "1":
#         s3 += 1
# if s3 % 2 == 1:
#     s3 = 1
# else:
#     s3 = 0

# s4 = 0
# for char4 in p4:
#     if char4 in "1":
#         s4 += 1
# if s4 % 2 == 1:
#     s4 = 1
# else:
#     s4 = 0

# s1 = str(s1)
# s2 = str(s2)
# s3 = str(s3)
# s4 = str(s4)

# u = s1 + s2 + s3 + s4
# u_change = hex(int(u,2))
# u_16 = u_change[2:].upper()
# print(u_16)

##################

# a = input()
# m = len(a)
# m2 = a
# z1 = 0
# while m >= 2:
#     for i in range(m):
#         num1 = int(m2[i] , base = 16)
#         z1 = z1 + num1
#     m1 = str(z1)
#     m12 = hex(int(m1,10))
#     m2 = m12[2:].upper()
#     m = len(m2)
#     z1 = 0
# print(m2)                     

############### 手撕异或

# q = len(a)
# p1 = "" 
# p2 = "" 
# p3 = ""
# p4 = ""
# for k in range(q):
#     g = bin(int(a[k],base = 16))
#     G1 = g.replace("b","0")
#     G2 = "000"
#     G = G2 + G1
#     p1 = G[-4] + p1
#     p2 = G[-3] + p2
#     p3 = G[-2] + p3
#     p4 = G[-1] + p4
# s1 = 0
# for char1 in p1:
#     if char1 in "1":
#         s1 += 1
# if s1 % 2 == 1:
#     s1 = 1
# else:
#     s1 = 0

# s2 = 0
# for char2 in p2:
#     if char2 in "1":
#         s2 += 1
# if s2 % 2 == 1:
#     s2 = 1
# else:
#     s2 = 0

# s3 = 0
# for char3 in p3:
#     if char3 in "1":
#         s3 += 1
# if s3 % 2 == 1:
#     s3 = 1
# else:
#     s3 = 0

# s4 = 0
# for char4 in p4:
#     if char4 in "1":
#         s4 += 1
# if s4 % 2 == 1:
#     s4 = 1
# else:
#     s4 = 0

# s1 = str(s1)
# s2 = str(s2)
# s3 = str(s3)
# s4 = str(s4)

# u = s1 + s2 + s3 + s4
# u_change = hex(int(u,2))
# u_16 = u_change[2:].upper()
# print(u_16)

########             异或可以直接操作 如下

# t = len(a)
# q1 = int(a[0],base = 16)
# for j in range(t-1):
#     q1 = q1^int(a[j+1],base = 16)
# q2 = hex(int(str(q1),10))
# q3 = q2[2:].upper()
# print(q3)

#############################################
###########                                            题4大水题 注意list运用 以及  map的运用

# n = int(input())
# list1 = []
# sum_xy = 0
# sum_x = 0
# sum_y = 0
# sum_x2 = 0
# for i in range(n):
#     m1 = input()
#     m2 = list(map(float, m1.split()))
#     sum_x = sum_x + m2[0]
#     sum_y = sum_y + m2[1]
#     sum_x2 = sum_x2 + m2[0]**2
#     sum_xy = sum_xy + m2[0]*m2[1]

# m3 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
# m = '{:.2f}'.format(m3)
# b1 = (sum_y - m3*sum_x) / n
# b = '{:.2f}'.format(b1)
# print(f'y = {m}x + {b}')

###########################     
###############################                         推广版题5

# n = input()
# t = len(n)
# m = t
# list_1 = []
# for i in range(t):
#     for k in range(t-i-1):
#         list_1.append(n[i:i+k+2])
# print(list_1)

# list_2 = []
# for char in list_1:
#     if list_1.count(char) > 1 and char not in list_2:
#         list_2.append(char)
# print(list_2)


# longest_word = ""
# len_1 = 0
# for word in list_2:
#     if len(word) > len_1:
#         longest_word = word
#         len_1 = len(word)
# print(longest_word)

###################                  错误 不知道在干什么

# n = input()
# t = len(n)
# m = t
# list_1 = []
# for i in range(t):
#     for k in range(1,t-i,i+2):
#         list_1.append(n[k-1:i+k+1])


# list_2 = []
# for char in list_1:
#     if list_1.count(char) > 1 and char not in list_2:
#         list_2.append(char)


# if list_2 == []:
#     print("No repeated pattern found")
# else:
#     longest_word = ""
#     len_1 = 0
#     for word in list_2:
#         if len(word) > len_1:
#             longest_word = word
#             len_1 = len(word)
#     print(longest_word)

###################################
##################                 苦尽甘来  终于完成！！！！！！！！！  其实本来也水，但是最后发现可以在count（）里面循环
# n = input()
# t = len(n)
# list_1 = []
# for i in range(t):
#     for k in range(t-i+1):
#         if n.count(n[i:i+k+1]) > 1 and n[i:i+k+1] not in list_1:
#             list_1.append(n[i:i+k+1])

# if list_1 == []:
#     print("No repeated pattern found")
# else:
#     longest_word = ""
#     len_1 = 0
#     for word in list_1:
#         if len(word) > len_1:
#             longest_word = word
#             len_1 = len(word)
#     print(longest_word)

########################################################    2024.9.29完成第一次作业总耗时    16+ hours！！！（粗略估计，只可能更多）


########################################################    2024.10.23第二次作业开始！！！
# num_list = input().split()
# num_list_2 = list(map(float,num_list))
# # print(num_list_2)

# num = int(input())
# query = []
# for i in range(num):
#     a_i = input()
#     query.append(a_i)

# # print(query)

# lst = []
# for i in range(num):
#     lst_1 = [m.strip() for m in query[i].split(",")]
#     lst.append(lst_1)
# # print(lst)



# for i in range(len(lst)):   
#     if lst[i][1] == "min":
        
#         if len(lst[i]) == 2:
#             print(min(num_list_2))
#         else:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(min(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print("Querying on empty list!")
            
#     if lst[i][1] == "max":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(max(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(max(num_list_2))
#     if lst[i][0] == "index" and lst[i][1] != "slice":
#         if num_list_2[int(lst[i][1])]:
#             print(num_list_2[int(lst[i][1])])
#         else:
#             print("Querying on empty list!")
#     if lst[i][0] == "index" and lst[i][1] == "slice":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])])
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(num_list_2)
#     if lst[i][1] == "all":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_3 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 print(sum(num_list_3))
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(sum(num_list_2))
#     if lst[i][1] == "avg":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_4 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 avg = sum(num_list_4)/len(num_list_4)
#                 print(avg)
#             else:
#                 print("Querying on empty list!")
#         else:
#             avg = sum(num_list_2)/len(num_list_2)
#             print(avg)
#     if lst[i][1] == "asc":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_5 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_5.sort()
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_5
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2.sort()
#             print(num_list_2)
#     if lst[i][1] == "desc":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6.sort(reverse = True)
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_6
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2.sort(reverse = True)
#             print(num_list_2)
#     if lst[i][1] == "rev":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6 = num_list_6[::-1]
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]= num_list_6
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2 = num_list_2[::-1]
#             print(num_list_2)

# ##################################  第一题判定太抽象了！！！！

# num = int(input())
# p = []
# for i in range(num):
#     a = input().split()
#     p.append(a)

# sum_1 = []
# for i in range(num-1):
#     m1 = (float(p[i+1][0]) - float(p[i][0]))**2 + (float(p[i+1][1]) - float(p[i][1]))**2
#     m = m1**(1/2)
#     sum_1.append(m)
# sum_2 = sum(sum_1)
# time = - float(p[0][2]) + float(p[num-1][2])
# v1 = sum_2 / time


# num_1 = int(input())
# q = []
# for j in range(num_1):
#     b = input().split()
#     q.append(b)

# print('{:.3f}'.format(v1))
# # print(q)
# sum_3 = []
# for j in range(num_1):
#     cal = 0
#     for i in range(int(q[j][0]),int(q[j][1])):
#         m2 = (float(p[i+1][0]) - float(p[i][0]))**2 + (float(p[i+1][1]) - float(p[i][1]))**2
#         m3 = m2**(1/2)
#         cal += 1
#         sum_3.append(m3)
#     sum_4 = sum(sum_3[-1:-1-cal:-1])
#     time_1 = float(p[int(q[j][1])][2]) - float(p[int(q[j][0])][2])
#     v2 = sum_4 / time_1
#     print('{:.3f}'.format(v2))

###############################################  第三题

# n = input().split()
# # print(n)
# list = []
# for i in range(int(n[0])):
#     a = input().split()
#     list.append(a)
# # print(list)

# for j in range(int(n[0])):
#     for i in range(int(n[1])):
#         if list[j][i] == "i":
#             if j==0 and i==0 and (list[j][i+1] == "i" or list[j][i+1] == "I")  and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"
#             if j==0 and i==int(n[1])-1 and (list[j][i-1] == "i" or list[j][i-1] == "I")  and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"
#             if j==int(n[0])-1 and i==int(n[1])-1 and (list[j][i-1] == "i" or list[j][i-1] == "I") and (list[j-1][i] == "i" or list[j-1][i] == "I"):
#                 list[j][i] = "e"
#             if j==int(n[0])-1 and i==0 and (list[j][i+1] == "i" or list[j][i+1] == "I")  and (list[j-1][i] == "i" or list[j-1][i] == "I"):
#                 list[j][i] = "e"
#             if j==0 and 0<i<int(n[1])-1 and (list[j][i+1] == "i" or list[j][i+1] == "I")  and (list[j][i-1] == "i" or list[j][i-1] == "I") and  list[j+1][i] and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"
#             if j==int(n[0])-1 and 0<i<int(n[1])-1 and (list[j][i+1] == "i" or list[j][i+1] == "I")  and (list[j][i-1] == "i" or list[j][i-1] == "I") and  list[j-1][i] and (list[j-1][i] == "i" or list[j-1][i] == "I"):
#                 list[j][i] = "e"  
#             if i==int(n[1])-1 and 0<j<int(n[0])-1 and (list[j-1][i] == "i" or list[j-1][i] == "I")  and (list[j][i-1] == "i" or list[j][i-1] == "I") and  list[j+1][i] and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"  
#             if i==0 and 0<j<int(n[0])-1 and (list[j][i+1] == "i" or list[j][i+1] == "I")  and (list[j-1][i] == "i" or list[j-1][i] == "I") and  list[j+1][i] and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"
#             if 0<j<int(n[0])-1 and 0<i<int(n[1])-1 and (list[j-1][i] == "i" or list[j-1][i] == "I")  and (list[j][i+1] == "i" or list[j][i+1] == "I") and (list[j][i-1] == "i" or list[j][i-1] == "I")  and (list[j+1][i] == "i" or list[j+1][i] == "I"):
#                 list[j][i] = "e"

# for i in range(int(n[0])):
#     print(list[i])

###################################### 第四题

# box_1 = int(input())
# wish1 = input().strip()
# wish = wish1[0] + wish1[2]
# color = list(input())
# pattern = list(input())
# elim = []
# turtles = []
# for i in range(len(color)):
#     a = color[i] + pattern[i]
#     turtles.append(a)



# def all(grid):
#    if len(set(grid)) == 9:
#         return True
#    else:
#         return False
    

# def three(t):  
#     num2 = 0   
#     if t[0] == t[1] == t[2] and t[0] != "0":  
#         num2 += 1   
#     if t[3] == t[4] == t[5] and t[3] != "0":  
#         num2 += 1   
#     if t[6] == t[7] == t[8] and t[6] != "0":  
#         num2 += 1    
#     if t[0] == t[3] == t[6] and t[0] != "0":  
#         num2 += 1  
#     if t[1] == t[4] == t[7] and t[1] != "0":  
#         num2 += 1
#     if t[2] == t[5] == t[8] and t[2] != "0":  
#         num2 += 1
#     if t[0] == t[4] == t[8] and t[0] != "0":  
#         num2 += 1
#     if t[2] == t[4] == t[6] and t[2] != "0":  
#         num2 += 1
#     return num2
        

# def check_pairs(grid):
#     global box_1
#     pairs = []
#     for i in range(8):
#         for j in range(i + 1, 9):
#             if grid[i] == grid[j] and grid[i] != "0":
#                 pairs.append(grid[i])
#                 pairs.append(grid[j])
#                 box_1 += 1
#                 grid[i] = grid[j] = "0"
#     return pairs

# grid = ["0"]*9
# for i in range(min(box_1,9)):
#     grid[i] = turtles[0] 
#     if turtles[0] == wish:
#         box_1 += 1      
#     turtles.remove(turtles[0])
# box_1 -= min(box_1,9)
         
            


# while True:
#     for i in range(9):
#         if turtles:
#                 if grid[i] == "0":
#                     if turtles[0] == wish:
#                         box_1 += 1
#                     grid[i] = turtles[0]
#                     turtles.remove(turtles[0])
#                     box_1 -= 1
#                     if box_1 == 0:
#                         break
#                     list_1 = [i for i in grid if i != "0"]
#                     if len(list_1) == 9:
#                         break
#     if ("0" not in grid) and all(grid):
#         box_1 += 5
#         elim.extend(grid)
#         grid = ["0"]*9

#     else:
#         if three(grid) != 0:
#             box_1 += 5*three(grid)

#         pairs = check_pairs(grid)
#         if pairs:
#             elim.extend(pairs)
    
#     if  box_1 == 0 and (not pairs) and ("0" in grid):
#          break

        

# for i in range(9):
#             if grid[i] != "0":
#                 elim.append(grid[i])



# for i in range(len(elim)):
#     elim[i] = (elim[i][0], elim[i][1])

# print(elim)

######################################     第四题debug了好久/  以后一定要按照题目要求的顺序来！！！！！！
######################################     2024.10.26 凌晨 2：57分 终于结束！！！！！！！！



######################################
######################################              第三次作业开始！！！！！24/11/1 10：44
# def piz(sequence_1=None, sequence_2=None):
#     def is_iter(i):
#         try:
#             iter(i)
#             return True
#         except TypeError:
#             return False
    
#     p = [sequence_1, sequence_2]
#     for j in p:
#         if not is_iter(j) and j is not None:
#             raise TypeError(f"Find a non-iterable object {type(j)}. Bad ++C Committee!")
        
#     if isinstance(sequence_1, list):
#         seq1 = sequence_1
#     else:
#         seq1 = list(sequence_1) if sequence_1 is not None else []

#     if isinstance(sequence_2, list):
#         seq2 = sequence_2
#     else:
#         seq2 = list(sequence_2) if sequence_2 is not None else []

#     seq = []
#     len1, len2 = len(seq1), len(seq2)
#     if len1 < len2:
#         seq1.extend(range(len2-len1))
#     elif len2 < len1:
#         seq2.extend(range(len1-len2))
#     for i in range(max(len(seq1), len(seq2))):    
#         seq.append((seq1[i], seq2[i]))
    
#     for j in p:
#         if is_iter(j) and not isinstance(j, list):
#            return seq + [f"Find a non-list but iterable object {type(j)}. Bad ++C Committee!"]
#     return seq

##################################### 第一题完成！！！ 2024/11/1 17：09


##################################### 第二题开始
# def search_social_tree(social_tree, target_r, oracle, path = []):
# 	for k, v in social_tree.items():
# 		current_path = path + [k]
# 		if target_r == oracle(current_path):
# 			return k
# 		if isinstance(v, dict):
# 			result = search_social_tree(v, target_r, oracle, current_path)
# 			if result and result != "!":
# 				return result
# 	return "!"
##################################### 第二题完成！！！ 2024/11/1 21：51

# def look(n):
#     if n == 0:
#         return ""
    
#     result = ''
#     count = 1
#     count1 = 1
#     if len(n) > 1:
#         for i in range(len(n)-1):
#             if n[0] == 'a':
#                 continue
#             if n[i+count1] == n[0]:
#                 count += 1
#             else:
#                 result += str(count) + n[0]
#                 n = 'a'*count + n[count::]
#                 count1 = count
#                 count = 1
#     if len(n) == 1:
#         result += str(1) + n[0]
#     return result

##############################
# n = input()
# p = 0
# while p < len(n):
#     x = n[p]
#     count = 0
#     while p < len(n) and n[p] == x:
#         p += 1
#         count += 1
#     result = str(count) + x
#     print(result,end = '')
################################

# l1 = [2,4,3]
# l2 = list(map(str,l1))
# a = ''.join(l2)
# print(a)

a = '123'
print(list(a))
