import os,re
import logging
log = logging.getLogger('zen.zenNrpeComponentfacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from NrpeComponent import NrpeComponent
from .interfaces import IzenNrpeComponentFacade


class zenNrpeComponentFacade(ZuulFacade):
    implements(IzenNrpeComponentFacade)

    def addNrpeComponent(self, ob, nrpeCommand='check_users', nrpeFlag='-u', nrpeArgs=[], nrpeEventComponent='NRPE'):
        """ Adds NRPE Component URL monitor"""
        id = ob.id + '_' + re.sub('[^A-Za-z0-9]+', '', nrpeCommand)+ '_' + re.sub('[^A-Za-z0-9]+', '', nrpeEventComponent)
        #for arg in nrpeArgs:
        #    newId += '_'+ re.sub('[^A-Za-z0-9]+', '', arg) 
        nrpecomponent = NrpeComponent(id)
        ob.nrpeComponents._setObject(nrpecomponent.id, nrpecomponent)
        nrpecomponent = ob.nrpeComponents._getOb(nrpecomponent.id)
        nrpecomponent.nrpeHost = ob.manageIp
        nrpecomponent.nrpeSSL = True
        nrpecomponent.nrpeCommand = nrpeCommand
        nrpecomponent.nrpeFlag = nrpeFlag
        nrpecomponent.nrpeArgs = nrpeArgs
        nrpecomponent.nrpeEventComponent = nrpeEventComponent

        return True, _t(" Added Remote Plugin Check for device %s" % (ob.id))
