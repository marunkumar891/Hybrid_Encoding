
from collections import OrderedDict
from huffman import HuffmanCoding
import sys
import os

"""---------------------------------Dynamic Bit reduction Compression------------------------------------------------"""


# function to convert decimal to binary
def DecimalToBinary(binary,num):
    if num > 1:
        binary=DecimalToBinary(binary,num // 2)
    binary.append(str(num % 2))
    return binary

#function to convert binary to decimal
def BinaryToDecimal(b_num):
    value = 0
    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value

# Assign numeric code to the unique character
def AssignNumericCode(characters,bit_len):
    char_dict={}
    for i in range(len(characters)):
        binary=[]
        binary=DecimalToBinary(binary,i)
        binary = "".join(binary)
        while(len(binary)<bit_len):
            binary = '0'+ binary
        char_dict[characters[i]] = binary
    return char_dict



fopen1 = open("input.txt", "r")
data = fopen1.read()


unique_character = list(OrderedDict.fromkeys(data).keys())
#print(unique_character)

bit_len=len(unique_character).bit_length()
#print(bit_len)

numeric_code=AssignNumericCode(unique_character, bit_len)
#print(numeric_code)

#convert text file to binary file
bin_output=""
for i in data:
    bin_output = bin_output + numeric_code[i]

#padding
add_zero=0
while((len(bin_output)%8)!=0):
    bin_output='0'+bin_output
    add_zero += 1


#converting 8-bit binary to characters
bin_string = bin_output
ascii_output=[]
start_bit=0
end_bit=8

while(end_bit<=len(bin_string)):
    b_num=list(bin_string[start_bit:end_bit])
    ascii_output.append(BinaryToDecimal(b_num))
    start_bit=end_bit
    end_bit=end_bit+8


output=""
for i in ascii_output:
    output=output+"".join(chr(i))

#writing in a file that is read by huffmann
huff_in = open("dbr_huffmann.txt","w",encoding='utf-8')
huff_in.write(output)
print("Hybrid huffman encoding done..!")
huff_in.close()


"""--------------------------------------------Huffman compression and Decompression----------------------------------------"""

path = "dbr_huffmann.txt"

# Huffmann Compression
h = HuffmanCoding(path)
output_path = h.compress()
print("Compressed file path: " + output_path)

#Huffmann decompression
decom_path = h.decompress(output_path)




"""--------------------------------------------Dynamic bit reduction Decompression------------------------------------------------"""

#opening the file decompressed by Huffmann
bin_output = ""
fopen2 = open("dbr_huffmann_decompressed.txt", "r",encoding="utf-8")
data = fopen2.read()
data = data.rstrip()
fopen2.close()

#convert characters to ascii values
ascii_values=[]
for i in data:
    ascii_values.append(ord(i))
for item in ascii_values:
    binary=[]
    binary="".join(DecimalToBinary(binary, item))
    while (len(binary)<8):
        binary='0'+binary
    bin_output=bin_output+binary

bin_output=bin_output[add_zero:]

key_list = list(numeric_code.keys())
val_list = list(numeric_code.values())

#convert binary to characters based on numeric codes
data2=""
start_bit=0
end_bit=bit_len
while(end_bit<=len(bin_output)):
    b_num=bin_output[start_bit:end_bit]
    data2 = data2 + key_list[val_list.index(b_num)]
    start_bit=end_bit
    end_bit=end_bit+bit_len

#writing the final decompressed file
decomp_output = open("finalout.txt", "w",encoding="utf-8")
decomp_output.write(data2)
print("Decompressed file path: finalout.txt")
decomp_output.close()

"""
Performance Parameters:
    1 -> Compression Ratio
        *** This is the ratio of size of the compressed file to the size of the source file. 
        
        CR = (C2/C1) * 100

    2 -> Saving Percentage
        *** Saving Percentage calculates the Compression of the source file as a  percentage.

        SP = (C1 - (C2/C1)) * 100

    C1 -> Size before Hybrid compression
    C2 -> size after Hybrid compression

"""

C1 =  os.stat("input.txt").st_size
C2 = os.stat("dbr_huffmann.bin").st_size

print("Size in bytes before compression:",C1,"bytes")
print("Size in bytes after hybrid compression:",C2,"bytes")

CR = (C2/C1) * 100
print("Compression Ratio : ",CR,"%")

SP = ((C1 - C2) / C1) * 100
print("Saving Percantage : ",SP,"%")


# Comparission between Huffman technique and Hybrid Huffman technique:

comparison1 = os.stat("input.bin").st_size
print("compressed size of binary file using Huffman only : ", comparison1,"bytes")

difference1 = comparison1 - C2
print("difference between compression techniques : ",difference1,"bytes")

"""

"""
# Comparision between Dynamic bit reduction and Hybrid Huffmn technique:

comparison2 = os.stat("dbr_huffmann.txt").st_size
print("compressed size of binary file using DBR only : ", comparison2,"bytes")

difference2 = comparison2 - C2
print("difference between compression techniques : ",difference2,"bytes")

