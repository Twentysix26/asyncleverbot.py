from distutils.core import setup

setup(
    name='asyncleverbot',
    version='1.0.0',
    url='https://github.com/Twentysix26/asyncleverbot.py',
    download_url='https://github.com/Twentysix26/asyncleverbot.py/tarball/1.0.0',
    author='Twentysix (originally created by: Rodney Folz)',
    description='Unofficial async library to access the Cleverbot API',
    license='BSD-2-Clause',
    packages=['asyncleverbot'],
    install_requires=['aiohttp'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
