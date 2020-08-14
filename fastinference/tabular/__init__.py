from ..soft_dependencies import SoftDependencies
if not SoftDependencies.check()['interp']:
    raise ImportError("The interp module is not installed.")

from .shap import *
from .interpretation import *
