string = open("sherlock.txt", "r").read() # opened txt file as file object
listr = string[1151:1955].replace(",","").replace(".","").split()


trigram_list = [] # this is the list of trigrams
pair = () # these are the pair of words
for i in range(len(listr) - 2): #this is going through list using numbers generated by len of list
    pair = listr[i:i+2] # making pairs and followers
    follower = listr[i+2]
    for i in trigram_list: # i is each trigram in the list
        if i[0] == tuple(pair): # i[0] is the pairs in the list checking against new pairs
            i.append(follower) # if the same appending the existing trigram
            print("found")
        #if i[0] != tuple(pair):
        #    trigram_list.append(list((tuple(pair),follower)))
        #elif i[0] == tuple(pair): # i[0] is the pairs in the list checking against new pairs
            #print(tuple(pair))
         #   i.append(follower) # if the same appending the existing trigram
            #print(i)

            #print(i[0], "here")
            #print("same")     # isolating matching pairs!!! need to append to the match figure it out!!!
    #print(pair)


    trigram_list.append(list((tuple(pair),follower)))
for i in trigram_list:
    print(i)

