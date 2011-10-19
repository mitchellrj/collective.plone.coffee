from Products.ResourceRegistries.exportimport.resourceregistry import \
     ResourceRegistryNodeAdapter, importResRegistry, exportResRegistry

from collective.plone.coffee import config
from collective.plone.coffee.interfaces import ICoffeeRegistry

_FILENAME = 'coffeeregistry.xml'
_REG_ID = config.COFFEETOOLNAME
_REG_TITLE = config.COFFEETOOLTITLE

def importCoffeeRegistry(context):
    """
    Import coffeescript registry.
    """
    return importResRegistry(context, _REG_ID, _REG_TITLE, _FILENAME)

def exportCoffeeRegistry(context):
    """
    Export coffeescript registry.
    """
    return exportResRegistry(context, _REG_ID, _REG_TITLE, _FILENAME)


class CoffeeRegistryNodeAdapter(ResourceRegistryNodeAdapter):
    """
    Node im- and exporter for CoffeeRegistry.
    """

    __used_for__ = ICoffeeRegistry
    registry_id = _REG_ID
    resource_type = 'coffeescript'
    register_method = 'registerScript'
    update_method = 'updateScript'
