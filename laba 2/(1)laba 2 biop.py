#Глецевич Карина 49 группа #немного не сходится со значениями в in и out с портала из-за неточных молярных масс аминокислот и воды
#лабораторная работа 2, вариант 4

from Bio.SeqUtils import molecular_weight
from Bio.Seq import Seq

b = input().strip()
if len(b)>1000:
    print('Длинна последоваительности превышает 1000 ак')
    exit()
    
seq = Seq(b)

w = molecular_weight(seq, seq_type='protein', monoisotopic=True)
mol_m_water = 18.01528
ww = w-mol_m_water

print(ww)
