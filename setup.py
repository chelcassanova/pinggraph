from cx_Freeze import setup, Executable

base = None

executables = [Executable("pinggraph.py", base=base)]
additional_mods = ['numpy.core._methods', 'numpy.lib.format']

packages = ["idna", "sys", "matplotlib.pyplot", "matplotlib.animation", "ping"]
options = {
    'build_exe': {
        'packages': packages,
        'includes': additional_mods
    },
}

setup(
    name = "<Ping Graph>",
    options = options,
    version = "<0.1>",
    description = 'Converts the ping command into a graph',
    executables = executables
)