# Bioinformatics - BIOL 5340 Fall 2024
The first half (Modules 1 and 2) of this class's homework was completed on a website called <a href="https://rosalind.info/problems/list-view/">ROSALIND</a>, a platform for learning bioinformatics and bioinformatics tools through problem-solving. Modules 1 and 2 of this repository contain my solutions to the Rosalind problems. Each problem task is listed below for reference. Solutions to ROSALIND problems are curated using Python on Spyder, with packages like BioPython utilized for tools such as Seq.

### Module 1
- <b>Rosalind 1:</b> Variables and Some Arithmetic
- <b>Rosalind 2:</b> Strings and Lists
- <b>Rosalind 3:</b> Conditions and Loops
- <b>Rosalind 4:</b> Working with Files
- <b>Rosalind 5:</b> Dictionaries
- <b>Rosalind 6:</b> Counting DNA Nucleotides
- <b>Rosalind 7:</b> Transcribing DNA to RNA
- <b>Rosalind 8:</b> Translating RNA into Protein
- <b>Rosalind 9:</b> Computing GC Content

### Module 2
- <b>Rosalind 10:</b> Compute the Number of Times a Pattern Appears in a Text
- <b>Rosalind 11:</b> Find the Most Frequent Words in a String
- <b>Rosalind 12:</b> Implement PatternToNumber
- <b>Rosalind 13:</b> Implement NumberToPattern
- <b>Rosalind 14:</b> Generate the Frequency Array of a String
- <b>Rosalind 15:</b> Find All Occurrences of a Pattern in a String
- <b>Rosalind 16:</b> Find Patterns Forming Clumps in a String
- <b>Rosalind 17:</b> Find a Position in a Genome Minimizing the Skew
- <b>Rosalind 18:</b> Compute the Hamming Distance Between Two Strings
- <b>Rosalind 19:</b> Generate the d-Neighborhood of a String
- <b>Rosalind 20:</b> Find All Approximate Occurrences of a Pattern in a String
- <b>Rosalind 21:</b> Find the Most Frequent Words with Mismatches in a String
- <b>Rosalind 22:</b> Find the Reverse Complement of a String
- <b>Rosalind 23:</b> Find Frequent Words with Mismatches and Reverse Complements

### Multiple Sequence Alignment (MSA)
Multiple sequence alignment (MSA) was performed on 18S ribosomal RNA sequences to identify conserved regions across different species. The analysis included locating G blocks, conserved motifs, and examining sequence variability. Additionally, the P450 gene dataset (P450.fasta) was analyzed to assess the evolutionary relationships and functional significance of P450 enzymes.

### BLAST
Protein sequences for Tribolium castaneum (Tcas), Anoplophora glabripennis (Agla), and Leptinotarsa decemlineata (Ldec) were retrieved from the NCBI databse. BLAST sequence analysis was performed on these sequences, focusing on key genes including maleless, mof, msl2, and msl3. The analysis aimed to investigate sequence similarities and functional relationships across the different species. The analysis was done using Python to compare one-way, two-way, and three-way relationships.

### Genomic Variant Analysis (GVA)
Genomic variant analysis (GVA) was conducted using both trimmed and untrimmed reads. Genomic Variant Analysis (GVA) is the process of examining genetic data to identify differences or "variants" in DNA sequences. The datasets included the reference sequence NC_012967.1.fasta, its corresponding GenBank file NC_012967.1.gbk, and paired-end reads SRR030257_1.fastq and SRR030257_2.fastq. Due to file size limitations, the data could not be uploaded.

### Earl Grey Final Project
In our final project, we were assigned the species Cassiopeia ornata. Using the Bridges 2 HPC, Earl Grey analysis was performed on the genes of interest. The project involved comparing high-level gene expression counts and repeat content, calculating the correlation coefficient (r), and analyzing transposable element (TE) content, as well as categorizing the TEs into their respective families and subfamilies. This analysis aimed to provide insights into gene expression patterns and the role of TEs in the genome.
