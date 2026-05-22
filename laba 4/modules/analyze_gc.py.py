# Глецевич Карина 1-49
# Лабораторная работа 4, вариант 4
# задание 2

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

print(f"\nРезультаты сохранены в файл: {output_file}")

# for rec_id, desc, gc in gc_sort:
# print(f"{rec_id}: {desc}, GC = {gc}")

# задание 3
