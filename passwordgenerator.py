import string
import random
import array
# length=int(input("enter password length: "))
# print("choose password character to input\n  1. Digits\n 2. Letters\n 3. Special characters\n 4. Exit")
      
# characterlist=""
# while(True):
#     choice=int(input("pick a number"))
#     if choice==1:
#         characterlist += string.ascii_letters
#     elif( choice==2):
#         characterlist += string.digits
#     elif choice==3:
#         characterlist += string.punctuation
#         break
#     else:
#         print("please pick a valid option")
        
#         password=[]
#         for i in range(length):
#             randomchar=random.choice(characterlist)
#             password.append(randomchar)
#             print ("the random password is " + "".join(password))
            
            
############------------------------------PASSWORD GENERATOR---------------------------------------------------
def characters():
    all_characters=string.ascii_letters + string.digits + string.punctuation
length=int(input("enter password length: "))
password=[]
for i in range(length):
            randomchar=random.choice("all_characters")
            password.append(randomchar)
            print ("your password is " + "".join(password))
characters()


# #----------------------------------------------STRONG PASSWORD GENERATOR---------------------------------------

# length=int(input("enter password length: "))

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
# LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
#                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
#                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
#                      'z'] 
  
# UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
#                      'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
#                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
#                      'Z'] 
  
# SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
#            '*', '(', ')', '<'] 
   
# COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 
  
# # randomly select at least one character from each character set above 
# rand_digit = random.choice(DIGITS) 
# rand_upper = random.choice(UPCASE_CHARACTERS) 
# rand_lower = random.choice(LOCASE_CHARACTERS) 
# rand_symbol = random.choice(SYMBOLS) 
  
# # helps to select only 4 passwords, one from each rand
# temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
  
  
# # selelcts the rest of the password 
# for x in range(length - 4): 
#     temp_pass = temp_pass + random.choice(COMBINED_LIST) 
  
#     # convert temporary password into array and shuffle to  prevent it from having a consistent pattern 
#     temp_pass_list = array.array('u', temp_pass) 
#     random.shuffle(temp_pass_list) 
  
# password = "" 
# for x in temp_pass_list: 
#         password = password + x 
# print(password)
# for word in range(password):
#     random_word=".join(random.shuffle(temp_pass_list) for_in range(password)))"
    
# print(random_word)
      