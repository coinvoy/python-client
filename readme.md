Coinvoy API - Python Client Library
===================================

Python client library for Coinvoy API


##About Coinvoy

Coinvoy is an online payment processor. It's objective is to provide an easiest yet the most secure way to accept cryptocurrencies.

##Get started


Place coinvoy.py in your directory and import it.

```
from coinvoy import Coinvoy

coinvoy = Coinvoy()

# Create invoice
amount   = 0.012
address  = "receiving address"
currency = "BTC"

payment = coinvoy.payment(amount, currency, address)

print(payment)

# payment.id      - always find your invoice at https://coinvoy.net/invoice/{id}
# payment.key     - you need this key if this is an escrow
# payment.url     - shortcut for the payment box https://coinvoy.net/payment/{id}
# payment.address - show it to user, it is the payment address
# payment.html    - easiest way to display a payment box, just echo it

```

###List of all commands:
- payment(amount, currency, address)			          - creates payment
- button(amount, currency, address)			              - prepares a button template
- donation(address)		                                  - prepares a donation template
- validateNotification(hash, orderID, invoiceID, secret)  - checks if incoming payment notification is valid.
- freeEscrow(key)		                                  - finalize an escrow with its unique key. This action sends funds to receiver
- cancelEscrow(key)                                       - cancel an escrow with its unique key. This action sends funds to owner
- status(invoiceID)		                                  - current status of payment [new,approved,confirmed,completed,cancelled]
- invoice(invoiceID)		                              - get latest invoice object

Your feedback and suggestions are very much welcome. Please write to support@coinvoy.net for any contact. 

Coinvoy

