# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc35 

from Bio import SeqIO
record = SeqIO.read("test_data/01.fasta","fasta")
print(record.id)
print(record.name)
print(record.description)
print(record.seq)
