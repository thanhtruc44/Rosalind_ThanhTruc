def assemble_genome(reads, k):
    # Tạo dict để lưu trữ tần số xuất hiện của các k-mer
    kmer_counts = {}

    # Đếm tần số xuất hiện của các k-mer từ reads
    for read in reads:
        sequence = str(read.seq)
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1

    # Xây dựng genome bằng cách ghép các k-mer
    genome = ''
    for i in range(len(reads) - k + 1):
        kmer = str(reads[i].seq)
        if i == 0:
            genome += kmer
        else:
            genome += kmer[-1]

    # Trả về genome đã lắp ráp
    return Seq(genome, generic_dna)

# Đọc dữ liệu đọc từ file FASTA
reads = list(SeqIO.parse('reads.fasta', 'fasta'))

# Thực hiện lắp ráp bộ gen với k=30
k = 30
assembled_genome = assemble_genome(reads, k)

# In genome đã lắp ráp
print(assembled_genome)
