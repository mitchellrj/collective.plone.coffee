from setuptools import setup, find_packages

version = '0.0.1'

tests_require = []

setup(name='collective.plone.coffee',
      version=version,
      description="Adds a resource registry for CoffeeScript in Plone",
      long_description='\n'.join([open(f).read() for f in (
                            'README.rst',
                            'HISTORY.rst',
                            'LICENSE.rst')]),
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone coffee script coffeescript javascript resource registry resourceregistry',
      author='Richard Mitchell',
      author_email='mitchell@awesomeco.de',
      url='http://github.com/mitchellrj/collective.plone.coffee',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test':tests_require,
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
