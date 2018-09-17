#import this
from re import search
from urllib.request import urlretrieve

def url_catch():
    pro_id = str (input ("please enter code of product : "))

    if pro_id[0] != "d" : pro_id = "dkp-" + pro_id
    pro_url = "http://www.digikala.com/product/" + pro_id
    #print("you requested this url : "pro_url)
    try :
        urlretrieve(pro_url,"tmp.html")
        print (" product info caught succesfully")
        return pro_url
    except : 
        print("product id error, pls try again")
        return url_catch()    


print ("""dear user, welcome to this program
this program will find price and name of a digikala product id!""");
url_catch()
try :
    my_file = open("tmp.html","r")
except:
    print ("file creatation error... exiting")    
    exit()
htm = my_file.read()


#  <meta property="og:title" content="شارژر همراه انرجایزر مدل UE15005 ظرفیت 15000 میلی آمپر ساعت">
try :     
    name_pattern = r"""<meta property="og:title" content=".*">"""
    name_o = search(name_pattern,htm)
    name = htm[name_o.start()+35:name_o.end()-2]
except :
    print ("im really sorry , i cant find product name , pls try again later")

#c-price__value ۱۹۹,۰۰۰ <span
#       span class="js-price-value"> ۱۹۹,۰۰۰ </span>
# "price": 1990000,
try:
    price_pattern=r"""price.:.{50},"""
    price_o = search(price_pattern,htm)
    price = htm[price_o.start()+1:price_o.end()-1]
except :
    print("im really sorry , i cant find product price , pls try again later")

try:
    print(name)
    print(price)
except :
    pass

#        252167