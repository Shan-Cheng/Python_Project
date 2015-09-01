# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     Open the file and count the word
#
# Author:  Shan
# Date: May 8
# -----------------------------------------------------------------------------
"""
Counts the word frequency in the file and out put the word order file

find the longest word in the giving file, and find top 5 words that appear in
the txt file most . And out put the file that contains word order with times
appeared

"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random

# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


# Enter your own helper function definitions here

def count_words(filename):
    """
    build and return the dictionary for the given filename

    lower case of input file, eliminate the numerical word,
    the word with or without punctuation will be the same
    :parameter  filename: giving filename
    :return  word_dict : a dictionary that word as key, and counts as value
    """
    word_dict = {}

    with open(filename, 'r', encoding="utf-8") as my_file:
        for line in my_file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                if not (word.isdigit()):
                    for char in word:
                        if char in string.punctuation:
                           word = word.replace(char, "")
                    if word in word_dict:
                        word_dict[word] +=1
                    else:
                        word_dict[word] =1


    return word_dict


def report(word_dict):
    """
    report on various statistics based on the given word count dictionary

    report 1 => find the longest word
    report 2 => find the top 5 common word
    report 3 => write new file with each word counts ,sort by alphabetical
    :parameter word_dict :dictionary that contain word and count value
    :return none
    """

    word_list = sorted(word_dict, key=len)
    print("The longest word is :", max(word_list, key=len))

    common_words = sorted(word_dict, key=word_dict.get, reverse=True)
    five_common_words = {}
    for i in range(0, 5):
        five_common_words[common_words[i]] = word_dict.get(common_words[i])

    print("The 5 most common word are :", five_common_words)

    with open('out.txt', 'a', encoding='utf-8') as out_file:
        word_order = sorted(word_dict)
        for word in word_order:
            if word:
                out_file.write(word + ":" + str(word_dict[word]) + '\n')




def main():
    # get the input filename and save it in a variable
    user_input = input("please input the file name :")

    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    word_count = count_words(user_input)

    # call report to report on the contents of the dictionary
    report(word_count)


    # If you want to generate a word cloud, uncomment the line below.
    #draw_cloud(word_count,3)


if __name__ == '__main__':
    main()