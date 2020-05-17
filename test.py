import os
import importlib

print(__file__)
print(os.path.abspath(__file__))
cwd = os.getcwd()
name = cwd.split(os.sep)[-1]
print(name)
ns,pkg = name.split('-')
print(ns, pkg)
mypkg = importlib.import_module("%s.%s" % (ns, pkg))
print(dir(mypkg))
NAME = os.path.dirname(os.path.abspath(__file__))
about = importlib.import_module("%s.%s.__about__" % (ns, pkg))
print(about.AUTHOR)
