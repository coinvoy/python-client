from coinvoy import Coinvoy


def createPayment(amount, currency, address):
    coinvoy = Coinvoy()

    payment = coinvoy.payment(amount, currency, address)

    print(payment)

    if payment['success']:
        status = coinvoy.status(payment['id'])

        print(status)

def createEscrow(amount, currency, address, returnAddress):
    coinvoy = Coinvoy()

    payment = coinvoy.payment(amount, currency, address, { 'escrow'        : True,
                                                           'returnAddress' : returnAddress })

    print(payment)

    if payment['success']:
        invoice = coinvoy.invoice(payment['id'])

        print(invoice)


def getDonation(address):
    coinvoy = Coinvoy()

    donation = coinvoy.donation(address)

    print(donation)


def getButton(amount, currency, address):
    coinvoy = Coinvoy()

    button = coinvoy.button(amount, currency, address)

    print(button)
    
def freeEscrow(key):
    coinvoy = Coinvoy()
    
    result = coinvoy.freeEscrow(key)
    
    print(result)
    
def cancelEscrow(key):
    coinvoy = Coinvoy()
    
    result = coinvoy.freeEscrow(key)
    
    print(result)


amount        = 0.012
address       = "receiving address" 
returnAddress = "return address"
currency      = "BTC"
key           = "key returned from escrow payment"

createPayment(amount, currency, address)
# createEscrow(amount, currency, address, returnAddress)
# getDonation(address)
# getButton(amount, currency, address)
# freeEscrow(key)
# cancelEscrow(key)
