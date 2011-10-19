from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ResourceRegistries.tools.BaseRegistry import BaseRegistryTool
from Products.ResourceRegistries.tools.JSRegistry import JavaScript
from Products.ResourceRegistries.tools.JSRegistry import JSRegistryTool
from zope.component import getUtility
from zope.interface import implements

from collective.plone.coffee import config
from collective.plone.coffee.interfaces import ICoffeeCompiler
from collective.plone.coffee.interfaces import ICoffeeRegistry


class CoffeeScript(JavaScript):

    def __init__(self, id, **kwargs):
        super(CoffeeScript, self).__init__(id, **kwargs)


InitializeClass(CoffeeScript)


class CoffeeRegistryTool(JSRegistryTool):
    """A Plone registry for managing the linking to Coffeescript files."""

    id = config.COFFEETOOLNAME
    meta_type = config.COFFEETOOLTYPE
    title = config.COFFEETOOLTITLE

    security = ClassSecurityInfo()

    implements(ICoffeeRegistry)

    #
    # ZMI stuff
    #

    manage_coffeeForm = PageTemplateFile('www/coffeeconfig', config.GLOBALS)
    manage_coffeeComposition = PageTemplateFile('www/coffeebrew', config.GLOBALS)

    manage_options = (
        {
            'label': 'CoffeeScript Registry',
            'action': 'manage_coffeeForm',
        },
        {
            'label': 'Merged Coffee Composition',
            'action': 'manage_coffeeComposition',
        },
    ) + BaseRegistryTool.manage_options

    filename_appendix = '.coffee'
    merged_output_prefix = u"""
/* Merged, compiled Plone CoffeeScript file
 * This file is dynamically assembled from separate CoffeeScript parts.
 * Some of these parts have 3rd party licenses or copyright information attached
 * Such information is valid for that section,
 * not for the entire composite file
 * originating files are separated by - filename.js -
 */
"""
    resource_class = CoffeeScript

    security.declarePrivate('compileCoffee')
    def compileCoffee(self, content):

        compiler = getUtility(ICoffeeCompiler)
        content = compiler(content)

        return content

    security.declarePrivate('finalizeContent')
    def finalizeContent(self, resource, content):
        if not self.getDebugMode():
            content = self.compileCoffee(content)
        base = super(CoffeeRegistryTool, self)
        return base.finalizeContent(resource, content)


InitializeClass(CoffeeRegistryTool)