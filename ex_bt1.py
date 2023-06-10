#Khai báo thư viện argparse
import argparse
#Xây dựng hàm đếm kmer lặp lại hơn hai lần cho trình tự sequence với k tối thiểu là k_min
def count_kmers(sequence,k_min):
    # Tạo dictionary rỗng để chứa trình tự kmer và số lần xuất hiện
    kmer_counts = {}
    # Chaỵ vòng lặp từ k_min đến k = len(sequence)-1 (k cuối cùng có 2 kmes)
    for k in range(k_min, len(sequence)):
        # Với mỗi giá trị k trên chạy vòng lặp từ vị trí 0 đến vị trí len - k
        for i in range(len(sequence) - k + 1):
            #Lấy trình tự k-mer từ vị trí thứ i độ dài k
            kmer = sequence[i:i+k]
            # Chạy điều kiện nếu kmer có trong dictionary thì value cộng 1, còn lại là 1
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1
    # Kết quả chỉ lấy những kmer có số lần lặp lại lớn hơn hoặc bằng 2
    kmer_counts = {kmer: count for kmer, count in kmer_counts.items() if count >= 2}
    return kmer_counts
#Tạo parse
parser = argparse.ArgumentParser(description='Find repeated k-mers in a DNA sequence')
#Truyền các args vào parser
parser.add_argument('--filename',type =str, help='Path to the FASTA file containing the DNA sequenceSe')
parser.add_argument('--k', type=int, default=10, help='Length of k-mers (default: 10)')
# Giúp chương trình nhận được thông tin từ các args 
args = parser.parse_args()
#Xây dựng hàm đếm kmer lặp lại hơn hai lần cho trình tự sequence với k tối thiểu là args.k
with open(args.filename,'r') as file:
    #Bỏ dòng đầu tiên (header)
    file.readline() 
    #Đọc file và truyền vào biến sequence 
    sequence = file.read().replace('\n', '')
count = count_kmers(sequence,args.k)
# In kết quả
for kmer, count in count.items():
    print(f'{kmer}:{count}')

