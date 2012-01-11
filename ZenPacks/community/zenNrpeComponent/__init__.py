import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
import os,re

unused(Globals)
""" Add device relations
"""
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
Device._relations += (('nrpeComponents', ToManyCont(ToOne,'ZenPacks.community.zenNrpeComponent.NrpeComponent','nrpeDevice')),)

from Products.ZenUtils.Utils import monkeypatch,prepId

@monkeypatch('Products.ZenModel.Device.Device')
def manage_addNrpeComponent(self, nrpeSSL=True, nrpeCommand='check_users', nrpeFlag='-u', nrpeArgs=[], nrpeEventComponent='NRPE'):
    """make a nrpe component"""
    from NrpeComponent import NrpeComponent
    
    newId = self.id + '_' + re.sub('[^A-Za-z0-9]+', '', nrpeCommand) + '_' + re.sub('[^A-Za-z0-9]+', '', nrpeEventComponent)
    #for arg in nrpeArgs:
    #    newId += '_'+ re.sub('[^A-Za-z0-9]+', '', arg) 
    compid = prepId(newId)
    nrpecomponent = NrpeComponent(compid)
    self.nrpeComponents._setObject(nrpecomponent.id, nrpecomponent)
    nrpecomponent = self.nrpeComponents._getOb(nrpecomponent.id)
    nrpecomponent.nrpeHost = self.manageIp
    nrpecomponent.nrpeSSL = nrpeSSL
    nrpecomponent.nrpeCommand = nrpeCommand
    nrpecomponent.nrpeFlag = nrpeFlag
    nrpecomponent.nrpeArgs = nrpeArgs
    nrpecomponent.nrpeEventComponent = nrpeEventComponent
    return nrpecomponent

class ZenPack(ZenPackBase):
    """ NRPE Component
    """

    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        Device._relations = tuple([x for x in Device._relations if x[0] not in ('nrpeComponents')])
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()
