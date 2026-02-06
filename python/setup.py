from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="minecraft-server-utility",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive library for interacting with Minecraft servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/minecraft-server-utility",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities"
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords=[
        "minecraft",
        "server",
        "ping",
        "utility",
        "api",
        "mojang",
        "bedrock",
        "java"
    ],
    project_urls={
        "Bug Reports": "https://github.com/darkboy0p/minecraft-server-utility/issues",
        "Source": "https://github.com/darkboy0p/minecraft-server-utility",
    },
)
