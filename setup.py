from setuptools import setup
from setuptools import find_packages
 
VERSION = '2.0.0'
DESCRIPTION = 'Fernet encrypt/decrypt'
LONG_DESCRIPTION = 'A package that provides Fernet encrypt/decrypt functions'
 
# Setting up
setup(
    name="bf_crypto",
    version=VERSION,
    author="""
        Diederick de Buck
        """,
    author_email="""
        diederick.de.buck@blue-fez.com
        """,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    python_requires='>=3.4',
    install_requires=['fernet'],
    keywords=['python', 'crypto', 'fernet'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    license_files = ('LICENSE.txt'),
    options=({'bdist_wheel':{'universal':True}})
)
