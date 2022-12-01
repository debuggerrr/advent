from setuptools import setup, find_packages

setup(
    name="advent-challenge",
    version="0.0.1",
    description="advent challenge",
    author="Siddhesh",
    long_description_content_type="text/markdown",
    classifiers=[],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "test": [
            "tox==3.27.0"
        ]
    }
)
