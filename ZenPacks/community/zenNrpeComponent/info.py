from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenNrpeComponent.interfaces import INrpeComponentInfo

class NrpeComponentInfo(ComponentInfo):
    """
    Info adapter for zenNrpeComponent components.
    """
    implements(INrpeComponentInfo)
    nrpeHost = ProxyProperty("nrpeHost")
    nrpeSSL = ProxyProperty("nrpeSSL")
    nrpeCommand = ProxyProperty("nrpeCommand")
    nrpeFlag = ProxyProperty("nrpeFlag")
    nrpeArgs = ProxyProperty("nrpeArgs")
    nrpeEventComponent = ProxyProperty("nrpeEventComponent")
