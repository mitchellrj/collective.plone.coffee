from Products.ResourceRegistries.interfaces import IJSRegistry
from zope.interface import Attribute
from zope.interface import Interface


class ICoffeeRegistry(IJSRegistry):

    id = Attribute('id',
                   """ The tool's ID.

                   o Must be set to 'portal_coffee'.
                   """)


class ICoffeeCompiler(Interface):

    def __call__(self, content):
        """ Take CoffeeScript as a string, return JavaScript as a
            string.
        """
