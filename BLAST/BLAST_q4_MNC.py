#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:07:05 2024

@author: marielle
"""

# Parse BLAST result files
def parse_blast_results(filename):
    results={}
    with open(filename, "r") as file:
        for line in file:
            query, subject, e_value = line.strip().split()
            if query not in results:
                results[query] = subject
    return results

# Find reciprocal best blast hits (RBBH) between two sets of results
def find_rbbh(results1, results2):
    rbbh={}
    for query, subject in results1.items():
        if subject in results2 and results2[subject] == query:
            rbbh[query]=subject
    return rbbh

# Main function to find 3-way RBBH
def main():
    results={key: parse_blast_results(files[key]) for key in files}

    # Compute 2-way RBBH pairs
    rbbh_pairs = {"Agla_Ldec": find_rbbh(results["Agla_Ldec"], results["Ldec_Agla"]),
        "Agla_Tcas": find_rbbh(results["Agla_Tcas"], results["Tcas_Agla"]),
        "Ldec_Tcas": find_rbbh(results["Ldec_Tcas"], results["Tcas_Ldec"])}
    two_way_counts={key: len(rbbh_pairs[key]) for key in rbbh_pairs}
    
    # Find 3-way RBBH groups
    three_way_orthologs={}
    for query_agla, subject_ldec in rbbh_pairs["Agla_Ldec"].items():
        # Check if query_agla also has an ortholog in Tcas
        if query_agla in rbbh_pairs["Agla_Tcas"]:
            subject_tcas = rbbh_pairs["Agla_Tcas"][query_agla]
            # Verify that subject_ldec matches with subject_tcas in the Ldec_Tcas results
            if subject_ldec in rbbh_pairs["Ldec_Tcas"] and rbbh_pairs["Ldec_Tcas"][subject_ldec] == subject_tcas:
                three_way_orthologs[query_agla] = (subject_ldec, subject_tcas)
    
    # Print results
    print("\nNumber of 2-way orthologous pairs for each comparison:")
    for key, count in two_way_counts.items():
        print(f"{key}: {count}")
    
    print("\nThe number of 3-way orthologous groups:")
    print(len(three_way_orthologs))

if __name__ == "__main__":
    main()
