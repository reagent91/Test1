calls = 0
def count_calls():
   global calls
   calls += 1
def string_info(string):
    count_calls()
    print((len(string), string.upper(), string.lower()))
    return
def is_contains(string, list_to_search):
    count_calls()
    stroke = False
    string = string.lower()
    list_to_search_2 = [item.lower() for item in list_to_search]
    for i in list_to_search_2:
        if string == i:
            stroke = True
            break
        else:
            continue
    if stroke == True:
        print(True)
    else:
        print(False)



string_info("Capybara")
string_info("Armageddon")
is_contains('Urban', ['ban', 'BaNaN', 'urBAN',  'loha'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)

