from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class Definition():
    """
    """
    version = Version(2, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "zenNrpeComponent" # ZenaPack Name
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
    #dictionary of components
    component = 'NrpeComponent'
    
    packZProperties = []
    
    componentData = {
                  'singular': 'Remote Plugin',
                  'plural': 'Remote Plugins',
                  'displayed': 'eventComponent', # component field in Event Console
                  'primaryKey': 'command',
                  'properties': { 
                        # Basic settings
                        'hostname' : addProperty('Hostname or IP','Basic','id', switch='-H',override=True, isReference=True),
                        'port' : addProperty('Port','Basic', switch='-p'),
                        'ssl' : addProperty('Disable SSL','Basic',False,'boolean', switch='-n'),
                        'command': addProperty('Plugin Command','Basic', switch='-c',optional='false'),
                        'arglist': addProperty('Arguments','Basic',[],'list',switch='-a'),
                        # Misc additional settings
                        'treatTimeout' : addProperty('Timeout UNKNOWN instead of CRITICAL','Miscellaneous',False,'boolean', switch='-u'),
                        'eventComponent' : addProperty('Alias','Display Settings','Remote Plugin',optional='false'),
                        'eventKey' : addProperty('Event Key','Display Settings','/Cmd/Fail'),
                        },
                  }
    
    #dictionary of datasources
    cmdFile = 'check_nrpe'
    provided = False
    cycleTime = 300
    timeout = 60
    datapoints = []                  
                            
