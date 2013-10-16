from setuptools import setup, find_packages
import os

version = __import__('beltbadgers_com').__version__
#version = "2.0"

install_requires = [
    'django',
    'south',
    'django-belts',
    'django-autoslug',
    'django-tinymce',
]

setup(
    name = "beltbadgers_com",
    version = version,
    url = 'http://github.com/powellc/beltbadgers_com',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "The site that powers beltbadgers.com",
    author = "Colin Powell",
    author_email = 'colin.powell@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'beltbadgers_com': 'beltbadgers_com',
    },
)
