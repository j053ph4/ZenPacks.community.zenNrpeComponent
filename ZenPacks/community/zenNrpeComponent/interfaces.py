
'''
args: componentInterface,comopnentInterfaceproperties,componentIFacade,iFacadeMethodName
'''

from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class INrpeComponentInfo(IComponentInfo):
    ssl = schema.Bool(title=_t(u'Disable SSL'))
    arglist = schema.List(title=_t(u'Arguments'))
    command = SingleLineText(title=_t(u'Plugin Command'))
    eventKey = SingleLineText(title=_t(u'Event Key'))
    hostname = SingleLineText(title=_t(u'Hostname or IP'))
    port = SingleLineText(title=_t(u'Port'))
    eventComponent = SingleLineText(title=_t(u'Alias'))
    treatTimeout = schema.Bool(title=_t(u'Timeout UNKNOWN instead of CRITICAL'))



class IzenNrpeComponentFacade(IFacade):
    def addNrpeComponent(self, ob, **kwargs):
        ''''''

'''
args : dsinterface,dsinterfaceproperties
'''

# datasource interface
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class INrpeComponentDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (s)'))
    hostname = SingleLineText(title=_t(u'Hostname or IP'))
    treatTimeout = schema.Bool(title=_t(u'Timeout UNKNOWN instead of CRITICAL'))
    ssl = schema.Bool(title=_t(u'Disable SSL'))
    eventComponent = SingleLineText(title=_t(u'Alias'))
    command = SingleLineText(title=_t(u'Plugin Command'))
    eventKey = SingleLineText(title=_t(u'Event Key'))
    timeout = SingleLineText(title=_t(u'Timeout (s)'))
    arglist = schema.List(title=_t(u'Arguments'))
    port = SingleLineText(title=_t(u'Port'))


