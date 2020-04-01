import setuptools
with open("README.md", "r") as readme:
    long_description = readme.read()
setuptools.setup(
    name="covid19-openapi",
    version="0.0.1",
    author="Natworpong Loyswai",
    author_email="Natworpong.Loyswai@mail.kmutt.ac.th",
    description="Thailand Covid-19 status.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)