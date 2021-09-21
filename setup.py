from setuptools import setup, find_packages

print(find_packages())
setup(
    name='pygments-molokai',
    packages=find_packages(),
    package_data={ '' : ['*.*'] },
    include_package_data=True,
    entry_points=
    """
    [pygments.styles]
    molokai = molokai.molokai:MolokaiStyle
    """,
)
