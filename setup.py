from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="penligent-ai",
    version="0.1.0",
    author="Penligent AI Team",
    description="Advanced AI-Powered Pentesting Suite for Educational Purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abubkkar55748gcf6-ctrl/Penligent-AI-Free-",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "penligent=penligent.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
