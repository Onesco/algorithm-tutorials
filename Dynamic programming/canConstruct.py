
'bruteforce method'
def can_construct(target, characters):
    if target == '':
        return True

    for char in characters:
        reminderTargetWord = target.replace(char,'',1)
        if(reminderTargetWord != target):
            return can_construct(reminderTargetWord, characters)

    return False


'memorization method attempt there is no difference in the above two method in terms of efficiency'
def can_construct2(target, characters, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for char in characters:
        reminderTargetWord = target.replace(char,'',1)
        if(reminderTargetWord != target):
            memo[reminderTargetWord] = can_construct2(reminderTargetWord, characters, memo)
            return memo[reminderTargetWord]
    memo[target] = False
    return memo[target]

print(can_construct('johnooooojohnooooojohnooooojohnooooo', ['j','h','n', 'o', 'j','h','n', 'o', 'j','h','n', 'o']))

print(can_construct2('johnooooojohnooooojohnooooojohnooooo', ['j','h','n', 'o', 'j','h','n', 'o', 'j','h','n', 'o']))