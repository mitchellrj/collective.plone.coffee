from cStringIO import StringIO
import shlex
import subprocess

from zope.interface import implements

from collective.plone.coffee import config
from collective.plone.coffee.interfaces import ICoffeeCompiler


class SubprocessCoffeeCompiler(object):
    """ Calls the coffee compiler program on the host machine to
        compile to Javascript.
    """

    implements(ICoffeeCompiler)

    def __call__(self, content):

        cmd = shlex.split('%s %s' % (config.COFFEE_EXECUTABLE,
                                     config.COFFEE_SWITCHES))

        p = None
        try:
            p = subprocess.Popen(cmd,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)

            result = p.communicate(input=content)[0]
        except (OSError, subprocess.CalledProcessError), e:
            result = str(e)

        if not p or p.returncode>0:
            errors = result
            errors.replace('/*', '\\/*').replace('*/', '*\\/')
            return '/* Error compiling CoffeeScript! */\n' + \
                   '/*\n%s\n*/' % (errors,)

        return result