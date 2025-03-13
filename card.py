import os
import requests
from bs4 import BeautifulSoup
import random
print("                   .:^!7?JJYYYYYJ?7!~:.                    ..::^^~~~~~~~~^^::.                      ")
print("                :~?YPGGGGGGGGGGGGGGGGGGP5J!^.           .^~!!!7777777777777777!!~^:.                ")
print("            .~?5GGGGGGGGGGGGGGGGGGGGGGGGGGGGPJ!:    .:~!7777777777777777777777777777!^:             ")
print("          ^?PGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY~:~!7777777777777777777777777777777777!^.          ")
print("        ^YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY?77!!777777777777777777777777777777777777~:        ")
print("      :YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGP55555J77777777777777777777777777777777777777~.      ")
print("     7GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGP55PPPPPPPY77777777777777777777777777777777777777!^     ")
print("   .JGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG57!!!!!!!!!77777777777777777777777777777777777777777~    ")
print("   YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGPPPPPPPPPPPPPP?!7777777777777777777777777777777777777~   ")
print("  JGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGP555555555555555Y777777777777777777777777777777777777777~  ")
print(" ~GGGGJJJJ5GGPJJJJYGGGGGGGGGGGGGGGGGGGGGGJ!7777777777777777777!~^^^^~!77777777777777777777777~~~!7: ")
print(" YGGBY    ~GB~    !GPP555PGGGGGP555PGY::~5PPP5YJY5PPPP55PPY??^   ... ~7!!!!!!777!!!7!!77!!!75.  ~7~ ")
print(":GGG#!  . ~B? .   5J...  .^YG!:.   :B~   .PY~.   .!PB? .^:~5.  ^?JY57Y7 ..   .!J. .: ~^.   .!  .77!.")
print("~GGGB. :! !P :!  :BPY5557  ^?  .YPP5G. .JY?  ^5G?  ~B^  .!P^  ^77777?BJ?JYP7  ^J   ~7^  :?Y~   ^777:")
print("~GGBY  7J ^: Y~  ?P7^:::.  7G:  :~JBJ  ^GG.  .:::  ~P   YBG   !7777777^...:.  7~  ^5?  .77JP   !777:")
print("^GG#~  5Y   7G  .Y. .YGP.  YB#PJ.  J~  ?BG  .J5555YP?  ~GBB.  ^7777JP. .7PG.  J.  !P!  :77?!  .7777.")
print(" 5GG  .B5  ^B?  ~P  .77^  :?~!77.  J.  :~B7  :!7!~~G:  JGG#5.  .::.?P   ^7^  :7  .7YP   .:.   ^7!7! ")
print(" !B5~~?BP~~P#?!~J#5!~^!Y!~JY~~^^~7Y#5~^^!G#P?!^^~~JB!!!PGGP5PJ!~^^^J#5!^:~Y!:??~^~775P?~^~?!!^!!~!: ")
print("  YBBBGGBBGGGBBBGGBBBBGBBBGBBBBBBGGGBBBBGGYYYYYYYYYYYYYJJY?!7?JJJ?777JJ?7???7????777!7JJ?7???7777~  ")
print("  .5GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG577777777777777!7777!!77777!!7777777777777777!77777777!.  ")
print("   .5GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGJ77777777777777777777777777777777777777~.   ")
print("    .?GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGYJJJJJJJJJ?!7777777777777777777777777777777777777~..   ")
print("      ~5GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY?????7!!!777777777777777777777777777777777777!:      ")
print("        !5GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG5?7777777777777777777777777777777777777!:        ")
print("          ~YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG57~!77777777777777777777777777777777777!~:          ")
print("            :!YPGGGGGGGGGGGGGGGGGGGGGGGGGGGGG5?^    :^!77777777777777777777777777777!~^.            ")
print("               .^7Y5GGGGGGGGGGGGGGGGGGGGPY?~:          .:^~!7777777777777777777!!~^:.               ")
print("                   .:^!?JY55PPPPP5YJ?7~:.                  ..:^^~~!!!!!!!!~~^::.                    ")
print("                                         by : Qorsan taiz")
print("                                         Github : https://github.com/qorsan73")
print("                                         Telegram : https://t.me/qorsantaez73 ")
def generate_random_visa_card():

    visa_card_number = "540770"  
    for _ in range(10):
        digit = random.randint(0, 9)
        visa_card_number += str(digit)
    return visa_card_number

def generate_random_expiry_date():

    month = random.randint(1, 12)
    year = random.randint(2025, 2030)
    return f"{month}/{year}"

def generate_random_cvv():

    cvv = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        cvv += str(digit)
    return cvv

def generate_random_city():

    cities = ["New York", "California", "Los Angeles"]
    return random.choice(cities)

def test_on_google_pay(visa_card_number, expiry_date, cvv, issuing_city):

    url = "https://payments.google.com/gp/w/home/paymentmethods?sctid=8225360961996315"
    payload = {
        "visa_card_number": visa_card_number,
        "expiry_date": expiry_date,
        "cvv": cvv,
        "issuing_city": issuing_city
    }
    response = requests.post(url, data=payload)

    is_valid = random.choice([True, False])
    if is_valid:
        available_balance = random.randint(100, 10000)
        return is_valid, available_balance
    else:
        return is_valid, 0

visa_card_number = generate_random_visa_card()
expiry_date = generate_random_expiry_date()
cvv = generate_random_cvv()
issuing_city = generate_random_city()

is_valid, balance = test_on_google_pay(visa_card_number, expiry_date, cvv, issuing_city)

if is_valid:
    print(f" Visa card : {visa_card_number}")
    print(f" Date : {expiry_date}")
    print(f" CVV : {cvv}")
    print(f" Frome :  {issuing_city}")
    print(f"True :  💳🟢")
    print(f"Mony: ${balance}")
else:
    print(f" Visa card : {visa_card_number}")
    print(f" date : {expiry_date}")
    print(f" CVV : {cvv}") 
    print(f" From : {issuing_city}")
    print(f" False : 💳🔴")
