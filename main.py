import os
from arquiLib import *

name_file = "Lista Mangas/Manhwas"

def ensure_manga_folder():
    ## Melhor solução ???Ver melhoria
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


def normalize_manga():
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split("-")

            if len(parts) == 1:
                manga   = parts[0].strip().title()
                _chapter = "0"
            else:
                manga   = parts[0].strip().title()
                _chapter = parts[1].strip()

            new_lines.append(f"{manga} - {_chapter}\n")

        with open(name_file, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        #print("Arquivo atualizado: todos os mangas agora têm capítulo.")
    except Exception as e:
        print(f"Erro: {e}")


def check_read_manga(_name):
    format_name = " ".join(_name.strip().title().split())
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            for mangas in file:
                parts = mangas.split("-")

                manga   = parts[0].strip().title()
                _chapter = parts[1].strip()

                if format_name == manga:
                    print('\nManga/Manhawa já cadastrado !\n')
                    print(f'{manga} - {_chapter}')
                    return True
            print(f'\n{format_name.title()} não encontrado\n')
            return False
    except Exception as e:
        print(f'Erro: {e}')


def read_positive_int():
    ## Função Auxiliar que detecta se o numero é um int positivo
    while True:
        value = input('Informe o numero do capitulo: ')
        try:
            number = int(value)
            if number > 0:
                return number
            else:
                print("Erro: o número deve ser inteiro e positivo.")
        except ValueError:
            print("Erro: entrada inválida, digite apenas números inteiros.")

def register_new_manga(_name, _chapter=0):
    format_name = " ".join(_name.strip().title().split())
    try:
        with open(name_file, 'a', encoding='utf-8') as file:
            file.write(f'{format_name} - {_chapter}')

        print('\nManga/Manhwa cadastrado com sucesso !')
    except Exception as e:
        print(f'Erro: {e}')


def ask_registration(text):
    # Melhora esta ruim
    while True:
        registers = input(f"{text} (Y/N)? ").strip()
        if registers.upper() == "Y":
            return True
        elif registers.upper() == "N":
            return False
        else:
            print("Entrada inválida. Digite apenas Y ou N.")


def reset_manga(_name):
    format_name = " ".join(_name.strip().title().split())
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split("-")
            if not line.strip():
                continue

            manga = parts[0].strip().title()
            _chapter = parts[1].strip() if len(parts) > 1 else "0"

            if format_name == manga:
                new_lines.append(f"{manga} - {0}\n")
            else:
                new_lines.append(f'{manga} - {_chapter}\n')
        with open(name_file, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        print(f"o mangá {format_name} foi zerado com sucesso.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    ensure_manga_folder()

    if not file_exists(name_file):
        create_file(name_file)

    normalize_manga()

    name = input('Informe o nome do manga/manhwas: ')

    if check_read_manga(name):
        if ask_registration("Deseja reiniciar o manga/manhwa"):
            reset_manga(name)

    else:
        if ask_registration("Deseja cadastrar"):
            chapter = read_positive_int()
            register_new_manga(name, chapter)
    print('\nAté mais cowboy!')