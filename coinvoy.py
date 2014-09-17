import json
import sys
import hashlib, hmac

try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request
    import urllib.parse


class Coinvoy:

    def invoice(self, amount, address, currency, options = None):
        params = {
            'amount'   : amount,
            'address'  : address,
            'currency' : currency
        }

        if not options is None:
            params.update(options)

        try:
            response = self._apiRequest('/api/newInvoice', params)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while creating invoice: ' + response['message']}

        return response

    def button(self, amount, address, currency, options = None):

        params = {
            'amount'   : amount,
            'address'  : address,
            'currency' : currency
        }

        if not options is None:
            params.update(options)

        try:
            response = self._apiRequest('/api/getButton', params)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}

        return response

    def donation(self, address, options = None):
        params = {
            'address' : address
        }
        
        if not options is None:
            params.update(options)

        try:
            response = self._apiRequest('/api/getDonation', params)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}

        return response

    def invoiceFromHash(self, hash, payWith):

        params = {
            'hash'    : hash,
            'payWith' : payWith
        }

        try:
            response = self._apiRequest('/api/invoiceHash', params)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        if not response['success']:
            return {'success' : False, 'error' : 'An error occured while getting button info: ' + response['message']}

        return response

    def freeEscrow(self, key):
        params = {
            'key' : key
        }

        try:
            response = self._apiRequest('/api/freeEscrow', params)
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        return response


    def getStatus(self, invoiceId):
        if invoiceId.strip() == '':
            return {'success' : False, 'error' : 'Please supply an invoice id'}

        params = {
            'invoiceId' : invoiceId
        }

        try:
            response = self._apiRequest('/api/status', { 'invoiceId' : invoiceId })
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }
        return response


    def getInvoice(self, invoiceId):
        if invoiceId.strip() == '':
            return {'success' : False, 'error' : 'Please supply an invoice id'}

        params = {
            'invoiceId' : invoiceId
        }

        try:
            response = self._apiRequest('/api/invoice', { 'invoiceId' : invoiceId })
        except:
            return {'success' : False, 'error' : 'An error occured: ' + sys.exc_info()[0] }

        return response

    def validateNotification(self, invoiceId, hash, orderID, address):
        hexString = hmac.new(address, ":".join([orderID, invoiceId]), hashlib.sha256).hexdigest()

        return hexString == hash
            

    def _apiRequest(self, url, postParams = False):

        if postParams:
            data = urllib.parse.urlencode(postParams)
            data = data.encode('utf-8')
        else:
            data = None

        url = "https://coinvoy.net" + url;

        if sys.version_info.major == 2:
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
        else:
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)

        return json.loads(response.read().decode())

    



