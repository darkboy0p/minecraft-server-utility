from setuptools import setup, find_packages
from pathlib import Path
import re


# ============================================================
# Paths
# ============================================================

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

README_PATH = ROOT / "README.md"
PACKAGE_DIR = HERE / "minecraft_server_utility"
INIT_PATH = PACKAGE_DIR / "__init__.py"


# ============================================================
# Read README
# ============================================================

if README_PATH.exists():
    with README_PATH.open("r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = (
        "A comprehensive Python library for interacting "
        "with Minecraft servers."
    )


# ============================================================
# Get package version
# ============================================================

def get_version():
    """Read __version__ from minecraft_server_utility/__init__.py."""

    if not INIT_PATH.exists():
        return "1.0.0"

    content = INIT_PATH.read_text(encoding="utf-8")

    match = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
        content,
        re.MULTILINE,
    )

    if match:
        return match.group(1)

    return "1.0.0"


# ============================================================
# Setup
# ============================================================

setup(
    name="minecraft-server-utility",

    version=get_version(),

    author="darkboy0p",
    author_email="wardengamerofficial@gmail.com",

    description=(
        "A comprehensive library for interacting "
        "with Minecraft servers"
    ),

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/darkboy0p/minecraft-server-utility",

    project_urls={
        "Bug Tracker": (
            "https://github.com/darkboy0p/"
            "minecraft-server-utility/issues"
        ),
        "Documentation": (
            "https://github.com/darkboy0p/"
            "minecraft-server-utility#readme"
        ),
        "Source Code": (
            "https://github.com/darkboy0p/"
            "minecraft-server-utility"
        ),
    },

    # ========================================================
    # Package discovery
    # ========================================================

    package_dir={
        "": "."
    },

    packages=find_packages(
        where="."
    ),

    # ========================================================
    # Python compatibility
    # ========================================================

    python_requires=">=3.7",

    # ========================================================
    # Dependencies
    # ========================================================

    install_requires=[
        "requests>=2.25.0",
    ],

    # ========================================================
    # Optional dependencies
    # ========================================================

    extras_require={
        "discord": [
            "discord.py>=2.0.0",
        ],

        "web": [
            "flask>=2.0.0",
        ],

        "cli": [
            "click>=8.0.0",
        ],

        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "twine>=4.0.0",
            "build>=0.10.0",
        ],

        "all": [
            "discord.py>=2.0.0",
            "flask>=2.0.0",
            "click>=8.0.0",
        ],
    },

    # ========================================================
    # Package metadata
    # ========================================================

    keywords=[
        "minecraft",
        "minecraft-server",
        "server",
        "server-status",
        "ping",
        "utility",
        "api",
        "mojang",
        "bedrock",
        "java",
        "gaming",
        "player",
        "minecraft-api",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Topic :: Software Development :: Libraries",
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

    license="MIT",

    platforms=["any"],

    include_package_data=True,

    zip_safe=False,
)
