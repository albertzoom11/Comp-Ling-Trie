# Python trie class used to store nodes in the data structure with methods to allow customization and access
# HackerRank video referenced to understand tries: https://www.youtube.com/watch?v=zIjfhVPRZCg
class Trie:
    def __init__(self):
        self.root = Node(True)


    def add(self, word):
        if len(word) == 0:
            return "\"" + word + "\" is not a valid word to add to the trie."

        if (self.search(word) == "\"" + word + "\" is a word in the trie."):
            return "\"" + word + "\" is already in the trie."
        current = self.root
        for char in word:
            if (char not in current.children):
                current.children[char] = Node(False)
            current = current.children[char]
        current.isWord = True
        return "\"" + word + "\" has been added to the trie."


    def delete(self, word):
        if len(word) == 0:
            return "\"" + word + "\" is not a valid word to delete from the trie."
        
        deleteFrom = Node(False)
        deleteLetter = ''
        current = self.root
        for char in word:
            if (char not in current.children):
                return "\"" + word + "\" is not a word in the trie."
            if len(current.children) > 1 or current.isWord:
                deleteFrom = current
                deleteLetter = char
            current = current.children[char]

        if not current.isWord:
            return "\"" + word + "\" is not a word in the trie."
        if bool(current.children):
            current.isWord = False
        else:
            del deleteFrom.children[deleteLetter]
        return "\"" + word + "\" has been deleted from the trie."


    def search(self, word):
        if len(word) == 0:
            return "\"" + word + "\" is not a word in the trie."

        current = self.root
        for char in word:
            if (char not in current.children):
                return "\"" + word + "\" is not a word in the trie."
            current = current.children[char]
        return "\"" + word + "\" is a word in the trie." if current.isWord else "\"" + word + "\" is not a word in the trie."


    def autocompleteList(self, prefix):
        if len(prefix) == 0:
            return "You entered an empty string. To see the full trie, display the trie."
        
        current = self.root
        output = []
        for i, char in enumerate(prefix):
            if (char not in current.children):
                return "The prefix \"" + prefix + "\" is not in the trie."
            current = current.children[char]
            if i == len(prefix)-1 and current.isWord:
                output.append(prefix)
        output += [prefix + suffix for suffix in self.listWords(current)]
        if output == [prefix]:
            return "The only word with the prefix \"" + prefix + "\" is \"" + prefix + "\"."
        return "Autocomplete suggestions list for the prefix \"" + prefix + "\": " + str(output)

    # Stack Overflow reference on recursive function for listing words in trie: 
    # https://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words
    # I implemented different conditioning to follow the attributes and constraints of my Node class.
    def listWords(self, trie):
        output = []
        for letter, node in trie.children.items():
            if not node.isWord:
                for word in self.listWords(node):
                    output.append(letter + word)
            elif node.children:
                output.append(letter)
                for word in self.listWords(node):
                    output.append(letter + word)
            else:
                output.append(letter)
        return output


    def display(self):
        contents = self.listWords(self.root)
        if not contents:
            return "The trie is empty."

        output = "Contents of Trie:"
        for word in contents:
            output += "\n" + word
        return output


class Node:
    def __init__(self, isWord):
        self.isWord = isWord
        self.children = {}