from Bio import SeqIO
record_ = SeqIO.parse('data/seqdump (1).txt', "fasta")
for seq_record in record_:
    print(">lcl|ORF ({})".format(seq_record.name))
    table = 1 # NCBI codon table 11 
    min_pro_len = 75 #最小的蛋白质长度
    # 遍历DNA的正链和负链
    for strand, nuc in [(+1, seq_record.seq), (-1, seq_record.seq.reverse_complement())]:
        # 遍历可能的6条序列
        for frame in range(3):
            length = 3 * ((len(seq_record)-frame) // 3) #Multiple of three
            # 分别将6条链翻译为蛋白质
            for pro in nuc[frame:frame+length].translate(table).split("*"):
                if len(pro) >= 75:
                    print(pro,"\n")
                    break
                # break
                    # print("%s...%s - length %i, strand %i, frame %i" \
                    #     % (pro[:30], pro[-3:], len(pro), strand, frame))
                    # print(pro,"\n")