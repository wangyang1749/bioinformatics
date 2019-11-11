output_file=open("E:/VisualStudio/vscode/gene/test.fasta","w")
# fastq与fasta转换
with open("E:/VisualStudio/vscode/gene/test.fastq","r") as input_fastq:
    for  index,line in enumerate(input_fastq):
        if index % 4 ==0:
            output_file.write(">"+line.strip()[1:]+"\n") 
        elif index%4==1:
            for i in range(0,len(line.strip()),40):
                output_file.write(line.strip()[i:i+40]+"\n")
        else:
            continue