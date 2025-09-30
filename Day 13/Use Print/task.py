# word_per_page = 0 # Before debugging
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Before debugging
word_per_page = int(input("Number of words per page: ")) # After debugging
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)
