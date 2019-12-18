charM_genom = ""
with open("/home/wy/Documents/bioinformatics/project/Phyllothelys_breve.fasta","r") as input_file:
    # 读取一行
    input_file.readline()
    for line in input_file:
        line = line.strip().upper()
        charM_genom = charM_genom+line
        # print()

total_count=len(charM_genom)
A_count=charM_genom.count("A")
T_count=charM_genom.count("T")
C_count=charM_genom.count("C")
G_count=charM_genom.count("G")
print("The total of gene is "+str(total_count))
# 统计ATCG
print("The number of A is "+str(A_count))
print("The number of T is "+str(T_count))
print("The number of C is "+str(C_count))
print("The number of G is "+str(G_count))

print("The overall base composition was {0}% A  、{1}% T 、{2}% C 、{3}% G "
        .format(A_count/total_count,T_count/total_count,C_count/total_count,
        G_count/total_count))
# print("The char A count in chrM is : {0}".format(charM_genom.count("A")))

 