# Ezzy's palindrome checker

# #palindrome checker

# userslist = []
# usesword=''

# for  i in range(10):
#     usersword = input('enter your list')
#     userslist.append(usersword)
# print(userslist)

# for user in userslist:
#     if user == user[:: -1]: 
#         print('true')
#     else: print("false") 




# palindrome checker

p = ["mummmy","hannah","murder for a jar of red rum","mom""seagull","tomato","no lemon",
     "no melon","some men interpret nine memos","madam"]
for x in p:
    if x == x[:: -1]:
        print( x, "is palindrome")
    else: 
        print(x,"is not palindrome") 
    
