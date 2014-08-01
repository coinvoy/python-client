import json
import sys

try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request
    import urllib.parse

__author__ = 'ps'

class Coinvoy:


    def __init__(self, options):
        self.options = options

    def invoice(self, payment):

        base = self.options.copy()
        base.update(payment)
        payment = base

        try:
            response = self._apiRequest('http://cryptopay/api/newInvoice', payment)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while creating invoice: ' + response['message']}

        return response

    def button(self, button):
        base = self.options.copy()
        base.update(button)
        button = base

        try:
            response = self._apiRequest('http://cryptopay/api/getButton', button)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}
        return response

    def donation(self, donation):
        base = self.options.copy()
        base.update(donation)
        donation = base

        try:
            response = self._apiRequest('http://cryptopay/api/getDonation', donation)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}
        return response

    def invoiceFromHash(self, hash=False, payWith=False, amount=False):

        data = {
            'hash'    :hash,
            'payWith' :payWith,
            'amount'  :amount,
        }
        try:
            response = self._apiRequest('http://cryptopay/api/getDonation', data)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}
        return response

    def completeEscrow(self, key):
        if key.strip() == '': return {'success' : False, 'error' : 'Please supply a key'}

        try:
            response = self._apiRequest('http://cryptopay/api/freeEscrow', { 'key' : key })
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }
        return response


    def getStatus(self, invoiceId):
        if invoiceId.strip() == '': return {'success' : False, 'error' : 'Please supply an invoice id'}

        try:
            response = self._apiRequest('http://cryptopay/api/status', { 'invoiceId' : invoiceId })
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }
        return response


    def getInvoice(self, invoiceId):
        if invoiceId.strip() == '': return {'success' : False, 'error' : 'Please supply an invoice id'}

        try:
            response = self._apiRequest('http://cryptopay/api/invoice', { 'invoiceId' : invoiceId })
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }
        return response

    def _apiRequest(self, url, postParams = False):

        if postParams:
            data = urllib.parse.urlencode(postParams)
            data = data.encode('utf-8')
        else:
            data = None

        if sys.version_info.major == 2:
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
        else:
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)

        return json.loads(response.read().decode())



