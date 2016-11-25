from setuptools import setup, find_packages

setup(
    name="wghw",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    description="Домашнее задание wargaming.net на позицию Python Developer",
    author='Pavel Bass',
    install_requires=[
        'Django==1.10.3',
        'celery==4.0.0',
        'redis==2.10.5',
    ],
)
