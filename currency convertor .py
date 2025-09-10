import requests

init_currency = input("Enter an intial currency: ")
target_currency = input("Enter an target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue

    if amount == 0 :
        print("The amount must be greater than 0")
        continue
    else:
        break

    
url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "pEJf9NTyTS7uLCMHY41sZpIVhu3ZmPkj"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code != 200:
    print("sorry, there was a problem. Please try again later")
    quit()
result = response.json()
converted_amount = result['result']
print(f'{amount} {init_currency} = {converted_amount} {target_currency}')