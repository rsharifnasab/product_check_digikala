#import this
from urllib.request import urlretrieve
print ("""dear user, welcome to this program
this program will find price and name of a digikala product id!""")


pro_id = str (input ("please enter code of product : "))

if pro_id[0] != "d" : pro_id = "dkp-" + pro_id
pro_url = "http://www.digikala.com/product/" + pro_id
#print("you requested this url : "pro_url)
urlretrieve(pro_url,"tmp.html")
my_file = open("tmp.html","r")
