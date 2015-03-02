from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

def addArgs(ob, context, data={}):
    ''' evaluate and return command line args '''
    parts = []
    args = str(getattr(context, 'arglist',''))
    if len(args) > 0:
        split_by_space = args.split(' ')
        split_by_newline = args.split('\n')
        values = split_by_newline
        if len(split_by_space) > len(split_by_newline):
            values = split_by_space
        parts.append('%s \"%s\"' % (data['arglist']['switch'], '\" \"'.join(values)))
    return parts

NrpeDefinition = type('NrpeDefinition', (BasicDefinition,), {
        'version' : Version(2, 2, 0),
        'zenpackbase': "zenNrpeComponent",
        'component' : 'NrpeComponent',
        'componentData' : {
              'singular': 'Remote Nagios',
              'plural': 'Remote Nagios',
              'displayed': 'eventComponent',
              'primaryKey': 'command',
              'properties': {
                    'hostname' : addProperty('Hostname or IP','Basic','id', switch='-H',override=True, isReference=True),
                    'port' : addProperty('Port','Basic','5666', switch='-p'),
                    'ssl' : addProperty('Disable SSL','Basic',False,'boolean', switch='-n'),
                    'timeout' : addProperty('Timeout','Basic','30',switch='-t'),
                    'command': addProperty('Plugin Command','Basic','check_log',switch='-c',optional='false'),
                    'arglist': addProperty('Arguments','Basic','path/to/log\n0\nstring_to_find','list',switch='-a'),
                    'treatTimeout' : addProperty('Timeout UNKNOWN instead of CRITICAL','Miscellaneous',False,'boolean', switch='-u'),
                    'eventComponent' : addProperty('Alias','Display Settings','Remote Plugin',optional='false'),
                    'eventClass' : getEventClass('/Cmd/Fail'),
                    },
              },
        'componentMethods': [],
        'cmdFile':'check_nrpe',
        'addManual' : True,
        'createDS' : True,
        'ignoreKeys' : ['arglist'],
        'datasourceMethods' : [addArgs],
        'saveOld': True,
        'loadOld': True,
        }
)

addDefinitionSelfComponentRelation(NrpeDefinition,
                          'nrpecomponents', ToMany, 'ZenPacks.community.zenNrpeComponent.NrpeComponent','port',
                          'ipservice',  ToOne, 'Products.ZenModel.IpService', 'port',
                          'IP Service', 'port')

