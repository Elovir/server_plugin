from setuptools import setup

setup(
    name='server_plugin',
    packages=['server_plugin'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)