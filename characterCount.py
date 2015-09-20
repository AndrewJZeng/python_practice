import pprint
message = "Once there was an ugly guy named Guyguy. One day, he died. The End"
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)