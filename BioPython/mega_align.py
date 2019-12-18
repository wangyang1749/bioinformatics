'''
使用mega进行序列比对
参考:https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface
    https://www.megasoftware.net/web_help_10/index.htm#t=MEGA-CC_Overview.htm
'''
import os

def alignFasta(input_seq,output_seq):
       # 如果不存在就创建文件夹
    if not os.path.exists(input_seq):
         os.makedirs(input_seq) 
    if not os.path.exists(output_seq):
         os.makedirs(output_seq) 
    os.system("megacc -a temp/mao/clustal_align_nucleotide.mao -d {0}  -f Fasta -o {1}".format(input_seq,output_seq))

def generate_align():
     for file_name in os.listdir("temp/result"):
         print("比对："+file_name+"...........")
         alignFasta("temp/result/{0}".format(file_name),"temp/align_output/")  
         

if __name__ == "__main__":
      generate_align()
