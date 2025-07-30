# This is a setup.py file from meta-llama/llama repository  
# Added to dev-jane branch for LLM model support

from setuptools import setup, find_packages

# Basic setup configuration based on meta-llama repository structure
setup(
    name="modelhub-llama",
    version="0.1.0", 
    description="ModelHub with Llama model support for large language model inference",
    author="Jane",
    author_email="jane@university.edu",
    packages=find_packages(),
    install_requires=[
        "torch>=1.8.0",
        "fire",
        "sentencepiece",
        "numpy",
        "fairscale>=0.4.4",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers", 
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)