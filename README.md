# Hybrid_Encoding

- DBR -> Dynamic Bit Reduction

This project is a Hybrid approach of **lossless Data Compression** using **Dynamic Bit Redutcion** and **Huffman Encoding**. The Workflow of the project is as follows:

1. The input text file ha the orginal input given by the user, The DBR is performed and output stored in dbr_huffman text file.
2. Huffman encoding is performed on dbr_huffman file and the compressed file is saved in dbr_huffman.bin binary file.
3. In Decompression, we first decode the text using Huffman decoding algo and this is stored in dbr_huffman_decompressed text file
4. DBR decompression algo is performed to get final desired output. 

***For more info regarding Huffman Coding*** [check herre](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
