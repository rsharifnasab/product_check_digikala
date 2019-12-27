from re import search
import urllib.request


def url_catch():
    pro_id = str(input("please enter code of product : "))
    if pro_id[0] != "d":
        pro_id = "dkp-" + pro_id
    pro_url = "https://www.digikala.com/product/" + pro_id
    try:
        user_agent = 'Mozilla/5.0' \
                '(Macintosh; Intel Mac OS X 10_9_3)' \
                'AppleWebKit/537.36 (KHTML, like Gecko)' \
                'Chrome/35.0.1916.47 Safari/537.36'
        html = urllib.request.urlopen(
            urllib.request.Request(
                pro_url,
                headers={'User-Agent': user_agent}
            )
        ).read()
        f = open("tmp.html", "wb")
        f.write(html)
        f.close()
        print ("product info caught succesfully")
        return pro_url
    except:
        print("product id error, pls try again")
        return url_catch()

print ("""dear user, welcome to this program
this program will find price and name of a digikala product id!""")

url_catch()

try:
    my_file = open("tmp.html", "r")
except:
    print ("file creatation error... exiting")
    exit()
htm = my_file.read()

try:
    name_pattern = r"""<meta property="og:title" content=".*">"""
    name_o = search(name_pattern, htm)
    name = htm[name_o.start()+35:name_o.end()-2]
except:
    print ("im really sorry. i cant find product name. pls try again later***")

try:
    price_pattern = r"""meta name="twitter:data1" content=".*">"""
    price_o = search(price_pattern, htm)
    price = htm[price_o.start()+35:price_o.end()-2]
except:
    print("im really sorry. i cant find product price. pls try again later")

try:
    print("your product name is : ", name, "\nand price is :", price)
except:
    print("print error")

print("sorry for persian text problem!")
