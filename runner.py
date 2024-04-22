from trie import Trie

if __name__ == "__main__":
    trie = Trie()

    action = input("\nWhat would you like to do?\nType:\n - \"a\" to add a word\n - \"r\" to remove a word\n - \"s\" to search for a word\n - \"p\" for a list of autocomplete options based on an input prefix\n - \"d\" to display the trie\n - \"stop\" to end the program\nPlease choose one of the options above: ").lower()
    
    while action != "stop":
        print()
        if action == "a":
            word = input("Please enter a word to add: ")
            print()
            print(trie.add(word))

        elif action == "r":
            word = input("Please enter a word to remove: ")
            print()
            print(trie.delete(word))
            
        elif action == "s":
            word = input("Please enter a word to search for: ")
            print()
            print(trie.search(word))

        elif action == "p":
            prefix = input("Please enter a prefix to find autocomplete suggestions for: ")
            print()
            print(trie.autocompleteList(prefix))

        elif action == "d":
            print(trie.display())

        else:
            print("Invalid input. Please try again.")
        print()

        action = input("What would you like to do now?\nType:\n - \"a\" to add a word\n - \"r\" to remove a word\n - \"s\" to search for a word\n - \"p\" for a list of autocomplete options based on an input prefix\n - \"d\" to display the trie\n - \"stop\" to end the program\nPlease choose one of the options above: ").lower()
    
    print("\nThe program has ended. Bye!\n")