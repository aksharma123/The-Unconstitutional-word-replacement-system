import re

def tokenize_text(text):
    return re.findall(r'\b\w+\b', text)

def replace_bad_words(paragraph, word_replacements):
    replaced_paragraph = paragraph
    for bad_word, good_word in word_replacements.items():
        
        red_bad_word = f'\033[31m{bad_word}\033[0m'
        green_good_word = f'\033[32m{good_word}\033[0m'
        
        replaced_paragraph = re.sub(r'\b{}\b'.format(re.escape(bad_word)), green_good_word, replaced_paragraph, flags=re.IGNORECASE)
        
        paragraph = re.sub(r'\b{}\b'.format(re.escape(bad_word)), red_bad_word, paragraph, flags=re.IGNORECASE)
    return paragraph, replaced_paragraph

def get_user_input(prompt):
    return input(prompt)

def load_word_replacements(file_path, delimiter=','):
    word_replacements = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    words = line.split(delimiter)
                    if len(words) == 2:
                        bad_word, good_word = words
                        word_replacements[bad_word.strip()] = good_word.strip()
                    else:
                        print(f"Ignoring line: {line}. Expected format: 'bad_word{delimiter}good_word'")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return word_replacements

def main():
    paragraph = get_user_input("Enter the paragraph you want to change:\n\n")

    file_path = 'word_replacements.txt'
    word_replacements = load_word_replacements(file_path)

    tokens = tokenize_text(paragraph)

    highlighted_paragraph, replaced_paragraph = replace_bad_words(paragraph, word_replacements)

    print("\nOriginal paragraph with unconstitutional words highlighted:\n")
    print(highlighted_paragraph)
    
    print("\nReplaced paragraph:\n")
    print(replaced_paragraph)

if __name__ == "__main__":
    main()
