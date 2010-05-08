# PyOpenGraph

PyOpenGraph is a library written in Python for parsing Open Graph protocol information from web sites.

Learn more about the protocol at:

http://opengraphprotocol.org

## Installation

To install, download the archive at http://pypi.python.org/pypi/PyOpenGraph and decompress, run python setup.py install. 

## Usage

    import PyOpenGraph

    og = PyOpenGraph('http://www.rottentomatoes.com/m/10011268-oceans/')

    print og.metadata # => {'url': 'http://www.rottentomatoes.com/m/10011268-oceans/', 'site_name': 'Rotten
    Tomatoes', 'image': 'http://images.rottentomatoes.com/images/movie/custom/68/10
    011268.jpg', 'type': 'movie', 'title': 'Oceans'}

    print og.metadata['title'] # => Oceans

    og.is_valid() # => return True or False

## License

Copyright (c) 2010 Gerson Minichiello

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.