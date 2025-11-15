import random
def get_words_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        words = content.split()
        return words
    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []
def get_random_sentence(length, file_path="words.txt"):
    words_list = get_words_from_file(file_path)
    if not words_list:
        return "Impossible de générer une phrase : liste de mots vide."

    random_words = [random.choice(words_list) for _ in range(length)]
    sentence = " ".join(random_words).lower()
    return sentence
def main():
    print("Bienvenue ! Ce programme génère une phrase aléatoire à partir d'une liste de mots.")
    user_input = input("Entrez la longueur de la phrase souhaitée (entre 2 et 20) : ")

    try:
        length = int(user_input)
        if length < 2 or length > 20:
            print("Erreur : la longueur doit être comprise entre 2 et 20.")
            return
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier.")
        return
    sentence = get_random_sentence(length)
    print(f"Phrase générée : {sentence}")

if __name__ == "__main__":
    main()
