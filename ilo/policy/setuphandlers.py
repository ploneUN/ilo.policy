from collective.grok import gs
from ilo.policy import MessageFactory as _

@gs.importstep(
    name=u'ilo.policy', 
    title=_('ilo.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
