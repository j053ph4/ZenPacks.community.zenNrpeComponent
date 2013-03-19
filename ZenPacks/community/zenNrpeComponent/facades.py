'''
args:  compFacade,compClass,facadeName,iFacadeName,facadeMethodName, createMethod, singular
'''

import os,re
import logging
log = logging.getLogger('zen.zenNrpeComponentFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from NrpeComponent import *
from .interfaces import *

class zenNrpeComponentFacade(ZuulFacade):
    implements(IzenNrpeComponentFacade)
    
    def addNrpeComponent(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenNrpeComponent.NrpeComponent import NrpeComponent
        import re
        cid = ''
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = NrpeComponent(id)
        relation = target.os.nrpeComponents
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
        setattr(component,"hostname",target.id)
    
    
    

    	return True, _t("Added Remote Plugin for device " + target.id)

