text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)


def add_ing(word):
    # Check if the word ends with a comma or dot
    if word[-1] in ",.":
        return word[:-1] + "ing" + word[-1]
    else:
        return word + "ing"

# Splitting the text into individual words
words = text.split()

# Adding 'ing' to each word while considering punctuation
modified_words = [add_ing(word) for word in words]

# Joining the modified words back together
modified_text = ' '.join(modified_words)

print(modified_text)
