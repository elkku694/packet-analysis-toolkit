from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="packet-analysis-toolkit",
    version="1.0.0",
    author="Educational Project",
    description="A comprehensive educational tool for packet capture, analysis, and manipulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elkku694/packet-analysis-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Education",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.11",
    install_requires=[
        "scapy>=2.5.0",
        "PyQt6>=6.6.1",
        "matplotlib>=3.8.2",
        "numpy>=1.24.3",
    ],
    entry_points={
        "console_scripts": [
            "packet-toolkit=src.main:main",
        ],
    },
)
