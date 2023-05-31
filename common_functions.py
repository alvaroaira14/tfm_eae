import importlib

def modules(module_name):
    try:
        importlib.import_module(module_name)

    except ModuleNotFoundError:
        import pip
        pip.main(['install', module_name])
        importlib.import_module(module_name)