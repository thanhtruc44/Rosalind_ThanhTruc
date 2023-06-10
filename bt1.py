#Khai báo thư viện argparse
import argparse
#Xây dựng hàm đếm kmer lặp lại hơn hai lần cho trình tự sequence với k tối thiểu là k_min
def count_kmers(sequence,k_min):
    # Tạo dictionary rỗng để chứa trình tự kmer (key) và số lần xuất hiện (value)
    kmer_counts = {}
    # Duyệt phần tử từ k_min đến k = len(sequence)-1 (cuối cùng có 2 kmes)
    for k in range(k_min, len(sequence)):
        # Với mỗi giá trị k, duyệt phần tử từ vị trí 0 đến vị trí len - k
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
#Tạo một đối tượng ArgumentParser từ module argparse giúp xử lí các đối số dòng lệnh
parser = argparse.ArgumentParser(description='Find repeated k-mers in a DNA sequence.')
# Tạo một đối số tên là filename kiểu str và thông tin mô tả
parser.add_argument('filename', type=str, help='Path to the FASTA file containing the DNA sequence')
# Tạo một đối tên là k_min, kiểu số nguyên, giá trị mặc định là 10 và thông tin mô tả 
parser.add_argument('--k', type=int, default=10, help='Length of k-mers (default: 10)')
#Giúp chương trình nhận được thông tin từ các args 
args = parser.parse_args()
#Mở tệp được chỉ định là đối số filename để đọc nội dung, 'with open' đảm bảo tệp được đóng tự động sau khi hoàn thành công việc.
with open(args.filename, 'r') as file:
    #Bỏ dòng đầu tiên (header)
    file.readline()  
    sequence = file.read()
# Gọi hàm count_kmers với tham số sequence và args.k và lưu vào biến counts
counts = count_kmers(sequence,args.k)
# In kết quả
for kmer, count in counts.items():
    print(f'{kmer}:{count}')


