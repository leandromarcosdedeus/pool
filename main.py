import requests
import tkinter as tk
from time import sleep

def getPrice(currency, vsCurrency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies={vsCurrency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[currency][vsCurrency]
    return None

def showAlert(price, currency):
    root = tk.Tk()
    root.title(f"Alerta de Preço de {currency}!")
    message = f"O preço de {currency} chegou a ${price}, sua pool está desativada!"
    label = tk.Label(root, text=message, padx=20, pady=20)
    label.pack()
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack(pady=10)
    root.after(10000, root.destroy)
    root.mainloop()

def showReturnAlert(price, currency):
    root = tk.Tk()
    root.title(f"Retorno ao Preço de {currency}!")
    message = f"O preço de {currency} voltou a ${price}!"
    label = tk.Label(root, text=message, padx=20, pady=20)
    label.pack()
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack(pady=10)
    root.after(10000, root.destroy)
    root.mainloop()

def startMonitoring():
    currency = currencyEntry.get().lower()
    vsCurrency = "usd"
    try:
        minPrice = float(minPriceEntry.get())
        maxPrice = float(maxPriceEntry.get())
    except ValueError:
        statusLabel.config(text="Insira valores válidos para os preços.", fg="red")
        return

    statusLabel.config(text=f"Monitorando {currency.upper()}...")
    flag = 0

    while True:
        price = getPrice(currency, vsCurrency)
        if price is not None:
            print(f"Preço atual de {currency.upper()}: ${price}")
            if (price <= minPrice or price >= maxPrice) and flag == 0:
                showAlert(price, currency.upper())
                flag = 1
            elif flag == 1 and minPrice < price < maxPrice:
                showReturnAlert(price, currency.upper())
                flag = 0
        else:
            print(f"Não foi possível obter o preço de {currency.upper()}.")
        sleep(60)

root = tk.Tk()
root.title("Monitor de Preço de Criptomoedas")

tk.Label(root, text="Moeda (ex: solana, ethereum):").grid(row=0, column=0, padx=5, pady=5)
currencyEntry = tk.Entry(root)
currencyEntry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Preço Mínimo:").grid(row=1, column=0, padx=5, pady=5)
minPriceEntry = tk.Entry(root)
minPriceEntry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Preço Máximo:").grid(row=2, column=0, padx=5, pady=5)
maxPriceEntry = tk.Entry(root)
maxPriceEntry.grid(row=2, column=1, padx=5, pady=5)

statusLabel = tk.Label(root, text="", fg="blue")
statusLabel.grid(row=3, columnspan=2, pady=10)

tk.Button(root, text="Iniciar Monitoramento", command=startMonitoring).grid(row=4, columnspan=2, pady=10)
root.mainloop()
