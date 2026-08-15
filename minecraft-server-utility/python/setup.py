from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).resolve().parent

README = HERE / "README.md"

with open(README, "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version():
    """Get version from version.py"""
    version_file = HERE / "minecraft_server_utility" / "version.py"
    
    with open(version_file, "r", encoding="utf-8") as f:
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
            "pytest-mock>=3.10.0",
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

    platforms=["any"],

    include_package_data=True,
    zip_safe=False,
)
