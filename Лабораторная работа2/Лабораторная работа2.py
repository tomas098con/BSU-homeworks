import pandas as pd

df_amin = pd.read_csv("amino.csv", sep="\t")
print(df_amin)

mass_dict = dict(zip(df_amin["1-буква"], df_amin["Масса (сред.)"]))
print(mass_dict)

proteins = list(mass_dict.keys())
print(proteins)


protein_our = input("Введите вашу последовательность: ").upper().strip()
if len(protein_our) > 1000:
    print("Ошибка: текст слишком длинный!")

elif not set(protein_our).issubset(proteins):
    unsuitable_prot = set(protein_our) - set(proteins)
    print(f"Ошибка при вводе аминокислот!, недопустивые символы: {unsuitable_prot}")

else:
    total_mass = 0
    for i in protein_our:
        total_mass += mass_dict[i]
    total_mass_result = total_mass - 18.01056 * (len(protein_our) - 1)
    print(f"Итоговая масса: {total_mass_result}")
