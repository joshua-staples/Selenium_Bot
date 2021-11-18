from amazon_bot import amazon_bot as ab

def main():
    with open('password.txt') as f:
        password = f.read()
    with open('email.txt') as f:
        email = f.read()
    # works with https://www.amazon.com/AmazonBasics-Volt-Performance-Alkaline-Batteries/dp/B081FFR91C/ref=sr_1_11?keywords=aaa+batteries&qid=1637273963&sr=8-11
    # need some error handling to work for every url, some pages have a checkout pop-up, others have a subscription
    # option rather than one time purchase, both of these cases break the program
    url = input("Enter a Amazon Product Url: ")
    bot = ab(email, password, url)
    bot.add_product_to_cart()

main()
