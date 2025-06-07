from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservation_mlops",
    version="0.2",
    author="Sanat Walia",
    author_email="codersanat896@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)
