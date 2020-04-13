# -*- coding: utf-8 -*-
"""

@author: 300111671
qq2"""

import json

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

def main():
  print(charge('b000000000.json'))


if __name__== "__main__":
    main()