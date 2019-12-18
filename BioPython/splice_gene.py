'''
拼接比对好的线粒体的基因
参考：
'''


import os
gene_dict={}
list_sort=["ND2","COX1","COX2","ATP8","ATP6","COX3","ND3","ND5","ND4","ND4L","ND6","CYTB","ND1"]
# list_sort=["ND2","COX1"]
for file_name in os.listdir("temp/align_output"):
    if file_name.endswith(".fasta"):
        gene_dict[file_name.split("-")[0]]=file_name
    
def spiceSeq():        
    dna_seq={}
    for gene in list_sort:
        if gene in gene_dict:
            print("向字典添加基因:"+gene+"............")
            with open("temp/align_output/{0}".format(gene_dict[gene]),"r") as input_file:
                seq = ""
                header = input_file.readline().strip()
                for line in input_file:
                    line = line.strip()
                    # print(line == "")
                    # print(line)
                    if line=="":
                        continue
                    elif line[0]!=">":
                        seq=seq+line
                    else:
                        if header in dna_seq:
                            dna_seq[header]+=seq
                            # print(header+"exist")
                        else:
                            dna_seq[header]=seq
                            # print(header+" not exist")
                        
                        # print(header)
                        # print(seq)
                        header = line
                        
                        seq = ""
                if header in dna_seq:
                    dna_seq[header]+=seq
                else:
                    dna_seq[header]=seq
    return dna_seq                
f = open("temp/align_result/align_result.fasta","w")
dna_seq= spiceSeq()
for key in dna_seq:
    # print(key)
    # print(dna_seq[key])
    f.write(key+"\n"+dna_seq[key]+"\n")
