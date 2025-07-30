# This is a setup.py file from huggingface/accelerate repository
# Added to dev-kai branch as part of initial framework setup

from setuptools import setup, find_packages

def get_version():
    """Get version from __init__.py file"""
    version_dict = {}
    with open("src/accelerate/__init__.py", "r") as version_file:
        exec(version_file.read(), version_dict)
    return version_dict["__version__"]

# Basic setup configuration based on accelerate repository structure
setup(
    name="modelhub",
    version="0.1.0",
    description="A framework for running and accelerating Large Language Models",
    author="Kai",
    author_email="kai@university.edu",
    packages=find_packages(),
    install_requires=[
        "torch>=1.10.0",
        "numpy",
        "packaging>=20.0",
        "psutil",
        "pyyaml",
        "huggingface-hub",
        "safetensors>=0.3.1",
    ],
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)