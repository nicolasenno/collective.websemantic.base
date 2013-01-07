#!/usr/bin/env python
# encoding=utf8
from Products.CMFCore.utils import getToolByName
from collective.websemantic.base.controlpanel.stanbolpanel import IStanbolSettings
from collective.websemantic.base.controlpanel.datatxtpanel import IDatatxtSettings
from plone.registry.interfaces import IRegistry
from stanbol.client import Stanbol
from datatxt.client import Datatxt
from zope.app.component.hooks import getSite
from zope.component import getUtility


def get_stanbol(context):
    """
    Utilitary function to access Stanbol preferences
    """
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IStanbolSettings)
    protocol = settings.stanbol_server_protocol
    host = settings.stanbol_server_host
    port = settings.stanbol_server_port
    baseuri = "%s://%s:%s" % (protocol, host, port)
    return Stanbol(baseuri)

def get_datatxt(context):
    """
    Utilitary function to access Datatxt preferences
    """
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IDatatxtSettings)
    app_key = settings.app_key
    app_id = settings.app_id
    lang = settings.app_lang
    api_url = settings.api_url
    rho = settings.rho
    epsilon = settings.epsilon
    long_text = settings.long_text
    prefix = settings.dbpedia
    endpoint = "%s%s" % (prefix, '/sparql')
    return Datatxt(app_key, app_id, lang, api_url, rho, epsilon, long_text, prefix, endpoint)

