#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rosalind Problem: Complementing a Strand of DNA
Problem ID: REVC
Link: https://rosalind.info/problems/revc/

Solution by: SMB (Seyed Majid Barekati)
GitHub: https://github.com/HPCSpecialist/rosalind-playground
"""

def reverse_complement(dna: str) -> str:
    """Return the reverse complement of a DNA string."""
    trans = str.maketrans('ATCG', 'TAGC')
    return dna.translate(trans)[::-1]


def main():
    """Read input and print the reverse complement."""
    dna = input().strip()
    print(reverse_complement(dna))


if __name__ == "__main__":
    main()
