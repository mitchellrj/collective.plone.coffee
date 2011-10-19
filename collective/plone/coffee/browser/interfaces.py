from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class ICoffeeView(Interface):

    def scripts():
        """ Returns a list of dicts with information for scripts rendering. """


class IHtmlHeadCoffee(IViewletManager):
    """ A viewlet manager for coffeescripts. """