from setuptools import setup, find_packages

setup(
    name='zebraPrinter',
    version='0.1.0',
    description=(
        "it is a package for zebra printer by zlpII"
    ),
    long_description=open('README.rst').read(),
    author='SimonXu',
    author_email='<你的邮件地址>',
    maintainer='<维护人员的名字>',
    maintainer_email='<维护人员的邮件地址',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='<项目的网址，我一般都是github的url>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)