#Khai bao thu vien argparse
import argparse
#Xay dung ham dem so kmer cho trinh tu
def count_kmers(sequence,k_min):
    # Tạo dictionary rỗng chứa trình tự kmer và số lần xuất hiện
    kmer_counts = {}
    for k in range(k_min, len(sequence)):
        for i in range(len(sequence) - k + 1):
            #Lấy trình tự k-mer từ vị trí thứ i 
            kmer = sequence[i:i+k]
        # Chạy điều kiện nếu kmer có trong dic thì cộng 1, không có là 1
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1
    # Kết quả chỉ lấy những kmer có số lần lặp lại lớn hơn hoặc bằng 2
    kmer_counts = {kmer: count for kmer, count in kmer_counts.items() if count >= 2}
    return kmer_counts
if __name__ == '__main__':
    #Tạo một đối tượng ArgumentParser từ module argparse giúp xử lí các đối số dòng lệnh
    parser = argparse.ArgumentParser(description='Find repeated k-mers in a DNA sequence.')
    # Tạo một đối số dòng lệnh tên là filename kiểu str và thông tin mô tả
    parser.add_argument('--filename', type=argparse.FileType('r'), help='Path to the FASTA file containing the DNA sequence')
    # Tạo một đối số dòng lệnh tên là k_min, kiểu số nguyên, giá trị mặc định là 10 và thông tin mô tả 
    parser.add_argument('--k', type=int, default=10, help='Length of k-mers (default: 10)')
    #Phân tích và trích xuất các đối số dòng lệnh được cung cấp cho chương trình bằng cách sử dụng thư viện argparse
    args = parser.parse_args()
with open(args.filename, 'r') as file:
    #Bỏ dòng đầu tiên (header)
    file.readline()  
    sequence = file.read().replace('\n', '')
count = {}
for k in range(args.k, len(sequence)):
    # Lần lượt update các dic mới với giá trị k từ 10 đến len(seq) - 1 
    count.update(count_kmers(sequence,k))
# In kết quả
for kmer, count in count.items():
    print(f'{kmer}:{count}')