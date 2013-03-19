from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

'''
args: routername,adaptername,routerMethodName, createMethodName
'''

class zenNrpeComponentRouter(DirectRouter):
    def _getFacade(self):
    	return Zuul.getFacade('zenNrpeComponentAdapter', self.context)
    
    def addNrpeComponentRouter(self, **kwargs):
    	from Products.ZenUtils.Ext import DirectResponse
    	facade = self._getFacade()
    	ob = self.context
    	success, message = facade.addNrpeComponent(ob, **kwargs)
    	if success:
    		return DirectResponse.succeed(message)
    	else:
    		return DirectResponse.fail(message)

