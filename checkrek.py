# Desc      : A python CLI based tools to check Indonesian bank/e-wallet account holder
# Author    : Hiiruki <hi@hiiruki.dev>
# URL       : https://github.com/hiiruki/CheckRek

import requests

print("""


         _____ _               _    _____      _    
        / ____| |             | |  |  __ \    | |   
       | |    | |__   ___  ___| | _| |__) |___| | __
       | |    | '_ \ / _ \/ __| |/ /  _  // _ \ |/ /
       | |____| | | |  __/ (__|   <| | \ \  __/   < 
        \_____|_| |_|\___|\___|_|\_\_|  \_\___|_|\_\ 
                                              
  A tools to check Indonesian bank/e-wallet account holder
                        by @hiiruki
                                              
""")

# Define the bank menu and mapping
bank_menu = {
    1: "BCA",
    2: "Blu By BCA",
    3: "BNI",
    4: "BRI",
    5: "Mandiri",
    6: "CIMB Niaga",
    7: "Permata",
    8: "Danamon",
    9: "Bank DKI",
    10: "BTPN/Jenius",
    11: "Bank NOBU",
    12: "Bank Jago",
    13: "Line Bank",
    14: "LinkAja!",
    15: "GoPay",
    16: "OVO",
    17: "DANA",
}
bank_mapping = {
    "BCA": "bca",
    "Blu By BCA": "royal",
    "BNI": "bni",
    "BRI": "bri",
    "Mandiri": "mandiri",
    "CIMB Niaga": "cimb",
    "Permata": "permata",
    "Danamon": "danamon",
    "Bank DKI": "dki",
    "BTPN/Jenius": "tabungan_pensiunan_nasional",
    "Bank NOBU": "nationalnobu",
    "Bank Jago": "artos",
    "Line Bank": "hana",
    "LinkAja!": "linkaja",
    "GoPay": "gopay",
    "OVO": "ovo",
    "DANA": "dana",
}

# Get the bank choice from the user
print("Supported bank/e-wallet:\n")
for number, name in bank_menu.items():
    print(f"{number}. {name}")
bank_choice = int(input("\nPlease choose a bank/e-wallet from the menu (use number 1-17): "))
while bank_choice not in bank_menu:
    bank_choice = int(input("Invalid option. Please choose a bank/e-wallet from the menu (use number 1-17): "))
bank_name = bank_menu[bank_choice]
print("""
Format:

- Bank      : 338801028216xxx
- E-Wallet  : 08123456789
""")
account_number = input("Enter the account number: ")

# Send the API request
api_url = "https://cekrek.heirro.dev/api/check"
api_params = {
    "accountBank": bank_mapping[bank_name],
    "accountNumber": account_number,
}
response = requests.post(api_url, data=api_params)

# Parse the API response and print the account info
json_data = response.json()
if json_data["status"] == 200:
    account_name = json_data["data"][0]["accountName"]
    print("\n============= Account Information =============\n")
    print(f"Bank/e-wallet   : {bank_name}")
    print(f"Number          : {account_number}")
    print(f"Name            : {account_name}\n")
else:
    print("API request failed.\n")
