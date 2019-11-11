charM_genom = ""
with open("E:/VisualStudio/vscode/gene/chrM.fa","r") as input_file:
    for line in input_file:
        line = line.strip().upper()
        charM_genom = charM_genom+line
        # print()

print(len(charM_genom))
# 统计ATCG
print(charM_genom.count("A"))
print(charM_genom.count("T"))
print(charM_genom.count("C"))
print(charM_genom.count("G"))
print("The char A count in chrM is : {0}".format(charM_genom.count("A")))

 