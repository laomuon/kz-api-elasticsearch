from setuptools import setup, find_packages

setup(
    name="kz-api-elasticsearch",
    version="0.0.1",
    author="zer0K-z",
    packages=find_packages(),
    license="MIT",
    description="Continuously upload kz records to an elastic node",
    install_requires=["elasticsearch"],
    zip_safe=False,
)