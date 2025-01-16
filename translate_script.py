import os
from googletrans import Translator

# Configure translator
translator = Translator()

# Folderul unde se află fișierele HTML
directory = '.'

# Iterează prin toate fișierele din director
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Traduce conținutul în limba română
        translated_content = translator.translate(content, src='en', dest='ro').text

        # Salvează traducerea într-un nou fișier
        new_filename = f"translated_{filename}"
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(translated_content)

        print(f"Tradus: {filename} -> {new_filename}")
