# coding: utf-8

codondict= {   "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
		"CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
		"AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
		"GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
		"UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
		"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
		"ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
		"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
		"UAC": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
		"CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
		"AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",					"GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
		"UGC": "C", "UGC": "C", "UGA": "*", "UGG": "W",
		"CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
		"AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
		"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G" }

import sys

f=-1

try:
    f= open("dna.txt")
except IOError:
    print "File dna.txt not Found"
    sys.exit(0)
    
content = f.read().splitlines()


if len(content)!=2:
	sys.exit(0)

if len(content[0])!=len(content[1]):
	sys.exit(0)

amino=[]

for i in range(len(content)):
	content[i]=content[i].replace("T","U")
	import textwrap
	temp= textwrap.wrap(content[i],3)
	for j in range(len(temp)):
		value= codondict[temp[j]]
	 	amino.append(value)

aminoA= "".join(amino[:len(amino)/2])
aminoB= "".join(amino[len(amino)/2:])

f = open("output.txt","w")

for i in range(len(aminoA)):
	if aminoA[i]!=aminoB[i]:
		f.write("%d %s %s \n" % (i,aminoA[i],aminoB[i])) 

f.close()

		