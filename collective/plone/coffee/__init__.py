from Products.CMFCore.utils import ToolInit
from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.FSFile import FSFile
from zope.component import getSiteManager

from collective.plone.coffee.CoffeeRegistry import CoffeeRegistryTool
from collective.plone.coffee.compiler import SubprocessCoffeeCompiler
from collective.plone.coffee import config

def initialize(context):

    manager = getSiteManager(context)
    manager.registerUtility(factory=SubprocessCoffeeCompiler)

    # Register coffee extension to allow it to be used from FS skins
    registerFileExtension('coffee', FSFile)

    TOOLS = (
        CoffeeRegistryTool,
    )

    ToolInit(
        config.PROJECTNAME + ' Tool',
        tools = TOOLS,
        icon = 'tool.gif',
    ).initialize(context)
