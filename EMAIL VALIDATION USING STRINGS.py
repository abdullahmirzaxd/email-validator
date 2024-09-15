#!/usr/bin/env python
# coding: utf-8

# In[1]:


#EMAIL VALIDATION USING STRINGS

email = input("Write your email: ")

k, j, d = 0, 0, 0  # Flags 

if len(email) >= 15:  #email limit 
    
    if email[0].isalpha():  #first character should be a letter
        
        if ("@" in email) and (email.count("@") == 1):  # only single '@'
            
            if email[-4] == "." or email[-3] == ".":  # posotion of '.'
                
                for i in email:
                    if i.isspace():  # check any space
                        k = 1
                    elif i.isalpha():  #all letters
                        if i.isupper():  #no uppercase letters allowed
                            j = 1
                    elif i.isdigit():  #allow digits
                        continue
                    elif i == "_" or i == "." or i == "@":  #allow _, ., @
                        continue
                    else:  
                        d = 1

                #check if any of the flags are set to 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong email, try again")
                else:
                    print("Right email")
            else:
                print("Wrong email, try again")
        else:
            print("Wrong email, try again")
    else:
        print("Wrong email, try again")
else:
    print("Wrong email, try again")


# In[ ]:




