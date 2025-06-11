import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Seaborn style
sns.set(style="darkgrid")  
sns.set(style="white")     
sns.set(style="dark")      
sns.set(style="ticks")      

# List of crypto Funds (CoinGecko IDs)
cryptos_index = ['bitcoin', 'ethereum', 'solana']
crypto_curr_inr = {coin: [] for coin in cryptos_index}
recordtime = []

# Track Price
units = 4
print("Tracking crypto Currencies...\n")

for i in range(units):
    coin_ids, funds = ','.join(cryptos_index), 'inr'
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': coin_ids, 'vs_currencies': funds}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        recordtime.append(current_time)

        for token_id in cryptos_index:
            total_in_inr = data.get(token_id, {}).get('inr')

            if total_in_inr is not None:
                crypto_curr_inr[token_id].append(total_in_inr)
                print(f"[{current_time}] {token_id.capitalize()}: ₹{total_in_inr}")
            else:
                print(f" We couldn't find the price for{token_id}.")
                crypto_curr_inr[token_id].append(None)

    else:
        print("Sorry, enable to fetch the data:", response.status_code)
        for crypto in cryptos_index:
            crypto_curr_inr[crypto].append(None)

    print("---")
    time.sleep(1)  

# Results

colors = ["#F00D0D", '#33C3FF', "#00F646"] 
plt.figure(figsize=(10, 6))

for i, crypto in enumerate(cryptos_index):
    plt.plot(recordtime, crypto_curr_inr[crypto], marker='o', label=crypto.capitalize(),color=colors[i])

plt.title("Cryptocurrency Price Tracker in INR",fontsize=17)
plt.xlabel("Crypto Prices Over Time",fontsize=15)
plt.ylabel("Price in INR",fontsize=15)
plt.legend()
plt.tight_layout()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
