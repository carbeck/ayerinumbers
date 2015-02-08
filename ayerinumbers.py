#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' ayerinumbers.py -- Converts numbers to Ayeri number words '''

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

'''Morphemes for the powers 12^1 to 12^44'''
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
    44:'menlanang',     # FIXME
}

'''The number words for the numbers 0...B'''
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

'''Assign keys from nword to pword on the fly. We need this to generate
   morphemes for powers beyond 'tamang'.'''
pnword = {}
for i, x in zip(sorted(nword), [pword[i] for i in sorted(pword)]):
    pnword[i] = x
pnword['0'] = 'lanang'

def c(n):
    '''Convert number > 9 to a string ABCDE…'''
    if(n > 9):
        n = chr(n + 55);
    return n

def baseconv(n, b = 12):
    '''Convert an integer number n in base 10 to another'''
    s = ''
    while n > 0:
        r = n % b       # remainder
        n = n // b      # integer
        s = str(c(r)) + str(s)
    return s

'''List of numbers 01…0A'''
sd = ['0'+baseconv(i) for i in range(1,12)]

def numword_bigram(n, pn = 'nword'):
    '''Take a number bigram (str!) and return the corresponding number word.'''
    
    # Instantiate empty string as a container
    s = ''
    
    # Single digit
    if len(n) < 2:
        
        # Digit is 1...B and we're using regular number words
        if n[0] != '0' and pn == 'nword':
            s = '{}'.format(nword[n[0]])
            
        # Digit is 1...B and we're using power words
        elif n[0] != '0' and pn == 'pnword':
            s = '{}'.format(pnword[n[0]])
        
    # Two digits
    else:
        
        # Digits 10, 20, 30, ..., B0 and we're using regular number words
        if n[0] != '0' and n[1] == '0' and pn == 'nword':
            s = '{}{} '.format(nword[n[0]], pword[1])
        
        # Digits 10, 20, 30, ..., B0 and we're using power words
        elif n[0] != '0' and n[1] == '0' and pn == 'pnword':
            s = '{}{} '.format(nword[n[0]], pnword['0'])
        
        # Digits 11, 12, 13, ..., 21, 22, 23, ..., B1, B2, B3, ...
        elif n[0] != '0' and n[1] != '0':
            s = '{}{}-'.format(nword[n[0]], pword[1])
        
        # Digits 01, 02, ..., 0B
        elif n[0] == '0' and n[1] != '0':
            s = 'nay '
        
        # Last digit is not 0 and we're using regular number words
        if n[1] != '0' and pn == 'nword':
            s += '{}'.format(nword[n[1]])
        
        # Last digit is not 0 and we're using power words
        elif n[1] != '0' and pn == 'pnword':
            s += '{}'.format(pnword[n[1]])
    
    return s.strip()

def rsplit_str(s, i):
    '''Splits string after i digits from the back'''
    
    # Containers
    chars = ''
    spl = []
    
    # Calculate the modulo the last index results in for the length of the group
    # 12345, split into groups of max. 3 => last index: 4, 4 % 3 = 1
    m = (len(s) - 1) % i
    
    for n, char in enumerate(s):
        chars += char;
        if n % i == m:
            spl.append(chars);
            chars = ''
    
    return spl

def split_num(s):
    '''Split into list with the format [['00','00'],['00','00'], ...]'''
    
    # Splitting into groups of 4
    sp = rsplit_str(s, 4)

    # Splitting into subgroups of 2
    for i, n in enumerate(sp):
        sp[i] = rsplit_str(n, 2)
        
    return sp

def count_elements(l):
    '''Count the number of elements in the list on the 1st sublevel'''
    return sum(len(x) for x in l)

def get_power(i):
    '''Gets the word for the respective power from number of elements'''
    pow = 2 * i - 2

    # If power word exceeds the hard-coded ones, generate one on the fly
    if pow > max(pword):
        return numberword(baseconv((math.ceil(i/2)*2 - 1) // 2 + 1), 'pnword')
    
    # In case it's already readily defined
    if pow in pword:
        return pword[pow]
    
    # In case it's not already defined
    elif pow not in pword:
        
        # Iterate through all the power words until one bigger than the input 
        # is found, use the previous one then.
        flag = True
        p = 0
        while flag:
            for x in sorted([n for n in pword]):
                if x > pow:
                    flag = False
                else:
                    p = x
        return pword[p]

def numberword(n, pn = 'nword'):
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
    
    for i, myrgrp in enumerate(n):
        
        # The power word for the current group, avoid *menang menang
        if i < len(n) - 1 and n[i] != ['00', '00']:
            s.append(get_power((len(n) - i) * 2))
        
        # Some fixing: [['01', ...]] -> [['1', ...]]
        if len(n[i]) > 1 and n[i][0] in sd:
            n[i][0] = n[i][0][1]
        
        # Some fixing: [['00', '01'], [...]] -> [['00', '1'], ...]
        if i < len(n) - 1 and len(n[i]) > 1 and n[i][1] in sd:
            n[i][1] = n[i][1][1]
        
        # Get the word for power of the element in the group
        if len(n[i]) > 1 and n[i][0] != '00':
            s.append(get_power(len(n[i])))
        
        # For each group of hundreds, get the number word
        for j, hungrp in enumerate(n[i]):
            s.append(numword_bigram(n[i][j], pn))
        
    return ' '.join(filter(None, s))

def main(argv=None):
    """Main function providing command line option parser."""
    if argv is None:
        argv = sys.argv[1:]

    # Parser for command line options
    parser = argparse.ArgumentParser(description=
        "Converts numbers to Ayeri number words.")
    parser.add_argument('n', type=int, help='''an integer number 0 <= n < 12^44''')
    parser.add_argument('-s', '--show-conversion', action='store_const', 
        const=True, default=False, help='''show the conversion into base 12'''),
    args = parser.parse_args(argv)
    
    # Return string
    s = ''
    if args.show_conversion:
        s += '{}₁₂: '.format(baseconv(args.n))
    s += '{}'.format(numberword(baseconv(args.n)))
    
    return s

if __name__ == '__main__':
    sys.exit(main())
