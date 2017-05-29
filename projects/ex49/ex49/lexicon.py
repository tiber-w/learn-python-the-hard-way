def scan(sentence):
    tuples = []
    words = sentence.split()
    for word in words:
        low_word = word.lower()
        if low_word in ('north','south','east','west','down','up','left','right'
                ,'back'):
            tuples.append(('direction', word))
        elif low_word in ('go','stop','kill','eat'):
            tuples.append(('verb', word))
        elif low_word in ('the','in','of','from','at','it'):
            tuples.append(('stop', word))
        elif low_word in ('door','bear','princess','cabinet'):
            tuples.append(('noun', word))
        else:
            num = convert_number(word)
            if num is None:
                tuples.append(('error', word))
            else:
                tuples.append(('number', num))
    return tuples

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
