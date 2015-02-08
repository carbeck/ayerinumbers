AYERINUMBERS.PY
===============

Converts numbers to [Ayeri](http://benung.nfshost.com) number words. So far (February 4, 2015) only converts integer numbers, no fractions.

Executing the Script
--------------------

You'll need Python 3 for this. Note that this is a *command-line program*. `python ayerinumbers.py -h` gives you some advice on the input:

    positional arguments:
      n                     an integer number n >= 0

    optional arguments:
      -h, --help            show this help message and exit
      -s, --show-conversion show the conversion into base 12

Some output examples:
    
    $ ./ayerinumbers.py 54292
    samang sam menang itolan-iri nay yo
    
    $ ./ayerinumbers.py 5106212
    samang menang men henlan-miye menang samlan-tam veyalan-hen
    
    $ ./ayerinumbers.py 636
    menang yo irilan
    
    $ ./ayerinumbers.py -s 20736
    10000₁₂: samang men
    
    $ ./ayerinumbers.py --show-conversion 3457
    2001₁₂: menang samlan nay men    

Disclaimer
----------

This software comes "as-is" with no warranties expressed or implied.
