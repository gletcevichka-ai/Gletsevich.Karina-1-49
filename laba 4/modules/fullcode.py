
from Bio import SeqIO


def gc_content(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    total = len(seq)
    if total == 0:
        return 0
    return (g + c) / total


f_name = r"C:\питон\лабы\sequence.finalver.gb"

records = []

for record in SeqIO.parse(f_name, "genbank"):
    seq = str(record.seq)
    gc = gc_content(seq)
    des = record.description
    records.append((record.id, des, gc))

gc_sort = sorted(records, key=lambda x: x[2])

output_file = r"C:\питон\лабы\gc_analysis_results.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for rec_id, desc, gc in gc_sort:
        line = f"{rec_id}: {desc}, GC = {gc:.4f}\n"
        f.write(line)
        print(line, end="")

from Bio import SeqIO

filename = r"C:\питон\лабы\sequence.finalver.gb"
output = r"C:\питон\лабы\translation_results.txt"

with open(output, "w", encoding="utf-8") as f:   # ← файл открыт

    for record in SeqIO.parse(filename, "genbank"):
        f.write(f"{record.id}: {record.description}\n")

        for feature in record.features:
            if feature.type == "CDS":

                start = int(feature.location.start)
                end = int(feature.location.end)
                strand = feature.location.strand

                f.write(f"    Coding sequence location = [{start}:{end}]({ '+' if strand == 1 else '-' })\n")
                f.write("    Translation =\n")

                cds_seq = record.seq[start:end]

                if strand == -1:
                    cds_seq = cds_seq.reverse_complement()

                protein = cds_seq.translate(to_stop=True)

                f.write(str(protein) + "\n\n")