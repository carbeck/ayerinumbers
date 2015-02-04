#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' ayerinumbers.py -- Converts numbers to Ayeri number words
'''

# Copyleft 2015 Carsten Becker <carbeck@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import math
import sys

pword = {
    1: 'lan',           #  1    element
    2: 'menang',        #  2    elements
    4: 'samang',        #  3- 4 elements
    8: 'kaynang',       #  5- 6 elements
    12:'yonang',        #  7- 8 elements
    16:'irinang',       #  9-10 elements
    20:'miyenang',      # 11-12 elements
    24:'itonang',       # 13-14 elements
    28:'henang',        # 15-16 elements
    32:'veyanang',      # 17-18 elements
    36:'malnang',       # 19-20 elements
    40:'tamang',        # 21-22 elements
}

nword = {
    '0':'ja',
    '1':'men',
    '2':'sam',
    '3':'kay',
    '4':'yo',
    '5':'iri',
    '6':'miye',
    '7':'ito',
    '8':'hen',
    '9':'veya',
    'A':'mal',
    'B':'tam',
}

pnword = {}
for i, x in enumerate([pword[i] for i in sorted(pword)]):
    pnword[str(i+1)] = x

def c(n):
    '''Convert number > 9 to a string ABCDE…'''
    if(n > 9):
        n = chr(n + 55);
    return n

def baseconv(n, b = 12):
    '''Convert an integer number n in base 10 to another'''
    n = int(math.floor(float(n)))
    s = ''
    while n > 0:
        r = n % b       # remainder
        n = n // b      # integer
        s = str(c(r)) + str(s)
    return s

def numword_bigram(n):
    '''Take a number bigram (str!) and return the corresponding number word.'''
    
    # Instantiate empty string as a container
    s = ''
    
    if len(n) < 2:
        if n[0] != '0':
            s = '{}'.format(nword[n[0]])
    else:
        if n[0] != '0':
            s = '{}{} '.format(nword[n[0]], pword[1])
        elif n[0] == '0' and n[1] != '0':
            s = 'nay '
        
        if n[1] != '0':
            s += '{}'.format(nword[n[1]])
    
    return s.strip()

def split_num(s):
    '''Split into list with the format [[00,00],[00,00], ...]'''
    
    # Splitting into groups of 4
    sp = " ".join(s[::-1][i:i+4] for i in range(0,len(s), 4))[::-1].split()

    # Splitting into subgroups of 2
    for i,n in enumerate(sp):
        sp[i] = " ".join(n[::-1][i:i+2] for i in range(0,len(n), 2))[::-1].split()
    
    return sp

def count_elements(l):
    '''Count the number of elements in the list on the 1st sublevel'''
    return sum(len(x) for x in l)

def get_power(i):
    '''Gets the word for the respective power from number of elements'''
    pow = i * 2 - 2
    
    if pow in pword:
        return pword[pow]
    
    elif pow not in pword and pow < max(pword):
        flag = True
        p = 0
        while flag:
            for x in sorted([n for n in pword]):
                if x > pow:
                    flag = False
                else:
                    p = x
        return pword[p]

def numberword(n):
    '''The function to form the number word.'''
    
    # Make n a string if it's not yet provided as such
    # (Thing is, we're dealing with base 12, so normal number manipulation 
    # doesn't work because that's all in base 10)
    n = str(n)
    
    # In case it's zero
    if n == '0':
        return nword[n]
    
    # Otherwise, instantiate new list to collect converted strings in:
    s = []
    
    # Split the number up into myriads and hundreds
    n = split_num(n)
    
    # The highest power word
    if count_elements(n) > 2:
        s.append(get_power(count_elements(n)))
    
    for i, myrgrp in enumerate(n):
        # Get the word for power of the element in the group
        if len(n[i]) > 1 and n[i][0] != '00':
            s.append(get_power(len(n[i])))
        
        # For each group of hundreds, get the number word
        for j, hungrp in enumerate(n[i]):
            s.append(numword_bigram(n[i][j]))
    
    return ' '.join(filter(None, s))

def main(argv=None):
    """Main function providing command line option parser and file I/O."""
    if argv is None:
        argv = sys.argv[1:]

    # Parser for command line options
    parser = argparse.ArgumentParser(description=
        "Converts numbers to Ayeri number words.")
    parser.add_argument('n', type=str, help='''An integer number between 0 and
        14,697,715,679,690,864,505,827,555,550,150,426,126,974,976''')
    
    args = parser.parse_args(argv)
    
    return '{}: {}'.format(baseconv(args.n), numberword(baseconv(args.n)))

if __name__ == '__main__':
    sys.exit(main())