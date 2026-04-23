# Задание 2. GC-составы

import textwrap
import pandas as pd
from Bio import SeqIO

def run_task_2(data):
    print('\n--- Задание 2: GC-состав ---')    
    result_list=[]
    for record in data:
        nucleotides = record.seq.upper()
        count_C = nucleotides.count('C')
        count_G = nucleotides.count('G')
        percent = (count_C+count_G)/ len(nucleotides)

        name = record.annotations.get('source')
        id = record.id
        result_list.append((id, record.description, percent))

    result_list.sort(key= lambda x: x[2])

    for id, dec, per in result_list:
        text = f'{id}: {dec}, GC= {per}'
        wrapped_text = textwrap.fill(text, width=65,
                                    initial_indent='     ')
        print(wrapped_text)
        