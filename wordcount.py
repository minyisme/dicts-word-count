def count_all_the_things(text_file):
    """Takes a file and returns a dictionary of all the words as keys and 
    the count of those words as the values

    count_all_the_things(file containing: "This is a test test")
    This 1
    is 1
    a 1
    test 2

    """

    file_to_count = open(text_file)

    wordcounts = {}

    for line in file_to_count:
        # Iterating through each word in the file
        for word in line.split():
            # Add or increment the value corresponding to word
            wordcounts[word] = wordcounts.get(word,0) + 1

    file_to_count.close()

    for word, count in wordcounts.iteritems():
        print word, count

    return None



count_all_the_things("test.txt")
print ""
print ""
count_all_the_things("twain.txt")
