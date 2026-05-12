from iocbuilder import AutoSubstitution
#, ModuleBase, records, Device, Xml
from iocbuilder.hardware import Calc

class idmGui(AutoSubstitution):
    TemplateFile = 'IDM_gui.template'

class idmDefer(AutoSubstitution):
    TemplateFile = 'IDM_defer.template'

class idmEncSync(AutoSubstitution):
    TemplateFile = 'IDM_encSync.template'
