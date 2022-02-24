import re

mystr = '''
But I must explain to you how all this mistaken idea of denouncing pleasure and praising 
pain was born and I will give you a complete account of the system, and expound the actual 
teachings of the great explorer of the truth, the master-builder of human happiness. No one 
rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not 
know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is 
there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because 
occasionally circumstances occur in which toil and pain can procure him some great pleasure. 
To take a trivial example, which of us ever undertakes laborious physical exercise, 
except to obtain some advantage from it? But who has any right to find fault with a 
man who chooses to enjoy a pleasure that has no annoying consequences, 
or one who avoids a pain that produces no resultant pleasure?"
'''
# Findall, search, split, sub, finditer
# patt = re.compile(r'pain')
# patt = re.compile(r'.ros')   # To find the place of character...
# patt = re.compile(r'^who')
# patt = re.compile(r're?$')   # To Check the end of string..!
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai+')   # This will print only a and i combine.
# patt = re.compile(r'ai{2}')   # This also to check
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|fax')


# Special Sequences...!
# patt = re.compile(r'But\A')
patt = re.compile(r'\d{5}-\d{4}')  # This one is for extracting the numbers based on value locations such as 5 and 4..!

# For Extracting Indian Standard Numbers..!
# pattern=re.compile(r'\+91\d{10}')
# matches=pattern.finditer(str)
# for m in matches:
#     print(m)

matches = patt.finditer(mystr)

for match in matches:
    print(match)

    # print(mystr[448:452])




# Printing Numbers From 1 to N..!   Assignment work
# for i in range(int(input())):
#     print(i,end=" ")


