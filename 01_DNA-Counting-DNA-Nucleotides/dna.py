#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rosalind Problem: Counting DNA Nucleotides
Problem ID: DNA
Link: https://rosalind.info/problems/dna/

Solution by: SMB (Seyed Majid Barekati)
GitHub: https://github.com/HPCSpecialist/rosalind-playground
"""

def count_nucleotides(dna_string):
    a = dna_string.count('A')
    c = dna_string.count('C')
    g = dna_string.count('G')
    t = dna_string.count('T')
    return a, c, g, t

def main():
    dna = input("Enter DNA string: ").strip()
    a, c, g, t = count_nucleotides(dna)
    print(f"{a} {c} {g} {t}")

if __name__ == "__main__":
    main()