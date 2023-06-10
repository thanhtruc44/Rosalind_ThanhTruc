import logging
import sys
from Bio import SeqIO
logging.basicConfig(filename='consensus.log', level=logging.INFO)
fasta_file = 'Seq02.fasta'
num_sequences = 10
sequences = []
try:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequences.append(str(record.seq))
        if len(sequences) == num_sequences:
            break
except FileNotFoundError:
    logging.error(f"File '{fasta_file}' not found.")
    sys.exit()

def profile_matrix(dna_strings): 
    n = len(dna_strings[0])
    profile_matrix = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile_matrix[nucleotide][i] += 1
    return profile_matrix

def consensus_string(profile_matrix):
    consensus_string = ""
    n = len(profile_matrix['A'])
    for i in range(n):
        max_count = 0
        max_nucleotides = ''
        count_max = 0
        for nucleotide, counts in profile_matrix.items():
            if counts[i] > max_count:
                max_count = counts[i]
                max_nucleotides = nucleotide
                count_max = 1
            elif counts[i] == max_count:
                count_max += 1
        if count_max >= 2:
            consensus_string += "N"
        else:
            consensus_string += max_nucleotides
    return consensus_string

profile = profile_matrix(sequences)
consensus = consensus_string(profile)
print(consensus)
logging.info(f"Consensus sequence: {consensus}")
