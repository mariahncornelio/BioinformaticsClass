#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:02:22 2024

@author: marielle
"""

nucleotide_sequence="GATAAGATGAATAGGAGAAGAGGAGTAGCTCTGTTACATGCCTACCTATCTTTGTGTAACTTGTTGAAGCTAGTCAGCGTCACCAGAACTCTGGTAACGTAACGACCACGGGCAGGCCCCACCACCTTCCGGAACTACGCACCCGCACATGGTGGTCAAGAGACAGAAACGCGACCAGCTCACGGTGTTCTGACGATTACTAAACAGTGAGTCCTGAAGCGTCGGGCCGCGAAGTCGTGGGAAGATCTGCAGCACCTGGAGAATACCCAAAGGGGTGGGAAGTGATCGCTTACTGGCACTACTATAGTACCCGTTTACGGTTGTGCGCAATTGCCCAACCTCTTTCGTACGGCGCAGGTTATATGTGTTCCATCTATCCGACGGACCCTCCCTAGATCCACGCCATCGGAGACCGGGTAATCGTTCTGGAACATAGTGGAAAATTAAAGTGGAAGAAATTCAGATCAAAGGGTGGACCCACGTGCCCTATGTCTGAATGCATGTCCAACTAGTGCTGTCAATTTTGACCACCCTGACCCGCTATCAACCAAGCAGCTGCCTATGAACCTTCTCAAAATTATAACATATCTAAGCGTTAGCTTCGCGATTGACACCAGTGCATAAATCGTCATAGGTGTAACTTCCCCTTGACCTGCGCGTCAGTGACCATGCGGCTTTTTGACCCAGATACTTAACGCACATTTTTTAGAAAGAAGCCCAAGTTCGATAAAGCAACGGACGAAGACTCTCCGTTAAGATACGCCATGAAAAAAGGGGCCGATGGCGTGAGAACATGAATGAGCTGGACTATAAATCGGATGATCCAGGGAAATAAGAGCCGCGCCGTGACTATCCATCTAAAGACGTCGTCGAAATGTGCGTACGCCAAGAGGCCTGATAGGAGGACAGCTCACTCATGGAGGCGAAGTCGGACTCGTGCTGCCGCAGGCCATTCCCTGTTTTCAATGGGCTGTTCTT"
A=nucleotide_sequence.count("A")
G=nucleotide_sequence.count("G")
C=nucleotide_sequence.count("C")
T=nucleotide_sequence.count("T")

print(A, C, G, T)