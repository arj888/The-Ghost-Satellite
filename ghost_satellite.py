from setuptools import setup

setup(
    name="ghost_satellite",
    version="1.0",
    description="Minimal Space SSA Defense Package",
    py_modules=["ghost_satellite"],
    install_requires=[
        "requests",
        "skyfield",
    ],
)
