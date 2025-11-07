
items_purchase = {'Water': '1', 'Bread': '3', 'TV': '1,000', 'Fertilizer': '20'}
wallet = '10'

wallet = int(wallet.replace("$", ""))

basket = []

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))

    if wallet >= price:
        basket.append(item)
        wallet -= price

if not basket:
    print("Rien")
else:
    print(sorted(basket))
