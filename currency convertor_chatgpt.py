import requests

# --- إعداد الـ API Key والروابط ---
API_KEY = "pEJf9NTyTS7uLCMHY41sZpIVhu3ZmPkj"
BASE_URL = "https://api.apilayer.com/fixer"
HEADERS = {"apikey": API_KEY}

# --- الحصول على العملات المدعومة ---
symbols_url = f"{BASE_URL}/symbols"
symbols_response = requests.get(symbols_url, headers=HEADERS)

if symbols_response.status_code != 200:
    print("⚠️ Failed to fetch currency symbols.")
    quit()

symbols_data = symbols_response.json()
supported_currencies = symbols_data["symbols"]  # دي بقت dict فيها {'EGP': 'Egyptian Pound', ...}

# --- السؤال عن عرض العملات ---
while True:
    show_list = input("🔎 Do you want to see the supported currencies? (yes/no): ").strip().lower()
    if show_list in ["yes", "y"]:
        print("\n🌍 Supported Currencies:\n")
        for code, name in supported_currencies.items():
            print(f"{name} : {code}")
        print("-" * 40)
        break
    elif show_list in ["no", "n"]:
        break
    else:
        print("❌ Please enter 'yes' or 'no'.")

# --- دالة لإدخال العملة بعد التحقق ---
def get_valid_currency(prompt_text):
    while True:
        currency = input(prompt_text).upper().strip()
        if currency in supported_currencies:
            return currency
        else:
            print("❌ Invalid currency code. Please try again.")

# --- استلام المدخلات ---
init_currency = get_valid_currency("Enter an initial currency: ")
target_currency = get_valid_currency("Enter a target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            continue
        break
    except:
        print("❌ The amount must be a numeric value!")

# --- إرسال طلب التحويل ---
def convert_currency(from_curr, to_curr, amount):
    url = f"{BASE_URL}/convert?from={from_curr}&to={to_curr}&amount={amount}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("⚠️ Error while converting currency.")
        quit()
    data = response.json()
    return data["result"]

# --- تنفيذ التحويل ---
converted_amount = convert_currency(init_currency, target_currency, amount)
print(f"\n✅ {amount} {init_currency} = {converted_amount} {target_currency}")

# --- خيار التحويل العكسي مع التحقق من صحة الإدخال ---
while True:
    reverse = input("\n🔁 Do you want to convert the result back? (yes/no): ").strip().lower()
    if reverse in ["yes", "y"]:
        reversed_result = convert_currency(target_currency, init_currency, converted_amount)
        print(f"🔄 {converted_amount} {target_currency} = {reversed_result} {init_currency}")
        break
    elif reverse in ["no", "n"]:
        print("👌 Okay! Conversion completed.")
        break
    else:
        print("❌ Invalid input. Please type 'yes' or 'no'.")
