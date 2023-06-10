#Khai báo các thư viện logging, Biopython
import logging
from Bio import SeqIO
# Cấu hình logging
logging.basicConfig(filename='consensus.log', level=logging.INFO)
# Đường dẫn đến tệp fasta
fasta_file = 'Seq02.fasta'
# Số lượng chuỗi cần xem xét
num_sequences = 10
# Đọc các chuỗi từ tệp fasta
sequences = []
for record in SeqIO.parse(fasta_file, 'fasta'):
    sequences.append(str(record.seq))
    if len(sequences) == num_sequences:
        break
def profile_matrix(dna_strings): 
    #Lấy chiều đài của các trình tự giả sử các trình tự có chiều dài bằng nhau
    n = len(dna_strings[0]) 
    #Khởi tạo một biến profile_matrix là một dictionary với 4 key là 'A', 'C', 'G', 'T' và giá trị ban đầu là một danh sách gồm n phần tử 0.
    profile_matrix = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    #Duyệt  từng trình tự trong danh sách dna_strings
    for dna in dna_strings:
        #Duyệt từng vị trí i và nucleotide trong dna
        for i, nucleotide in enumerate(dna):
            #Tăng giá trị của phần tử tương ứng với nucleotide tại vị trí i trong profile_matrix lên 1.
            profile_matrix[nucleotide][i] += 1
    return profile_matrix
# Hàm tạo consensus cho các trình tự
def consensus_string(profile_matrix):
    consensus_string = ""
    # Lấy độ dài của các cột
    n = len(profile_matrix['A'])
    # Duyệt từng cột
    for i in range(n):
        max_count = 0
        max_nucleotides = ''
        count_max = 0
        # Duyệt qua từng cặp key-value trong profile matrix
        for nucleotide, counts in profile_matrix.items():
            # Nếu số Nu hiện tại lớn hơn max_count thì cập nhật max_count và max_nucleotide
            if counts[i] > max_count:
                max_count = counts[i]
                max_nucleotides = nucleotide
                count_max = 1
            # Ngược lại, nếu số Nu hiện tại bằng max_count, tăng count_max lên 1
            elif counts[i] == max_count:
                count_max += 1
        if count_max >= 2:
            consensus_string += "N"
        else:
            consensus_string += max_nucleotides
    return consensus_string
profile = profile_matrix(sequences)
print(consensus_string(profile))
