from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='django-huey-logger',
    version='1.0.0',
    url='https://github.com/lotrekagency/django-huey-logger',
    long_description=long_description,
    description="A simple Django app to let you know if huey tasks are working without errors.",
    license="MIT",
    author="Gabriele Baldi",
    author_email="gabriele.baldi.01@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
