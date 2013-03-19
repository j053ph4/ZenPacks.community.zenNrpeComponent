from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class NrpeComponent(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'NrpeComponent'
    
    ssl = False
    arglist = []
    command = None
    eventKey = '/Cmd/Fail'
    hostname = ''
    port = None
    eventComponent = 'Remote Plugin'
    treatTimeout = False

    _properties = (
    {'id': 'ssl', 'type': 'boolean','mode': '', 'switch': '-n' },
    {'id': 'arglist', 'type': 'list','mode': '', 'switch': '-a' },
    {'id': 'command', 'type': 'string','mode': '', 'switch': '-c' },
    {'id': 'eventKey', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'hostname', 'type': 'string','mode': '', 'switch': '-H' },
    {'id': 'port', 'type': 'string','mode': '', 'switch': '-p' },
    {'id': 'eventComponent', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'treatTimeout', 'type': 'boolean','mode': '', 'switch': '-u' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'nrpeComponents')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.command
    
    def viewName(self):
        return self.eventComponent
    
    name = titleOrId = viewName


