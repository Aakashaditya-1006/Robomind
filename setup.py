from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="robomind",
    version="0.1.0",
    author="YOUR_NAME",
    author_email="your@email.com",
    description="Control robots with plain English using local LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/robomind",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
        "pybullet>=3.2.5",
    ],
    keywords="robotics, llm, ai, natural language, pybullet, ros, automation",
)
