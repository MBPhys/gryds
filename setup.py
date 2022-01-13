import os
import codecs
import setuptools

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


# Add your dependencies in requirements.txt
# Note: you can add test-specific requirements in tox.ini
requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setuptools.setup(
    name="gryds",
    version="0.0.9",
    author="Marc Boucsein, Robin Koch", 
    description="Gryds: a Python package for geometric transformations of images",
    long_description="""
Gryds enables you to make fast geometric transformations of images.
The supported geometric transformations include translations, rigid transformations (translation + rotation),
similarity transformations (translation + rotation + isotropic scaling),
affine transformations (translation + rotation + arbitrary scaling + shearing),
and deformable transformations (modeled as B-splines). It is also possible to apply the transformations to
coordinates in the image domain, and to inspect the deformation vector field.""",
    long_description_content_type="text/markdown",
    url="https://github.com/MBPhys/gryds",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
