# test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
# print("The original list is : " + str(test_list))
# res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
# print ("List after performing character swaps : " + str(res))
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
res = ", ".join(test_list)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')

print("List after performing character swaps : " + str(res))