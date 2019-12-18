# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc36

from Bio import SeqIO
record = SeqIO.read("/home/wy/Documents/bioinformatics/project/Phyllothelys_breve-线粒体基因组拼接结果-注释版(GB格式).gb","genbank")
print("recore id is "+record.id)
print("record name is "+record.name)
print("record description is "+record.description)
print(record.annotations["source"])
# print(record.seq)
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc37
print(len(record.features))
# print(record.features)
# print(record.features)
for ele in record.features:
    if ele.type == "tRNA":
        print(ele.qualifiers.get("gene"))
        # for ele1 in ele.location.parts:
        #     print(ele1.start,ele1.end)

