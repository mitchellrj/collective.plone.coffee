=======================
collective.plone.coffee
=======================

Adds a CoffeeScript resource registry to Plone. When in debug mode,
your CoffeeScript resources are included in the page along with the
compiler script. When not in debug mode, scripts are compiled to
JavaScript and then handled as they would normally be by the
JavaScript registry with regard to compression & caching.

Requires the ``coffee`` compiler to be installed on the host machine
and on the system path.

More information at http://coffeescript.org/