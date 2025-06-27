from stats import num_words, get_book_text, count_characters

def main():
    #print(num_words(),"words found in the document")

    book_text = get_book_text("books/frankenstein.txt")

    char_counts = count_characters(book_text)

    print("Character counts:")
    print(char_counts)
    
main()