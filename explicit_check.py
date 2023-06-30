import better_profanity

def explicit_check(text):
    if better_profanity.profanity.contains_profanity(text):
        print('yabe word')
    else:
        print('not yabe word')
