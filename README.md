AYERINUMBERS.PY
===============

Converts numbers to [Ayeri](http://benung.nfshost.com) number words. It currently only converts integer numbers, no fractions decimal or otherwise.

Executing the Script
--------------------

You'll need Python 3 for this. Note that this is a *command-line program*. `python ayerinumbers.py -h` gives you some advice on the input:

    positional arguments:
      n                     an integer number 0 <= n < 12^44

    optional arguments:
      -h, --help            show this help message and exit
      -s, --show-conversion show the conversion into base 12
      
You may need to call the python script by prefixing either `python` or `python3`,
or make it executable e.g. by `cd`ing to the directory the file is in, and then 
doing `chmod +x ayerinumbers.py`. You should then be able to just start the 
program with `./ayerinumbers.py`.

Some input/output examples:
    
    $ ./ayerinumbers.py 54292
    samang sam menang itolan-iri nay yo
    
    $ ./ayerinumbers.py 5106212
    samang menang men henlan-miye menang samlan-tam veyalan-hen
    
    $ ./ayerinumbers.py 636
    menang yo irilan
    
    $ ./ayerinumbers.py -s 20736
    1,0000₁₂: samang men
    
    $ ./ayerinumbers.py --show-conversion 3457
    2001₁₂: menang samlan nay men    

Disclaimer
----------

This software comes "as-is" with no warranties expressed or implied.
