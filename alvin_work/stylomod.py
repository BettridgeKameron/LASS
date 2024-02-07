from spellchecker import SpellChecker

def num_errors(text):
    total = len(text.split())
    if total == 0:
        return 0
    checker = SpellChecker()
    amount_miss = len(checker.unknown(text.split()))
    return amount_miss / total
