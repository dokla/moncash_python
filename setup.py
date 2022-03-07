from setuptools import setup, find_packages

setup(
    name='moncash',
    version='1.0.3',
    license='MIT',
    description='Simple python wrapper to perform and retrieve payment to Digicel Moncash with Python',
    packages=find_packages('src'),
    package_dir={'': 'src'}, 
    author="Dokla",
    author_email="support@dokla.ht",
    install_requires=["requests>=2.25.1,<3.0"],
)