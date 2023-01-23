phrase = input("Insert a phrase: ").upper().strip()
print("""Letter A Counter: {}
First Appearance: {}
Last Appearance: {}
""".format(phrase.count('A'), phrase.find('A')+1, phrase.rfind('A')+1))
