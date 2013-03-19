from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenNrpeComponent.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class NrpeComponentInfo(ComponentInfo):
    implements( INrpeComponentInfo )
    ssl = ProxyProperty('ssl')
    arglist = ProxyProperty('arglist')
    command = ProxyProperty('command')
    eventKey = ProxyProperty('eventKey')
    hostname = ProxyProperty('hostname')
    port = ProxyProperty('port')
    eventComponent = ProxyProperty('eventComponent')
    treatTimeout = ProxyProperty('treatTimeout')


'''
args : zenpackname,zenpackname,dsclass,dsvolcclass,dsvolcvar,dsinfo,dsinterface,dsinfoproperties
'''
# datasource info
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.community.zenNrpeComponent.interfaces import *
from ZenPacks.community.zenNrpeComponent.datasources.NrpeComponentDataSource import *

def NrpeComponentRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(NrpeComponentDataSource.onRedirectOptions)

class NrpeComponentDataSourceInfo(RRDDataSourceInfo):
    implements(INrpeComponentDataSourceInfo)
    cycletime = ProxyProperty('cycletime')
    hostname = ProxyProperty('hostname')
    treatTimeout = ProxyProperty('treatTimeout')
    ssl = ProxyProperty('ssl')
    eventComponent = ProxyProperty('eventComponent')
    command = ProxyProperty('command')
    eventKey = ProxyProperty('eventKey')
    timeout = ProxyProperty('timeout')
    arglist = ProxyProperty('arglist')
    port = ProxyProperty('port')

    @property
    def testable(self):
        ''''''
        return False

