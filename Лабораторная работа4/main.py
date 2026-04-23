from Bio import SeqIO
from task2 import run_task_2 
from task3 import run_task_3

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

    print('Общее колличество cds:', count_cds)
    print('Колличество уникальных видов', unique_species)

    if count_cds >10 and len(unique_species) == 2:
        print('\n\nУсловие соблюдается')
        return records
    else:
        print('\n\nУсловия нарушены')
        return None
    
def main():
    input_file = 'sequence (1).gb'
    data = check_data(input_file)

    if data:
        result_2 = run_task_2(data)
        result_3 = run_task_3(data)

        print('Все задачи выполнены')


if __name__ == "__main__":
    main()
