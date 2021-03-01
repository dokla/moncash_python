import setuptools 

long_description = """
        Unofficial moncash python sdk provides integration access to the Moncash API.
      """

setuptools.setup(
    name="moncash",
    version="1.0.0",
    description="Moncash Python SDK",
    long_description=long_description,
    author="Madsen Servius",
    author_email="madsen@dokla.ht",
    url="https://github.com/dokla/moncash_python",
    packages=setuptools.find_packages(),
    install_requires=["requests>=2.25.1,<3.0"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)