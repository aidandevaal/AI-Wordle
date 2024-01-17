
update_dict = open("wordlist.txt","r")

len5 = [line for line in update_dict if len(line.strip())==5]

update_dict.close()

newList = open("wdict.txt","w")

newList.write(''.join(len5))

update_dict.close()
newList.close()