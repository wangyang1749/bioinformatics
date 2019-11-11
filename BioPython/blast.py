from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nucleotide", "JZ562264")
print(result_handle.read())