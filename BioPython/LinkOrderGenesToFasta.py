from Bio import SeqIO
import os
list_sort=["ND2","COX1","COX2","ATP8","ATP6","COX3","ND3","ND5","ND4","ND4L","ND6","CYTB","ND1"]


def linkGene(input_path,output_path):
    if not os.path.exists(input_path):
         os.makedirs(input_path) 
    if not os.path.exists(output_path):
         os.makedirs(output_path) 
    

    f = open("{0}/{1}.fasta".format(output_path,"new_seq"),"w")
    for file_name in os.listdir(input_path):

        records = SeqIO.read("{0}/{1}".format(input_path,file_name),"genbank")
        #从Genbank获取完整序列
        complete_seq = str(records.seq)
        print(records.description)
        gene_dict = {}
        for feature in  records.features:
            if feature.type == "CDS":
                # print(feature.qualifiers.get("gene"))
                gene_name = feature.qualifiers.get("gene")[0]
                # print(type(feature.location.parts))
                gene_seq=""
                for gene in  feature.location.parts:
                    # print(complete_seq[gene.start:gene.end])
                    gene_seq = gene_seq + complete_seq[gene.start:gene.end]
                gene_dict[gene_name]=gene_seq


        #按照顺序遍历基因
        end_seq=""
        print("定义了",len(list_sort),"个基因","序列有",len(gene_dict),"个基因")
        for gene in list_sort:	
            if gene in gene_dict:
                print("找到基因：",gene,"长度为：",len(gene_dict[gene]))
                # print(gene_dict[gene])
                end_seq=end_seq+gene_dict[gene]
            else:
                print("error----------","没有找到基因：",gene)

        f.write(">"+records.description+"\n"+end_seq+"\n")
        print("*******写入完成*******")

if __name__ == "__main__":
    linkGene("temp/result","temp/789")