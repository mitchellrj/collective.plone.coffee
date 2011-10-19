from Acquisition import aq_inner
from Products.ResourceRegistries.browser.scripts import ScriptsView
from Products.CMFCore.utils import getToolByName

from collective.plone.coffee import config

class CoffeeView(ScriptsView):
    """ Information for script rendering. """

    def registry(self):
        return getToolByName(aq_inner(self.context), config.COFFEETOOLNAME)

    def include_compiler(self):
        return self.registry().getDebugMode()