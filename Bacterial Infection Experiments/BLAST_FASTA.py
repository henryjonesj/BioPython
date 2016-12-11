# coding: utf-8

from Bio.Blast import NCBIWWW

from Bio import pairwise2

import csv

c = csv.writer(open("Experiment1.csv", "wb"))

c.writerow(["Species","QueryCoverage","Identity"])

list1 = ['Acetobacter', 'Borrelia', 'Bortadella', 'Borrelia','Burkholderia', 'Campylobacter','Chlamydia', 'Enterobacter','Escherichia', 'Fusobacterium','Helicobacter', 'Hemophilus','Klebsiella', 'Legionella','Leptospiria', 'Neisseria', 'Nitrobacter', 'Proteus','Pseudomonas', 'Rickettsia','Salmonella', 'Serratia','Shigella', 'Thiobacter','Treponema', 'Vibrio','Yersinia'];

from Bio import SeqIO
seq1 = SeqIO.read("ermb.fasta", "fasta")

result_handle = NCBIWWW.qblast("blastn", "nr",seq1.seq,alignments=250,entrez_query='(txid2 [ORGN]) NOT (txid1239 [ORGN] OR environmental samples[organism] OR metagenomes[orgn] OR txid32644[orgn])',
megablast=True)

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

list2=[];

index=-1


for description in blast_record.descriptions:
     flag=False
     ermB='null';
     for species in list1:
	if species in description.title and 'hypothetical' not in description.title:
		ermB=species
		flag=True
		break
	
     index=index+1
     if flag==False:
	continue

     if ermB in list2:
	continue

     list2.append(ermB)

     hsp= blast_record.alignments[index].hsps[0]
     identity = float(hsp.identities/(len(hsp.match)*0.01))

     if (int(hsp.align_length)<int(blast_record.query_length)):
	q_cov=(int(hsp.align_length)/int(blast_record.query_length))*100
     else :
     	q_cov = (int(blast_record.query_length)/int(hsp.align_length))*100

     print  description.title
     print 'Query coverage:',q_cov
     print 'Identity:',identity
     if q_cov>80 and identity>80:
   	  c.writerow([ermB,q_cov,identity])




list2=[];
index=-1

c = csv.writer(open("Experiment2.csv", "wb"))
c.writerow(["Species","QueryCoverage","Identity"])

result_handle = NCBIWWW.qblast("blastn", "nr",seq1.seq,alignments=250,entrez_query='(txid2 [ORGN]) NOT (txid1239 [ORGN] OR environmental samples[organism] OR metagenomes[orgn] OR txid32644[orgn])')

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

for description in blast_record.descriptions:
     flag=False
     ermB='null';
     for species in list1:
	if species in description.title and 'hypothetical' not in description.title:
		ermB=species
		flag=True
		break
	
     index=index+1
     if flag==False:
	continue

     if ermB in list2:
	continue

     list2.append(ermB)

     hsp= blast_record.alignments[index].hsps[0]
     identity = float(hsp.identities/(len(hsp.match)*0.01))

     if (int(hsp.align_length)<int(blast_record.query_length)):
	q_cov=(int(hsp.align_length)/int(blast_record.query_length))*100
     else :
     	q_cov = (int(blast_record.query_length)/int(hsp.align_length))*100


     print  description.title
     print 'Query coverage:',q_cov
     print 'Identity:',identity
     if q_cov>80 and identity>80:
   	  c.writerow([ermB,q_cov,identity])
