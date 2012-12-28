from collective.websemantic.base.utils import get_stanbol
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName

def indexer_handler(obj, event):
    obj._stanbol_enhancements = None
    stanbol = get_stanbol(obj)
    try:
        import pdb;pdb.set_trace()
        transforms = getToolByName(obj, 'portal_transforms')
        stream = transforms.convertTo('text/plain', obj.getText(), mimetype='text/html')
        text = stream.getData().strip()
#        obj._stanbol_enhancements = stanbol.engines(text, 'rdfjson')
        
        datatxt = get_datatxt(obj)
        res = datatxt.annotate(text)

    except Exception, e:
        msg = "Problem while using Stanbol server for automatic "+\
              "enhancement.\n%s" % str(e)
        IStatusMessage(obj.REQUEST).addStatusMessage(msg, type='error')
