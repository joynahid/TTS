from phonemizer import phonemize

def bangla_text_to_phonemes(text):
  phonemized_text = phonemize(text, "bn", "espeak", language_switch="remove-flags")
  return phonemized_text

