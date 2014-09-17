Coinvoy API - Python Client Library
================================

Python client library for Coinvoy API


##About Coinvoy

Coinvoy is an online payment processor with an integrated exchange feature for established cryptocurrencies, namely Bitcoin, Litecoin and Dogecoin. It's objective is to provide an easiest yet the most secure way to accept cryptocurrencies.

##Get started


Place coinvoy.py in your directory and import it.

```
from coinvoy import Coinvoy

coinvoy = Coinvoy(options)

# Create invoice
amount   = 1.42;                           # Amount of invoice value
address  = "your cryptocurrency address"   # Your receiving address for Bitcoin, Litecoin or Dogecoin
currency = "BTC";                          # Currency of invoice value

invoice = coinvoy.invoice(amount, address, currency)

print(invoice)

# invoice.id      - always find your invoice at https://coinvoy.net/invoice/{id}
# invoice.key     - you need this key if this is an escrow
# invoice.url     - shortcut for the payment box https://coinvoy.net/payment/{id}
# invoice.address - show it to user, it is the payment address
# invoice.html    - easiest way to display a payment box, just echo it

```

###List of all commands:
- invoice(payment)			                        - creates live invoice
- button(button)			                        - prepares a button template
- donation(donation)		                        - prepares a donation template
- invoiceFromHash(hash, payWith[,amount]) 			- creates live invoice from template hash
- validateNotification(invoiceId, orderID, hash)	- checks if incoming payment notification is valid.
- completeEscrow(key)		                        - finalize an escrow with its unique key. This action sends funds to receiver
- getStatus(invoiceId)		                        - current status of invoice [new,approved,confirmed,completed,cancelled]
- getInvoice(invoiceId)		                        - get latest invoice object

Your feedback and suggestions are very much welcome. Please write to support@coinvoy.net for any contact. 

Coinvoy

