from trie import Trie

if __name__ == "__main__":
    trie = Trie()

    introString = "\nWhat would you like to do?\nType:\n - \"a\" to add a word\n - \"al\" to add a list of words\n - \"r\" to remove a word\n - \"s\" to search for a word\n - \"p\" for a list of autocomplete options based on an input prefix\n - \"d\" to display the trie\n - \"stop\" to end the program\nPlease choose one of the options above: "
    action = input(introString).lower()
    
    while action != "stop":
        print()
        if action == "a":
            word = input("Please enter a word to add: ").lower()
            print()
            print(trie.add(word))

        # For random words: https://commentpicker.com/random-word-generator.php
        elif action == "al":
            words = input("Please enter a list of words (space-separated) to add: ").lower()
            print()

            print(trie.addList(words.split()))

        elif action == "r":
            word = input("Please enter a word to remove: ").lower()
            print()
            print(trie.delete(word))
            
        elif action == "s":
            word = input("Please enter a word to search for: ").lower()
            print()
            print(trie.search(word))

        elif action == "p":
            prefix = input("Please enter a prefix to find autocomplete suggestions for: ").lower()
            print()
            print(trie.autocompleteList(prefix))

        elif action == "d":
            print(trie.display())

        else:
            print("Invalid input. Please try again.")

        print()
        action = input(introString).lower()
    
    print("\nThe program has ended. Bye!\n")