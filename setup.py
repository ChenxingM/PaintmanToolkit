from setuptools import setup, find_packages

setup(
    name="PaintmanToolkit",
    version="1.0.3",
    author="Ma Chenxing",
    author_email="tammcx@gmail.com",
    description="A toolkit for reading and generating Paintman related files for color management.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChenxingM/PaintmanToolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 支持的 Python 版本
)
