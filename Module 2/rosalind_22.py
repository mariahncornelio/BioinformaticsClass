#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:38:31 2024

@author: marielle
"""

from Bio.Seq import Seq

dna_string="AGCACTATACGCTAGGCGCCATGATGGGTGAGGTGACAGGAAATTCTTGTGTATCGCAGGACCGACATAATGGTAAACGGGAGCAGTGTGGGCTGACCTTAATACCGGCTTAGTGTGATGATTGAGTTACGGCGTTGGACATCTGGTTAAGGGTTGATGACGGCAGAACCTCTACCTCTAAGACACGCCTGGTTTATTCCAGCTGGGTGCTACAACGATTAGGTAACATAGCATAGTGCGATGTCGTCGCTTGTACATATATGTCAACTATTCACAGGGGTGGTACCTGGTGCTTTGGAGGAACGACCGGTAACCATCGACAAAGTAATCTCACAACTGGGTTATGCAATCGGGGGATATTCAATATCATTCCGGGACTACGATGCAACCGCTCTCGCATCAGGTCGCTCGTCGACCACCACGTAAGCCACTTACGGCCGCAAGACGCTGCGCACCGGTATACAAGTCCACACAGGCCAAGTTTAACGAGTTAGCTCCGATCTCTACCCGTTAAATGATGGTTATGCTGCAAACATCGTGGACGGCAGACAATGTGGCAGACAAAGTGGCCCGCGGTGCTTTGAACGGAACCGATAGCCAACAGGGTGGAAAATCCTAGCGAAAAGGGGCCCGGACTGAGACTCCTTTTGTGAGTCTACATTAAACGTAGCCATCCCGTCTCTTCATACTGGGCGCGCAGAGTGGGATGTTCTGCGCCGCCAGTCTAAAGGTAGGTAGGCTTCGATACACGTTCTGCCTCAGGAAACTGAGGTGACGCGACGGGGGACCATCCGCGTAACATCGCCGGTCCAGAGCTTTCGCGTTCATACCTACTGGAAGCCCCCCGCCGCTAGTTGCGGAGGCACATATGAGCGGTACCCTGATCAGTTCTGGACGTTTAACTAGAATTTTTTCGCGGTACCTACTTGTTCCTGCCTGGTCAATTAATTTGCGGTACGAAGCACGAGATTCAGCGTCCGACCTAGTGGAACAATTGACCATGTTTGTCCAGTCGCTTGTTCCCTAACAAAGCCCTATGGCATACCCGCAACGCTTACGACCGGATCAAGACGAAACTGACAGCGATCCTGCACAAGAAAATGACATTCACATCCAACCAGTTAAGGTAGTTTGCCGGTTCGCCGACCAGAGTGATACACCTCTGGGCTGTGGGCACACGTCGACCAACTTTTATAAGTACATGAATATCCTTGGGTGGGAACACACGGATTTTACAATCGTTGGCGCTCTCGTACGTGATGCTAATCGATGAGGATCTAACATTGGCAGAAAACTAATGTCGATTTTCCATTAAATCTTCATAATCGGTCGGATTAATAGATGCCCTCACCGCCATTACTACTTGCTACAGCGTGAATGTATTTTGTTCCCTAAGGGTAATAGATAATTGGTATGCGTAGGCACAGACTGTGGATCGGGTCGCGAGATGCCGCTGCGTTACAGTAAGTTCTGTGGATAAACCATTAAACTTCTCTCGTTACATTATATACCGAATAGGTTTACCGTTGGTGCTTAATTTCAATACAGTATGTGTTCTCCAGATGTGCATGCCCTTCTAATTTCAAAAAATCACCAAGATGACCATGATGGACTTCACTAGAGTGTATTCCGCCTTTCTGCCTAGCATAAGGCCAAGCCCGTACTGAGACACGGGGGATCGTCGGGAGTATAGGTTCTTCCTCCCACACGGGAGAGGAAAGTGGAATTGACACCCCCATAACACCGCTAGAAGCGCGTCATCGCCGGGTAGCTTCCATACTGGGGGCGAACACAGTCCCAGATTTGCCCTGGGGGGATCCTCTTAATAAATATTTAGCGTCTGTGTAGAATCAAACACGGCACGTGGCCTTTTATGCATAGGCGGACTCTCCGATGCCGGGCACCGAGTTTACCCGAACGCCATGTCGGATACCCGTGAGGGTTGTGGGATATGCGGCCAACACACCGTTCATTGCGTGGAATCACGGCTTCCAGCGGGATTTCTACGATGCTCAGGTCAAAATAGTCCACACCTCGATTCAGTGGGCTTCCTCTGGCCCCAGAATCCTGTTGTTGTTGCTCGCGATGGGCGGCGATTTCCCTACCTGTAGAATCTTGTAAGAACCCCAGGGAACTACTGAGTCAGTTCGTATCGCATCTCCTAAAGAGGAAGGGTCGAATACATTACGGTCTCACCGCCAGATTCGTCGAACGTATACTGGACGACGTTTACCCTTGAGACTATGAGGTTTGTCAAGTAGTATACAATCAGCTGCGAGGAGCAATCCGTCGTCCTACAGATGTCTTCGCTACGTTCAGTAGAGCTTTACTACAGATCTGTCGCCATAAACTCATTGATAGGGCAGGAGCTTCACATCCTTTTGTTGAACGAGGAGGCAGCCGCCCCTCGTTGGGGACCTAATTCTTTCGACGCTCGGGTCAAGAGAAGCCGACCTGTATACAGTGCCCGTTGACATCACAGCCTACTCTTGCACTGGTCCCTTCTGGTCCAACTCTGCACCTTTTTGAGGCCCGAAGCGCTTCGAAGCCATGGAGAGTCGGTCGAACCCGTGGGAGAGCAACATTTACAAACATCCGGTGCCGATCGAATAGGGTAGGAATCTGCCACTAACCACCTACGAATACAGAGAGCTCTTAACAACCCCCGACAGTGCCGCAGGGACACTTTTCATCTTGATAACTACGGCTGGAGGGGGGACACGAGCATGGAGATCATAGGGAATTCAAAGATTGTTAACATTCCAAAACCAGCTAACTGACGCAAGATAATTGAGCGGTAGATCTGTCTATCGTATACTGCACGCTCACGTGCTAGAGCTATTTGGTGTAGTTGCCTGACGTCGTCGTCTATCTCATGGCCCTGACAGCAGTTTCATATCGAACGGTATCCAGCGTGCTTTTATCCCGCGGCCTCGGCGATCACTAGAAATACTTTTCGGTAATTTCTCCATACCTCACCTATAACACTCGTCCAGGGCTACGGACTGAGTCGACAAGATGACCGCAGATCAACCACGATCGAATAAGTATAGGGACCTGCATCTCTAAGCGGCCCCACTTCTTGTAGCCATTCAGAGAGGGTTGGGCGACTTTTTTCCCCACGCTCAGAGAGCCTCATCGATTCGCATCGATTAACCAGACTTCTGTGGTTATAAACGAGAGAAGGAGGGTCTCTTTAAGACCCCCGGCGGGGTTCTTTTTTCAGCCGCAAATGAGATAGCCTCTAAGACTCCGGTTGTGAACAGAAAGGCCTGTTCGAGCTTGTCGTGTAAACCAGCATGCAACAGGCACCGTTAAAGCTGTGCGGTGCCCGTAGTAGGCAATACTCGCACAGCTTCGGCCAAAATAGCTAATTATGACTGACAGCAGTCTTCGTGTAGGTCACGACATGGTGAGGCAACAAAATAGAAAGTGAATTTGCCGAGGCCATTTACATACGAGTGGCTGAACTACAGCGTTCATTTCGCGGCCTAGCGGATAATCGGGCAGCTCGGGCTTTGGAAGATTCTCTCTTTATGCCTTAGGTCGCCGACTGGCAGGAAGTGGGGGGGCTGAACTGTGTTGCCTCGGCATTTTCTACGAAGAGTTCGCTACCCGCGGACTTAGGGACATGAACAGGATAGCTAAATACTCCCGGAGGGGATTCGCTCACACGGTAAATTCCCTCACGTTTCCAGTCAGGGGATCACCACTTACACTCTGCGTATATGGAGCGTACACCGGAAACTAGCCAAAAAGCGTCCTGAGGTAAAAACACCCGGCGACCAAGCCGTATGCAAAGCTCGACGCGTCCTTAGTATCGTAGAATTACCCTGAGAAACAAACCAGAGTTAAGACTCGCGTCAATCACTCTGAAGTTTGAGTAACAGGAGCACTCGGAAACACTGCGAGGGAGATATTCAGCTAATTGCGGTGATCTGACGACTATGGGGAGCTCTCATATGCCGGCCAAGAACTTAATATCGGCCTAGATCGCCAGGTTGTAGTAGGAAGACAACCCCACAAGCGAAGGGGTCAAAGCGGACCAAAGTGCAGAGAAGCACATGGTATGTGTGACAGGTGAATAAGTCAGGCTGAGTACCCTAGGCTGTAGCTCGACGACCCTCCGCTTCATTGACTACTCGTTCAGAGTGTTTGCGCTTCATCGGGGGAATGAGATGACGGGTGAAAGGGTACTTGGTGTTGCGAAGTTGAACTGGCCCATATGGTCCCTTTCCCGACTCTTATACGATGAGGCATCGCGACGCATTCAGATCGCTACGTGCGGCGTATGCCGAACAGAATTCTTGCTTTAGGGGTCGCTGCCTCCGAACCGGAACTTAGGAGCTTCTAATAGCTCCGGAGATAATTGAGGAAAATGTTATGTCATCCCTAATCATGAGTTCATCACGTGCGCTAATGAAGCTCGCTACATCGTGTTGACCGTTGCACATTGCTAGAGCTGTTTTTTGTCACTTGGATGTTCTGTAGCACGCTCGAGAAAACAGGATCATGCATAAGGTACTATCCAGGTAATACAATACCTCGTTCGAAGATGTATTTCTGTCCTTCCTGCAATGATTCCGTGAGCTGTTGGCATAGCTCTGGGCTGGGGACCCAACACCTGATTACGGGAAACCGACCCAACCCTTGCGCCAAAATACCACTTTCAGTACCCTTGCCAATAGCTGGTGTCCGGTCACTTACATTGTGCGATGGTGGTCCGAGGAGATCTTCCATCTGGGCACTGCGTATGAGATTGGGGGCTCATTCAATTTGCGTCAACATGAGCCTTGGACTCATAGTTATGGTTGAGGGCTCATCAACGCCAGGTCAGCTACGCTACTTTCAAGCGGTTAGGAGCGTGTAGCAACTACAAAGAACTGCCCTTTGCATAATATGGTGTGGTTGTTATGAAGTACGATTAACTCAATTATTCTCGGGTGATATGGATCGCCGCACCCGCCATCTGAGAATCCGAGTGGTATACTCCCTTTCGAGGCCCTAAGATGCGCCTGTAACGACCGGGAGATGTTCGTCACATCTACTTTTCAAGAGTCACCTCAGCGCGTCTGACCAAGAGTATCGAACCAAATCGCAGATCCTTGGCCATAAACCTGACCGGTACATGGTCCTATACAGTGGAGAGGTAGGGTGTACGGTCGTTCAGGACGAAGCGGATAGTTCATGGAGCCACACGTACAACCTGACCGCATGGTCCTAACAACTTTCCCGAATAGAGACCAGGACACGGCTAGACATCATTACCTATTGCCTCACTCTGTGCGACCATAGGGGACTAGAAATTTGCCGTTCCACAATTTGAAGTACGGTAGGGCCTAGTTGGGTGGCTCAGCGTCTGCCCAGCGCGAATGCCATATTATAGCCTGTCAATCCATGGTCAACGCTTATGTCCATTTGATAGTGACCACTGATTTGTCACTGGCATATATTTGGTGATCCCGCCGACGCTTTCACCAAAGGAGCTATAGGCTACACCAGGAATCACGATAGTCGGGCGTGCTGAAGCATGCTGCCAGGGCTGCCTGGAGAATTTGTTATGAACATCGCCACTGTTGGTCCTGTTATCTCTGCGGATCAGATTGCAGGTAGAGGGTCGTCTAGGCGTCTTTGTAGTGACCACAGTACCCTTTCAACTGGATTTAAATAGATAGAGTGTACAGAGGTTTTCGATCCGACCGAGCACCCCTTCATGGGCTAACACCGGCTCGAGTGCTCGGTTGGTCAAATCGATCTCTTTGGTCTTACTGGAACAGTTCTGACGGTTCTTGGCCTCTTGGCCCGAGCATAGGTATTATTGTCCCTCGGAGCCACACTCTGGAGGCCGATCGTTGAAGTTAGGAAGAAAACAGTGGCGCCCCTTCCAGTGGGTCTCGTCGTTAAAGTTACTCTGAATATCCCTAGTCTACTGACTCACGTTGAAGCGCAGTTCTTAACTGTTTCCGTCTCCTTTGACATACGCTAGTGCCACCATTTGGCCTTCGCTACCGAGTTGTCCTGCGGTTTCGCTCAAAAATCGGCTATGGAATCGATCATAAGGGGCGATTCTTCGCCTACCGATGTCACCTAGGTCTCATACCTCGCCCTTGTGTCATAGAGCTTTGCGCGAAAAGACGTGGAGGTACTGAGTCGTATAATCAGATTGTAGTCAAGCATTATAAGTGAGTAAGCGATACCGATAGGGGAGCGCAGGGGATCGGCGGAAGTCACTACTGATATCGAGAACAGCGCGCGAGTGTCGTGCATCGCACTTGGAAAGGGGTAAGAAGTCTCGAGAAGCTAACTCGAACAACACAGAGCATGCTTAGCGGAACTAGAGCGAGGGCCTGCGGCTCTAAAGCGGGATCTGAAGGATTGCTACGTCTACGCATATGTCTCACAGAATACTGATCGCATCAGTAACCATTCCTGACTTTCTATGAAGACACTTACGTGCTAAGTGCATTAAGAATAACTGAACGCTTCACAGGTTTGAACCCCTTATGACGCACGCGGGTATGTAGAGTGTTTCTCCTTTTGTGGACGTAATATACATGAACGGTGTCTCGAGGAGACATTTGCCGCGAGGACCCTGTCTATTAGGTAATGTTAGGCGGTGCCTTATTATGCATATCCGTCCTTTTATCGTACAGGCTAGGCTTACTAGAGACGGTTGGCGCCGCATGCTCAGCCTCGTACATCGACCTTGTTGGCTGTTGGCGTGTCGTTCAAGTCGGCTTGCCGTCGCATGGTCTGGTCATATCACTTAAACGGGGCGGCGGGAGATTCGTACTGCTGCGCTGAGTACCTCTTTACCTCCTACATTTAGGTCTAGCGCGATCTACTTAGGGTAGCAATGGGTCTCGGCGGAGATCGTGGCACACCGGCTTTCACTCTGGAGACTCCTTCAAACAACCGTTTGATTCCGGGCCTAAGTTCAACGCTTCCCAACGAAGCTAACCATCTGCACCCTTTCTGCGCCCTCAGCTTTGCTTGTAAAGCCCGGTGCATTTGAGCTGCTGGTAAACGGCTGTGCACCTACGCAGCCATAATGACATTACGCATCCGGCTAGCTTCTGGTCGAATCCAAAGGGATCAGAGTGACTGTCCACTACGCGACTTAGCAAGAGCACGTGAAAGGAAGACCTTGGCTGGGGTCGCGCTGAACTACAGGGTTTTCGTCAATCTTGGAGAGAGTAGCGTGTATCAGCCACAATTAAACGCTGCTAAGTAAAATCTGAACTAAAGTCTACCCACTAAATAAGGTCCCACCGACGGATAGTACAACCAGGTCAAATTTGGCCGTAATGAGTTTAGTGATGAAATGCCTTGTTTTAGTCCTTAAACGCCGTCAGCCGCCAACAATGCCGCACGGCCGTGCATCATACTGAGCTAGATGTGCGAAGTACAAATGGTCCTTCCACAGATGGCCAACTTCATCCCATCCAAGTCACTAAACTGAGGGGGACCTAACCGAAGGACGCTCCATTAATGTGTAAACTCGATTGTTGACCAGGCGGGGAGAATGGTTTATTGGGTTATCCTCAATCGATCTAACAAAAATCAGCTGGTCTGCAAATCATGACAATACGCCCTGGCTAGAAGAAGGTCAAGGTTGTCACTCGTCGCGCAAAGTTCTCTACGAACAATTGGTGATTGTTGTGGGTATTCAGGTCCTCCCGTAAGTACCAGCGTAAAAGAGTCGCTACGCACATTGCGTGTTAGTCCGATGCTAACAATAGCAGCAGTGCTCACCCGTATGGAGCACGCCTAAGCCGCCTGAACCAGTCGAGCTCGTGTAACTGTCCCCTGCGCCCGCTTCATGGCCCGTCTTTAGACGTCCTCATTGAGCGGCTAGTCAGTCTCTATCCTGGTTATGAGGGCATGACAGATCTCGCGAGACATTTGCACGCACCATGCCGACACAAACGAGAGCGTCTTGTGAGCTGCGCCCTAGTTAGACAGGAAATGTCTACAGCAGTATGGGCACGCCCTGGTCATAGTAGAGTGAGCTCGAGGGCCGTCGTAGGTACATATCGGTTAGATGAAGAGAGCATTGTACAGCCGACAGGTTGAGGTGTGTATCGAGGTAGGACTTGAGAATTGTATTTCCGAACGTGAAACGTACGTATTCGAAAATCGAAGGCGCGGCTCCATGAAGCTATCAAATGGGTAGAAAGTTCACTCAGTCCTTAAGTGTTTACCAATTACAGCACTATGCTACCAACCTCTGGGCAGTTTATGTCATGAAAGTCCGTCGCGCGCTCATACATAGGCGTTTACTAGGTGGGCTCAGCTATGGGGATCTCAGAAGCATAGGCAATGTTGCGGGCACCACTGACACAAGTCGGCACCGGGCTGCCCTTGTCAGCGCCTCGACCGTGCTGGCTATCCTCATACCTAGCAGCTTCGACATCTCTTCTATGTAGGCGTCAAAAGAGGGAAAGTAAACTGCCGGGAAAACTTTTAACACTTCACCGAAGGTATGCAGGGACCTGTCTGGCACCGGAGGGCCTTACCCCTCATTCTGACGGCGACAAATGCCATTAAAGACTGTCTGTATCAATTAAGTCATCACGCACGACTTCCCAAAAGCCGGCCCTAGGTTTGGAGGCGGGTTAGACACATCACCAAATTCGAGTCTGCAGCATACCTAAAATCCCGTATTGTTGACCAACCGGTCCACTTTCAAATACGACTTAACTCCCACGAGGCTCCCCGTTATTATTTGACATTCCAACATCCCCAAGATCGGTTTATATAAATTTCGTTACCGTGTCGGTTTTCGCCACAAGCTTGGAACCATCATGGAAGGAAGTTATTAAGAAGATAGGGGGCTAACATGGTATCCGCGTCATTTAGAGCCACATACCATACCGGACCACTATGTCAAGGCCATCATCTACGGAAGGTTCACCAGCTCAAGCGGCTTATGCGTGCATAGGATGGTCCCTAGAATTTGTCCTCAGTAGTTAAGTTCCCTTGGTATGCACGGACCAATGTAATGAGCTCCCTGACATTGCAAAATAAGGCATGACTGCCACATAGCACATGACGCACCCGACTCAACGCACTCATTCGGATTCTCAGCGCAGGTGAGCGTAGCGGGTAGATATGTTAGATGCGTAGATACTGGTGTAGCCAGGGCATTTCATTTTTGAGCAACATGATTGGCTAGAGGTTTTACCATCGGGTCCTATCTTACCTGCCACGTGATACAGACAGGTTTGGGTTGGCCTGGGGTCTGGATGGCCCGCTTATGGCGCGCAGGAGTCAACAAATCAACGGGGTTAGATACACCGATGTATAAAGAAGAGCAATAGTCGAATCCCAGGGGAATAAAAATCGAGCTACGAAGGTCTTTCTGAAACTATACACGGTAGGTATGTAAAACTCTGCGGAACATATATTAACATCTGCACTATCCCCCGTGATATATCTCGCGTGGAACACTCTGGCAAAGTCCCAGCAAAACATCTTCTTGGCTTCAATGCAGAAGTTGAACCTGCGCTTATACCATTTTAAAAAACTATCGTGTCTCGAGGTTTAGGTAAGAGATATATTGAGTAGCTCTCGAATCGTGGTTCGTTTACAGGCCTACTTATCTAAGGGAGTCGCCTTGGGCAAAACGCCCATGCCTTAAGCCTACCCATCACGCGTTAAATTTTTAAGTGCTCAACTTTTCTTGCCCAAGCCCTAGGCTCAGCGAACATGGATGAAGCAACGGCCGGGTGTGTTCCAATGCCGTCCGGTTGGACTAGCTGCGGCATCCGTAGCACGCTTTGGAATGGGCCTGGGCAACCATAGCAAGAG"
seq=Seq(dna_string)
reversed_complement= seq.reverse_complement()
print(reversed_complement)
