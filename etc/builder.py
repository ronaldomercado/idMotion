from iocbuilder import AutoSubstitution
#, ModuleBase, records, Device, Xml
from iocbuilder.hardware import Calc

class IDGapSoftMotorTemplate(AutoSubstitution):
    Dependencies = (Calc,)
    TemplateFile = 'IDGapSoftMotor.template'

class id4AxisGui(AutoSubstitution):
    TemplateFile = 'ID_4VAxis_gui.template'
