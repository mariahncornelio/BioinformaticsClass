#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:37:40 2024

@author: marielle
"""

# Parse each file first
def load_best_hits(file):
    best_hits={} #This is a dictionary to store the best hits
    with open(file, "r") as f:
        for line in f:
            query, subject, e_value=line.strip().split() #These are the 3 columns in our BLAST result files
            if query not in best_hits:
                best_hits[query]=subject
    return best_hits

def find_reciprocal_best_hits(file1, file2):
    hits_1_to_2=load_best_hits(file1)
    hits_2_to_1=load_best_hits(file2)
    rbbh_count=0
    for query_1, subject_2 in hits_1_to_2.items():
        #Checks if it is reciprocal 
        if subject_2 in hits_2_to_1 and hits_2_to_1[subject_2] == query_1:
            rbbh_count+=1
            
    return rbbh_count

if __name__ == "__main__": # This is the main function
    file1="/Users/marielle/Desktop/bioinformatics/BLAST Homework/Ldec_query_v_Tcas_subject.txt"  
    file2="/Users/marielle/Desktop/bioinformatics/BLAST Homework/Tcas_query_v_Ldec_subject.txt"
    rbbh_count = find_reciprocal_best_hits(file1, file2)
    print(f"Number of reciprocal best BLAST hits (RBBH): {rbbh_count}")
    
# Do this for all 6 ways
## TCAS <-> AGLA: 10250
## AGLA <-> TCAS: 10250
## LDEC <-> AGLA: 9921
## AGLA <-> LDEC: 9921
## TCAS <-> LDEC: 9509
## LDEC <-> TCAS: 9509
