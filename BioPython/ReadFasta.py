def read_fasta(file_path):
    import re
    dna_seq={}
    pattern = re.compile(r'>(.*?):') 
    with open(file_path,"r") as input_fasta:
        seq = ""
        header = pattern.search(input_fasta.readline().strip()).group(1)
        for line in input_fasta:
            line = line.strip()
            if line[0]!=">":
                seq=seq+line
            else:
                dna_seq[header]=seq
                # print(header)
                # print(seq)
                header=pattern.search(line).group(1)
                seq = ""
        # print(header)
        # print(seq)
        dna_seq[header]=seq
        return dna_seq
if __name__ == "__main__":  
    fasta_file = read_fasta('/home/wy/Documents/bioinformatics/data/seqdump.txt')
    for key in  fasta_file.keys():
        print(key)
        print(fasta_file[key])
