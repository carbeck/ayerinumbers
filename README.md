AYERINUMBERS.PY
===============

Converts numbers to [Ayeri](http://benung.nfshost.com) number words. So far (February 4, 2015) only converts integer numbers, no fractions.

Executing the Script
--------------------

You'll need Python 3 for this. Note that this is a *command-line program*. `python ayerinumbers.py -h` gives you some advice on the input:

    positional arguments:
    n           An integer number between 0 and (10^40)₁₂

Some output examples:
    
    $ ./ayerinumbers.py 54292
    27504: samang sam menang itolan-iri nay yo
    
    $ ./ayerinumbers.py 5106212
    1862B98: samang menang men henlan-miye menang samlan-tam veyalan-hen
    
    $ ./ayerinumbers.py 636
    450: menang yo irilan
    
    $ ./ayerinumbers.py 20736
    10000: samang men
    
    $ ./ayerinumbers.py 3457
    2001: menang samlan nay men    

Disclaimer
----------

This software comes "as-is" with no warranties expressed or implied.