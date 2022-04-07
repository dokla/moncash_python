from setuptools import setup

setup(
    name='moncash',
    version='1.0.3',
    license='MIT',
    description='Simple python wrapper to perform and retrieve payment to Digicel Moncash with Python',
    packages=["moncash", "moncash.exceptions"],
    package_dir={'': 'moncash'}, 
    author="Dokla",
    author_email="support@dokla.ht",
    install_requires=["requests>=2.25.1,<3.0"],
)