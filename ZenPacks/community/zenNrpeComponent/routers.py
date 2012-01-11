from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul


class zenNrpeComponentRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('zenNrpeComponentAdapter', self.context)

    def addNrpeComponentRouter(self, nrpeCommand, nrpeFlag, nrpeArgs, nrpeEventComponent):
        
        facade = self._getFacade()

        ob = self.context
        success, message = facade.addNrpeComponent(ob, nrpeCommand, nrpeFlag, nrpeArgs, nrpeEventComponent)
        if success:
            return DirectResponse.succeed(message)
        else:
            return DirectResponse.fail(message) 
