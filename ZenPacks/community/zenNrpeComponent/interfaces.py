from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

class INrpeComponentInfo(IComponentInfo):
    """
    Info adapter for NrpeComponent components.
    """
    nrpeHost = schema.Text(title=u"Host")
    nrpeSSL = schema.Bool(title=u"SSL")
    nrpeCommand = schema.Text(title=u"Plugin")
    nrpeFlag = schema.Text(title=u"Flag")
    nrpeArgs = schema.List(title=u"Args")
    nrpeEventComponent = schema.Text(title=u"Component")

    
class IzenNrpeComponentFacade(IFacade):
    
    def addNrpeComponent(self, ob, nrpeCommand, nrpeFlag, nrpeArgs, nrpeEventComponent):
        """  add NRPE Component to device
        """
