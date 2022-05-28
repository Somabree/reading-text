# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("D:\Zuri Training\Reading-Text-Files\story.txt", "r") as f:  #using open as a method for reading files
        text = f.read()
    return text 

    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()    #using to split
    count = {}
    for word in split_text:
        count[word] = split_text.count(word)
    return count

print(count_words())