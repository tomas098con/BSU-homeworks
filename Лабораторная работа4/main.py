from Bio import SeqIO

from modules.fetch_sequences import check_data
from modules.analyze_gc import run_task_2
from modules.translate_sequences import run_task_3


def main():
    input_file = "sequence (1).gb"
    data = check_data(input_file)

    if data:
        result_2 = run_task_2(data)
        result_3 = run_task_3(data)

        print("Все задачи выполнены")


if __name__ == "__main__":
    main()
