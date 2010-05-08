from distutils.core import setup

setup(
    name = 'PyOpenGraph',
    version = '0.2',
    description = 'PyOpenGraph is a library written in Python for parsing Open Graph protocol information from web sites.',
    author = 'Gerson Minichiello',
    author_email = 'gerson.minichiello@gmail.com',
    url='http://github.com/minichiello/PyOpenGraph',
    download_url = 'http://pypi.python.org/pypi/PyOpenGraph',
    platforms = 'Any',
    license = 'MIT License',
    long_description='''\
=============
 PyOpenGraph
=============
    
PyOpenGraph is a library written in Python for parsing Open Graph protocol information from web sites.

Learn more about the protocol at:

http://opengraphprotocol.org

--------------
 Installation
--------------

To install, download the archive at http://pypi.python.org/pypi/PyOpenGraph and decompress, run python setup.py install.

-------
 Usage
-------
::

    import PyOpenGraph

    og = PyOpenGraph('http://www.rottentomatoes.com/m/10011268-oceans/')

    print og.metadata # => {'url': 'http://www.rottentomatoes.com/m/10011268-oceans/', 'site_name': 'Rotten Tomatoes', 'image': 'http://images.rottentomatoes.com/images/movie/custom/68/10011268.jpg', 'type': 'movie', 'title': 'Oceans'}

    print og.metadata['title'] # => Oceans

    og.is_valid() # => return True or False
''',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)