# Задание 3. Трансляция
import textwrap

def run_task_3(data):
    print("\n--- Задание 3: Трансляция ---")
    list_a = []

    with open('output/translate_sequences.txt', 'w', encoding= 'utf-8') as q:
        for record in data:
            name = record.description
            id = record.id
            for f in record.features:
                if f.type == 'CDS':
                    start = f.location.start
                    end = f.location.end
                    strand_ = f.location.strand
                    strand_symbol = '+' if strand_ == 1 else '-'
        
                    trans = f.qualifiers.get('translation', [''])[0]

                    header = f"{id}: {name}"
                    wrapped_header = textwrap.fill(header, width=55, 
                                                initial_indent='     ' )
                    loc_info = f'     Coding sequence location: [{start}:{end}] ({strand_symbol})'
                    print(wrapped_header)
                    print(loc_info)
                    print('     Translation =')

                    q.write(wrapped_header + '\n')
                    q.write(loc_info + '\n')
                    q.write('     Translation =\n')

                    for i in range(0, len(trans), 60):
                        print(trans[i:i+60])
                        q.write(trans[i:i+60] + '\n')

                

    
            