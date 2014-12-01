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
    _MINAMOUNT = 0.0005

    #----------------------------------------------------------------
    # Create new payment
    # Required : amount    # Billed amount
    # Required : currency  # Billed currency
    # Required : address   # Receiving address
    # Optional : options   # Payment options : orderID,
    #                                           secret, 
    #                                           callback,
    #                                           company,
    #                                           motto,
    #                                           logoURL,
    #                                           addressLine1,
    #                                           addressLine2,
    #                                           email,
    #                                           item,
    #                                           description,
    #                                           returnAddress,
    #                                           escrow 
    # Returns   : JSON object
    #----------------------------------------------------------------
    def payment(self, amount, currency, address = '', options = {}):
    
        if amount < Coinvoy._MINAMOUNT:
            return self.error('Amount cannot be less than ' + Coinvoy._MINAMOUNT)
            
        escrow = False
        try:
            escrow = options['escrow']
        except KeyError:
            pass
            
        if not escrow and not self.validAddress(address):
            return self.error('Invalid address')
    
        params = {
            'amount'   : amount,
            'address'  : address,
            'currency' : currency
        }
        
        params.update(options)
        
        try:
            response = self._apiRequest('/api/payment', params)
        
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #----------------------------------------------------------------
    # Create new payment template to use in client side
    # Required : amount        # Billed amount
    # Required : currency      # Billed currency
    # Required : address       # Receiving address
    # Optional : options       # Button options: orderID,
    #                                         secret, 
    #                                         callback,
    #                                         company,
    #                                         motto,
    #                                         logoURL,
    #                                         addressLine1,
    #                                         addressLine2,
    #                                         email,
    #                                         item,
    #                                         description,
    #                                         returnAddress,
    #                                         buttonText,
    #                                         escrow 
    # Returns   : JSON object
    #----------------------------------------------------------------
    def button(self, amount, currency, address, options = {}):
        if amount < Coinvoy._MINAMOUNT:
            return self.error('Amount cannot be less than ' + Coinvoy._MINAMOUNT)
    
        escrow = False
        try:
            escrow = options['escrow']
        except KeyError:
            pass
            
        if not escrow and not self.validAddress(address):
            return self.error('Invalid address')

        params = {
            'amount'   : amount,
            'address'  : address,
            'currency' : currency
        }

        
        params.update(options)

        try:
            response = self._apiRequest('/api/button', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #----------------------------------------------------------------
    # Create new donation template to use in client side
    # Required : address   # Receiving address
    # Optional : options   # Donation options: orderID,
    #                                           secret,
    #                                           callback,
    #                                           company,
    #                                           motto,
    #                                           logoURL,
    #                                           addressLine1,
    #                                           addressLine2,
    #                                           email,
    #                                           item,
    #                                           description,
    #                                           buttonText
    # Returns   : JSON object
    #----------------------------------------------------------------
    def donation(self, address, options = {}):
   
        if not self.validAddress(address):
            return self.error('Invalid address')
            
        params = {
            'address' : address
        }
        
        params.update(options)

        try:
            response = self._apiRequest('/api/donation', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #----------------------------------------------
    # Completes the escrow process and forwards coins to their last destination
    # Required : key     # key returned from /api/payment
    # Optional : options # freeEscrow options: address
    # Returns  : JSON object
    #----------------------------------------------
    def freeEscrow(self, key, options = {}):
        try:
            address = options['address']
            
            if not self.validAddress(address):
                return self.error('Invalid address')
                
        except KeyError:
            pass
    
        params = {
            'key' : key
        }
        
        params.update(options)
    
        try:
            response = self._apiRequest('/api/freeEscrow', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #----------------------------------------------
    # Cancels the escrow process and returns coins to owner
    # Required : key     # key returned from /api/payment
    # Optional : options # freeEscrow options: returnAddress
    # Returns  : JSON object
    #----------------------------------------------
    def cancelEscrow(self, key, options = {}):
        try:
            returnAddress = options['returnAddress']
            
            if not self.validAddress(returnAddress):
                return self.error('Invalid address')
                
        except KeyError:
            pass
    
        params = {
            'key' : key
        }
        
        params.update(options)

        try:
            response = self._apiRequest('/api/cancelEscrow', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #---------------------------------------------------
    # Required : invoiceID
    # Returns  : JSON object
    #---------------------------------------------------
    def status(self, invoiceID):
        params = {
            'invoiceID' : invoiceID
        }

        try:
            response = self._apiRequest('/api/status', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)
            
        return response


    #---------------------------------------------------
    # Required : invoiceID
    # Returns  : JSON object
    #---------------------------------------------------
    def invoice(self, invoiceID):
        params = {
            'invoiceID' : invoiceID
        }

        try:
            response = self._apiRequest('/api/invoice', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

    #----------------------------------------------
    # Validates received payment notification (IPN)
    # Required : hash      # provided by IPN call
    # Required : orderID   # provided by IPN call
    # Required : invoiceID # provided by IPN call
    # Required : secret    # secret used while creating payment
    # Returns  : True/False
    #----------------------------------------------
    def validateNotification(self, hash, orderID, invoiceID, secret):
        hexString = hmac.new(secret, ":".join([orderID, invoiceID]), hashlib.sha256).hexdigest()

        return hexString == hash
            

    def _apiRequest(self, url, postParams = False):
        if postParams:
            data = json.dumps(postParams)
            data = data.encode('utf-8')
        else:
            data = None

        url = "https://coinvoy.net" + url        

        if sys.version_info.major == 2:
            req = urllib2.Request(url, data, { 'Content-type' : 'application/json' })
            response = urllib2.urlopen(req)
        else:
            req = urllib.request.Request(url, data, { 'Content-type' : 'application/json' })
            response = urllib.request.urlopen(req)

        return json.loads(response.read().decode())
        
    def error(self, message = ''):
        return { 'success' : False, 'message' : message }
        
    def validAddress(self, address):
        if len(address) < 26 or len(address) > 35:
            return False
        
        if address[0] != '1' and address[0] != '3':
            return False
            
        return True
         
         

    



