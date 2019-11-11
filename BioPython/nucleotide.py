# EFetch: Downloading full records from Entrez
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc117
from Bio import Entrez
Entrez.email="1749748955@qq.com"
# The arguments rettype="fasta" and retmode="text" let us download this record in fasta format
handle = Entrez.efetch(db="nucleotide", id="JZ562261", rettype="fasta", retmode="text")
record = handle.read()
# print(record)
open("data/JZ562261.fasta","w").write(record)

