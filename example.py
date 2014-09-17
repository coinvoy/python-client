from coinvoy import Coinvoy


def createInvoice():
	coinvoy = Coinvoy()

	amount   = 0.42
	address  = "your cryptocurrency address"
	currency = "BTC"

	invoice = coinvoy.invoice(amount, address, currency)

	print(invoice)

	status = coinvoy.getStatus(invoice['id'])

	print(status)


def getDonation():
	coinvoy = Coinvoy()

	address  = "your cryptocurrency address"

	donation = coinvoy.donation(address)

	print(donation)


def getButton():
	coinvoy = Coinvoy()

	amount   = 0.42
	address  = "your cryptocurrency address"
	currency = "BTC"

	button = coinvoy.button(amount, address, currency)

	print(button)

	invoice = coinvoy.invoiceFromHash(button['hash'], 'BTC')

	print(invoice)


createInvoice()
#getDonation()
#getButton()