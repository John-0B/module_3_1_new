calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    string = len(string), string.upper(), string.lower()
    count_calls()
    return string
def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i] or string[0].upper() == list_to_search[i][0] and string[-1].upper() == list_to_search[i][-1]:
            return True
    return False
print(string_info('Apple'))
print(string_info('Ice'))
print(string_info('Three'))
print(is_contains('Urban', ['ban', 'BaNaN', 'UrbaN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Word', ['Look', 'sMart', 'WORD']))
print(calls)
