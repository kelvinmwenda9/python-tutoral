class MyFirstClass:
    print("Who wrote this?")
    # class variable as it is declared within a class
    index = "Author-Book"

    def hand_list(self, philospher, book):
        print(philospher + " wrote the book: " + book)

whodunnit = MyFirstClass()

whodunnit.hand_list("Sun Tzu", "The Art of War")
