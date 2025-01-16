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

        try:
            # Încearcă să traduci conținutul în limba română
            translated = translator.translate(content, src='en', dest='ro')
            # Verifică dacă răspunsul este valid
            translated_content = translated.text if translated else "Translation failed"
        except Exception as e:
            print(f"Eroare la traducerea fișierului {filename}: {e}")
            translated_content = "A apărut o eroare în timpul traducerii."

        # Creează un fișier nou pentru traducerea realizată
        new_filename = f"translated_{filename}"
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(translated_content)

        print(f"Fișier tradus: {filename} -> {new_filename}")
