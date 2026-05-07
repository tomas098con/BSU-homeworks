from Bio import SeqIO

def check_data(input_file):
    print('\n--- Задание1. Проверка ---')
    count_cds = 0
    unique_species = set()
    records = list(SeqIO.parse(input_file, 'genbank'))

    for i in records:
        cds = [y for y in i.features if y.type == 'CDS']
        count_cds += len(cds)

        species = i.annotations.get('source')
        unique_species.add(species)

        print(f'Вид: {species} | Колличество CDs: {len(cds)}')

    print('Общее колличество cds: ', count_cds)
    print('Уникальные виды: ', unique_species)

    if count_cds >10 and len(unique_species) == 2:
        print('\n\nУсловие соблюдается')
        return records
    else:
        print('\n\nУсловия нарушены')
        return None