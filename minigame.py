def minigame(): 
    item_list = []
    item = input("Write a word: ")
    while item:
        item_list.append(item)
        item = input('Write a word (empty ends): ')

    item_list.sort()
    print(f"The list has now been sorted by letters, congratulations!\nHere is the sorted list:\n{item_list}")
