from Bio import AlignIO


gapcount=0

for alignment in AlignIO.parse("c.fasta", "fasta", seq_count=16):
    print("Alignment length %i" % alignment.get_alignment_length())
    for record in alignment:
        gapcount= gapcount + record.seq.count('-')


print("Gap count is %i" %gapcount)

print("")
