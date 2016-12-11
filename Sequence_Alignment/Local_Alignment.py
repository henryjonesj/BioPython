# coding: utf-8

import Bio


def computeParameters(alignments):
	
	a,b,c,d,e= alignments[0]

	alignedString= pairwise2.format_alignment(*alignments[0])
	count=0
	transitions=0
	transversion=0
	i=0

	for i in range(0, e):

		if a[i]==b[i]:
			count+=1

		if (a[i]=='A' and b[i]=='G') or (a[i]=='G' and b[i]=='A') or (a[i]=='C' and b[i]=='T') or (a[i]=='T' and b[i]=='C') :
			transitions+=1
 	
		else:
			if a[i]!='-' and b[i]!='-' and a[i]!=b[i]:
				transversion+=1
			
	
	print "Score is",c
	print 'Number of gaps is', alignedString.count('-')
	print 'Number of matches is', count
	print 'Number of transitions is', transitions
	print 'Number of transversions is', transversion


def alignGlobaly(seq1,seq2,matrix):

	
	gapOpenPenalty= [-6, -10]
	gapExtendPenalty= [-5, -4]

	i=j=0
	for i in range(0, 2):
		for j in range(0, 2):
			print gapOpenPenalty[i], gapExtendPenalty[j]
			alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, matrix, gapOpenPenalty[i], gapExtendPenalty[j],penalize_end_gaps=(False, False))
			computeParameters(alignments)



def doAlignment(matrix):

	print "\n Computing for Brisbane2007.txt and Brisbane2007_M2.txt……."

	alignGlobaly(seq1,seq2,matrix);



from Bio import pairwise2
from Bio import SeqIO
seq1 = SeqIO.read("Brisbane2007.txt", "fasta")
seq2 = SeqIO.read("Brisbane2007_M2.txt", "fasta")

M1= {('A', 'A'): 5,
 ('A', 'T'): -4,
 ('A', 'G'): -4,
 ('A', 'C'): -4,
 ('T', 'A'): -4,
 ('T', 'T'):  5,
 ('T', 'G'): -4,
 ('T', 'C'): -4,
 ('G', 'A'): -4,
 ('G', 'T'): -4,
 ('G', 'G'):  5,
 ('G', 'C'): -4,
 ('C', 'A'): -4,
 ('C', 'T'): -4,
 ('C', 'G'): -4,
 ('C', 'C'): 5}

M2= {('A', 'A'): 5,
 ('A', 'T'): -5,
 ('A', 'G'): -1,
 ('A', 'C'): -5,
 ('T', 'A'): -5,
 ('T', 'T'):  5,
 ('T', 'G'): -5,
 ('T', 'C'): -1,
 ('G', 'A'): -1,
 ('G', 'T'): -5,
 ('G', 'G'):  5,
 ('G', 'C'): -5,
 ('C', 'A'): -5,
 ('C', 'T'): -1,
 ('C', 'G'): -5,
 ('C', 'C'): 5}

print "\n Computing with Matrix M1……………."

doAlignment(M1)

print "\n Computing with Matrix M2……………."

doAlignment(M2)
