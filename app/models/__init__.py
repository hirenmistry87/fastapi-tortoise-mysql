import pkgutil
import importlib
import inspect

from tortoise.models import Model

__all__ = []

for module_info in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_info.name}")

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, Model) and obj is not Model:
            globals()[name] = obj
            __all__.append(name)
