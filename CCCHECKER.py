import requests

logo = '''



                                ______________________________________
                               |                                      |
                    _.---------|.--.                                  |
                 .-'  `       .'/  ``                                 |
              .-'           .' |    /|                                |
           .-'         |   /   `.__//                                 |
        .-'           _.--/        /                                  |
       |        _  .-'   /        /                                   |
       |     ._  \      /     `  /                                    |
       |        ` .    /     `  /                                     |
       |         \ \ '/        /                                      |
       |        - \  /        /|                                      |
       |        '  .'        / |                                      |    by Lamer Qiz / @h3art_exe
       |          '         |.'|                                      |         1991 Team
       |                    |  |                                      |
       |                    |  |______________________________________|
       |                    |.'
       |                    /
       |                   /
       |                  /
       )                 /|
    .A/`-.              / |
   AMMMA. `-._         / /
  AMMMMMMMMA. `-.     / /
 AMMMMMMMMMMMMA. `.    /
AMMMMMMMMMMMMMMMMA.`. /
MMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMV'







'''

print(logo)
def cc_checker(cc_number):
    api_key = 'your_api_key_here' 
    url = f'https://api.bincodes.com/cc/?format=json&cc={cc_number}&api_key={api_key}'

    response = requests.get(url).json()

    if response['result'] == 'success':
        print(f"CC Number: {response['credit_card']['number']}")
        print(f"Brand: {response['credit_card']['issuer']}")
        print(f"Bank: {response['credit_card']['bank']}")
        print(f"Type: {response['credit_card']['type']}")
        return True
    else:
        return False

cc = input("Please enter your credit card number: ")

if cc_checker(cc):
    print("This credit card is valid and can be used for transactions.")
else:
    print("This credit card is invalid.")

