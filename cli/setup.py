from setuptools import setup, find_packages
import os                                                                                                                                            

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bhej",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="Send files like a developer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhruv4/bhej",
    packages=find_packages('bhej'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bhej = bhej.main:app',
        ]
    },
    install_requires=[
        'requests',
        'python-magic',
        'typer',
        'python-dotenv'
    ],
    python_requires='>=3.6',
)