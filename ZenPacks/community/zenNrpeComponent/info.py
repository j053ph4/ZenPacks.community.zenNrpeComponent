from ZenPacks.community.ConstructionKit.ClassHelper import *

def NrpeComponentgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class NrpeComponentInfo(ClassHelper.NrpeComponentInfo):
    ''''''

from ZenPacks.community.zenNrpeComponent.datasources.NrpeComponentDataSource import *
def NrpeComponentRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(NrpeComponentDataSource.onRedirectOptions)

class NrpeComponentDataSourceInfo(ClassHelper.NrpeComponentDataSourceInfo):
    ''''''


