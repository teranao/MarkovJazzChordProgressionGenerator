import markovify

# Get raw text as string.
with open("chords_sentence.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=3)

print(text_model.make_sentence())