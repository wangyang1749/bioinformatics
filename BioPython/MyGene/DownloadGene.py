from Bio import Entrez
import os
Entrez.email = "1749748955@qq.com"

def downloadByNucleotide(ids,path,file_type,endName):
    if not os.path.exists(path):
         os.makedirs(path) 

    print("共下载序列",len(ids),"条")
    for id in ids:
        print("准备下载",id,"....")
        hd_efetch_fa = Entrez.efetch(db='nucleotide', id=id, rettype=file_type)
        read_efetch_fa = hd_efetch_fa.read()
        with open("{0}/{1}.{2}".format(path,id,endName),"w") as file:
            file.write(read_efetch_fa)
        print(id,"下载完成....")
        
# download coding sequencess
def downloadByNucleotideAndCodingSequences(ids,path):
    downloadByNucleotide(ids,path,"fasta_cds_na","fasta")

# download coding sequencess
def downloadByNucleotideAndGenbank(ids,path):
    downloadByNucleotide(ids,path,"gb","gb")

if __name__ == "__main__":
    # ids=["NC_037234.1","NC_024028.1"]
    ids=["NC_037234.1","NC_029326.1","NC_024028.1","NC_030265.1","KY689117.1","KY689119.1","NC_034282.1","NC_037207.1","NC_037235.1","NC_030266.1","KY689125.1","NC_037205.1"]
    # downloadByNucleotideAndCodingSequences(ids,"/home/wy/Documents/bioinformatics/temp")
    downloadByNucleotideAndGenbank(ids,"temp/source")