#!/usr/bin/env python
# coding: utf-8

# In[1]:


#

import re  

email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"        

# ^:start of the stringEMAIL VALIDATION USING REGEX MODULE
# [a-z]+:one or more lowercase letters
# [\._]?:optional dot (.) or underscore (_)
# [a-z0-9]+:one or more lowercase letters or numbers (no space inside this part)
# [@]:the @ symbol must be present
# \w+:one or more word characters (letters, digits, or underscores) for the domain name
# [.]:a dot (.)
# \w{2,3}: 2 or 3 word characters (for domain suffix like .com or .net)
# $:end of the string



user_email = input("Enter email: ")

# Check if the user's input matches the email pattern
if re.search(email_condition, user_email):
    print("Right Email")
else:
    
    print("Wrong Email")



# In[ ]:




