# ---------------------- Day 13 -------------------
#                   Date  17-03-2024 
#                   -------------------  
#  *****************  String Methods ***************
x = y = z ="shahbaz"
print(x)
print(y)
print(z) 
s = "shahbaz"
print(len(s))
print(" The size of Length is ",len(s)) #string with length(also called size of string)

# ---------------- String Method No : -----------------
# ---------------- len() Method --------------
print(" Length(size of character) Method ")
a = " junaid "
print(len(a)) 
# ----------------- upper() Case Method -------------
print("variable.upper() case Method ") 
print(a.upper())   
# ----------------- lower() Case Method --------------
print("variable.lower() case Method ") 
print(a.lower()) 
# ----------------- rstrip() Method  --------------
print("It can't remove the lead character /It remove any trailing characters /also remove speical character ")
a = "junaid!!!"
b = "junaid$$$"
print(a.rstrip("!")) 
print(b.rstrip("$")) 

# ----------------- strip()Method -----------
print(" It remove White space before and after the string ")
c = "    shahbaz    " 
print(c.strip()) 

# ----------------- replace() Method ------------
print(" The Method all occurance of string with another string ")  
a = " shahbaz junaid"    
print(a.replace("shahbaz junaid"," zeeshan Mehdi "))

# ------------------ split() Method ------------
# print(" The split() Method split the given string at the specified instance ")
# print(" and returns the seperated string as list items ")           
print(" OR convert into the list items ")    
a = " shahbaz Jamil Zeeshan " 
print(a.split()) 

# ------------------ capitalize() Method -----------
# The frist character is capitalize  to upper case 
blogv = "introduction of computer Science"
print(blogv.capitalize())        

#------------------- centre() Method -----------------
# The method align the string centrenas parameter  given by the user 
welcom = "WelLcom to our party"
a = "shahbaz"
print(welcom.center(100))    
print(a.center(50))   

# -----------------  count() Method -------------------
# The method is used to count the letter of character
x ="shahbaz !!! !!! salingi"   
print(x.count("a"))

#  ----------------- endswith() Method ------------------
#  End of string with any character value . if yes then retrun otherwise else return false
a ="junaid bhai"      
print(a.endswith("bhai"))   

# -------------------- find() Method ------------------------
print(a.find("bhai")) # also called find the index 

# ------------------- isalnum() Method ---------- 
# it return Ture only if the entire string only consists of A-Z , a-z and 0-9 if any other
# character or punctation are present then it returns false 
print("This is for isalnum ")  
print(a.isalnum()) 

# ------------------- isalpha() Method ------------------
# It not include numeric .It consist A-Z and a-z .
a ="shah"  
print(a.isalpha())     
                      
# ------------------- islower() Method ------------------
# Retruns True if all the character is the string are lower case else it retruns False
# It is same with the lower case method it covert the string in small letter alphabet
# 
a ="shah" 
print(a.islower())     

# ------------------- isupper() Method ------------------
# Also same like islower()
a = "SHAH"
print(a.isupper()) 

# ------------------- isspace() Method ------------------
# Returns Ture only od the string contains white space else returns False 
a ="  "
print(" This is for tab / space ") 
print(a.isspace()) 

# ------------------- istitle Method ------------------

#  The istitle Method() returns Ture only if frist letter of each word of the string 
# is capitalized else if returns False 
a ="  Shahbaz Junaid" 
print(a.istitle()) 

# ------------------- startswith() Method ------------------
a ="python is easy"      
print(a.startswith("python")) 

# ------------------- swapcase() Method ------------------
# Convert upper case into lower and also lower into upper case . It is most useable method
a ="shahaz" 
print(a.swapcase())

# ------------------- title() Method ------------------
# used in blogs  
# The title method capitalizes each letter of word within the string
a =" hi this is shahbaz junaid" 
print(a.title()) 

# And also recoding steped with harry bhai  


                            







