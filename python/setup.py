from setuptools import setup, find_packages
import os

# Get the directory containing setup.py
HERE = os.path.abspath(os.path.dirname(__file__))

# Read the root README.md
README_PATH = os.path.join(HERE, "..", "README.md")

with open(README_PATH, "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Get version from __init__.py
def get_version():
    init_path = os.path.join(
        HERE,
        "minecraft_server_utility",
        "__init__.py"
    )

    with open(init_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")

    return "1.0.0"


setup(
    name="minecraft-server-utility",
    version=get_version(),
    author="darkboy0p",
    author_email="wardengamerofficial@gmail.com",
    description="A comprehensive library for interacting with Minecraft servers",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/darkboy0p/minecraft-server-utility",

    project_urls={
        "Bug Tracker": "https://github.com/darkboy0p/minecraft-server-utility/issues",
        "Documentation": "https://github.com/darkboy0p/minecraft-server-utility#readme",
        "Source Code": "https://github.com/darkboy0p/minecraft-server-utility",
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(),

    python_requires=">=3.7",

    install_requires=[
        "requests>=2.25.0",
    ],

    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "twine>=4.0.0",
            "build>=0.10.0",
        ],
    },

    keywords=[
        "minecraft",
        "server",
        "ping",
        "utility",
        "api",
        "mojang",
        "bedrock",
        "java",
        "gaming",
        "minecraft-server",
        "server-status",
    ],

    license="MIT",
    platforms=["any"],
    include_package_data=True,
    zip_safe=False,
)
