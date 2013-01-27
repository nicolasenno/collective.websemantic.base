from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from collective.websemantic.base.utils import get_stanbol, get_datatxt

def indexer_handler(obj, event):
    try:
        transforms = getToolByName(obj, 'portal_transforms')
        stream = transforms.convertTo('text/plain', obj.getText(), mimetype='text/html')
        text = stream.getData().strip()
#        obj._stanbol_enhancements = stanbol.engines(text, 'rdfjson')
        import pdb;pdb.set_trace()
        datatxt = get_datatxt(obj)
        tags = datatxt.tags(text)
        obj.setSubject(tags)

    except Exception, e:
        msg = "Problem while using Stanbol server for automatic " + \
              "enhancement.\n%s" % str(e)
        IStatusMessage(obj.REQUEST).addStatusMessage(msg, type='error')
