# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc36

from Bio import SeqIO
record = SeqIO.read("test_data/01.gb","genbank")
print(record.id)
print(record.name)
print(record.description)
# print(record.seq)
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc37
print(len(record.features))
# print(record.features)
for ele in record.features:
    if ele.type == "CDS":
        print(ele.qualifiers.get("gene"))
        for ele1 in ele.location.parts:
            print(ele1.start,ele1.end)

