k = 6
reads =('GCTCAACATTGTGATCTTCT','CTTCTTGTTTTTAAAATGCTATA','GCTCAACATTGTGATCTTCTTGTTTTTAAAATGCTAT','TTTTAAAATGCTATAAAAACTGTTTAGCTAGAGTAAGATAGA','AAAATGCTATAAAAACTGTTTAGC','TGTTTAGCTAGAGTAAGATAGAGGCAAGT','TAGCTAGAGTAAGATAGAGGCAAGT')
kmer_counts={}
for read in reads:
    for i in range(len(read) - k + 1):
        kmer = read[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
print(kmer_counts)
print(len("GCTCAACATTGTGATCTTCTTGTTTAGCTAGAGTAAGATAGAGGCAAGT"))
print(len('GCTCAACATTGTGATCTTCT'))