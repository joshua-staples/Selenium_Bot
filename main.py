from amazon_bot import amazon_bot as ab
import smtplib

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
    bot.login_amazon()
    bot.shipping()
    # can't get payment switching working yet
    # bot.payment()
    bot.checkout()

    # send an email when it adds to cart
    # not working yet, but close...

    # with open('email_password.txt') as f:
    #     email_pass = f.read()

    # gmail_user = email
    # gmail_password = email_pass

    # sent_from = gmail_user
    # to = email
    # subject = 'Item Added to Your Amazon Cart'
    # body = f'Item added to your cart! Go to this link now to checkout! ({bot.get_url()})'

    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s

    # %s
    # """ % (sent_from, to, subject, body)

    # try:
    #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     server.ehlo()
    #     server.login(gmail_user, gmail_password)
    #     server.sendmail(sent_from, to, email_text)
    #     server.close()

    #     print('Email sent!')
    # except:
    #     print('Something went wrong...')

    # finally close the webdriver session
    bot.close_session()

main()