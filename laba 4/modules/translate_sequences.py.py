# Глецевич Карина 1-49
# Лабораторная работа 4, вариант 4
# задание 3

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