import os
from arquiLib import *

name_file = "Lista Mangas"

def ensure_manga_folder():
    # Pega o user local
    username = os.environ.get('USERNAME')
    try:
        # Tenta acessar a pasta Manga
        os.chdir(fr"C:\Users\{username}\Documents\Manga")
        return True

    except FileNotFoundError:
        # Se não conseguir encontrar a pasta manga cria uma e acessa nela
        os.mkdir(fr"C:\Users\{username}\Documents\Manga")
        os.chdir(fr"C:\Users\{username}\Documents\Manga")
        return False
    except Exception as e:
        print(f'Erro ao criar a pasta: {e}')

def check_read_manga(_name):
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            for mangas in file:
                parts = mangas.split("-")

                # Se não tiver capítulo, acrescenta "0"
                if len(parts) == 1:
                    manga   = parts[0].strip().title()
                    chapter = "0"
                else:
                    manga   = parts[0].strip().title()
                    chapter = parts[1].strip()

                if name.strip().title() == manga:
                    print('Manga/Manhawa já cadastrado !\n')
                    print(f'{manga} - {chapter}')
                    return True
            print(f'{name.title()} não encontrado')
            return False
    except Exception as e:
        print(f'Erro: {e}')
def read_positive_integer():
    while True:
        value = input("Informe o Capitulo do manga/manhwas: ")
        try:
            number = int(value)
            if number > 0:
                return number
            else:
                print("Erro: o número deve ser inteiro e positivo.")
        except ValueError:
            print("Erro: entrada inválida, digite apenas números inteiros.")


def register_new_manga(_name):
    try:
        chapter = read_positive_integer()

        with open(name_file, 'a', encoding='utf-8') as file:
            file.write(f'\n{name.strip().title()} - {chapter}')

        print('Manga/Manhwa cadastrado com sucesso !')
    except Exception as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    ensure_manga_folder()
    if not file_exists(name_file):
        create_file(name_file)

    name = input('Informe o nome do manga/manhwas: ')
    #check_read_manga(name)
    register_new_manga(name)
