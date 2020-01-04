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
complete_seq = str(record.seq)
# for ele in record.features:
#     if ele.type == "CDS":
#         # print("> "+ele.qualifiers.get("gene")[0])
#         for gene in ele.location.parts:
#             # print(gene.start,gene.end)
#             # 查看前三个基因
#             # print(ele.qualifiers.get("gene")[0]+" : "+complete_seq[gene.start:gene.start+3])
#             print(ele.qualifiers.get("gene")[0]+" : "+complete_seq[gene.end-3:gene.end])


# for ele in record.features:
#     if ele.type == "rRNA":
#         # print("> "+ele.qualifiers.get("gene")[0])
#         for gene in ele.location.parts:
#             # print(gene.start,gene.end)
#             # 查看前三个基因
#             # print(ele.qualifiers.get("gene")[0]+" : "+complete_seq[gene.start:gene.start+3])
#             # print(len(complete_seq[gene.start:gene.end]))
#             rrna_seq = complete_seq[gene.start:gene.end].strip()
#             print((rrna_seq.count("A")+rrna_seq.count("T"))/len(rrna_seq))
#             print("total count:"+str(len(rrna_seq)))
#             # print()

for ele in record.features:
    if ele.type == "D-loop":
        # print("> "+ele.qualifiers.get("gene")[0])
        for gene in ele.location.parts:
            control_seq = complete_seq[gene.start:gene.end].strip()
            print((control_seq.count("A")+control_seq.count("T"))/len(control_seq))
            print("total count:"+str(len(control_seq)))
       