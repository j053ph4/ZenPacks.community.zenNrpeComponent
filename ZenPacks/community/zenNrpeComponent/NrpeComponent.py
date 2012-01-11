################################################################################
#
# This program is part of the zenNrpeComponent Zenpack for Zenoss.
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
   
class NrpeComponent(DeviceComponent, ManagedEntity):
    """
    NrpeComponent contains the basic properties of a NrpeComponent
    """
    portal_type = meta_type = 'NrpeComponent'
    
    nrpeHost = ''
    nrpeSSL = False
    nrpeCommand = ''
    nrpeFlag = '-u'
    nrpeArgs = []
    nrpeEventComponent = 'NRPE'

    _properties = (
        {'id':'nrpeHost', 'type':'string', 'mode':''},     
        {'id':'nrpeSSL', 'type':'boolean', 'mode':''},
        {'id':'nrpeCommand', 'type':'string', 'mode':''},
        {'id':'nrpeFlag', 'type':'string', 'mode':''},
        {'id':'nrpeArgs', 'type':'lines', 'mode':''},
        {'id':'nrpeEventComponent', 'type':'string', 'mode':''},
        )

    _relations = (
        ('nrpeDevice', ToOne(ToManyCont,'Products.ZenModel.Device.Device', 'nrpeComponent')),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)
    
    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
    
    def viewName(self):
        return self.nrpeCommand
    titleOrId = name = viewName

    def primarySortKey(self):
        return self.nrpeCommand
    
    def getStatus(self):
        return self.statusMap()
    
    def statusMap(self):
        """ map run state to zenoss status
        """
        self.status = 0
        return self.status
    
    def device(self):
        return self.nrpeDevice()

    def manage_deleteComponent(self, REQUEST=None):
        url = None
        if REQUEST is not None:
            url = self.device().nrpeComponents.absolute_url()
        self.getPrimaryParent()._delObject(self.id)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)


