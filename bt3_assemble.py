import itertools
def overlap(seq1,seq2,min_length):
    start = 0
    while True:
        start = seq1.find(seq2[:min_length],start)
        if start == -1:
            return 0
        if seq2.startswith(seq1[start:]):
            retu rn len(seq1)-start
        start +=1
def scs(ss):
    shortest_superstring = None
    for set in itertools.permutations(ss):
        sup = set[0]
        for i in range(len(ss)-1):
             olen = overlap(set[i],set[i+1],min_length=2)
             sup += set[i+1][olen:]
        if shortest_superstring is None or len(sup) < len(shortest_superstring):
            shortest_superstring = sup
    return shortest_superstring
print(scs(["GCTCAACATTGTGATCTTCT","CTTCTTGTTTTTAAAATGCTATA","GCTCAACATTGTGATCTTCTTGTTTTTAAAATGCTAT","TTTTAAAATGCTATAAAAACTGTTTAGCTAGAGTAAGATAGA","AAAATGCTATAAAAACTGTTTAGC","TGTTTAGCTAGAGTAAGATAGAGGCAAGT","TAGCTAGAGTAAGATAGAGGCAAGT"]))
            
