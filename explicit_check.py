import better_profanity

def explicit_check(text):
    if better_profanity.profanity.contains_profanity(text):
        print(f'explicit word: {text}')
    else:
        print(f'not explicit word: {text}')
