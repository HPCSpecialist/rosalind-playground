#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rosalind Problem: Counting DNA Nucleotides
Problem ID: RNA
Link: https://rosalind.info/problems/dna/

Solution by: SMB (Seyed Majid Barekati)
GitHub: https://github.com/HPCSpecialist/rosalind-playground
"""

def make_rna_string(dna_string):
    rna_string = dna_string.replace('T', 'U')
    return rna_string

def main():
    dna = input("Enter DNA string: ").strip()
    rna = make_rna_string(dna)
    print(rna)

if __name__ == "__main__":
    main()
