from flask import Flask, request, jsonify, render_template
from trie import Trie

app = Flask(__name__)

# Initialize Trie or import your Trie implementation
trie = Trie()

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle adding a word
@app.route('/add_word', methods=['POST'])
def add_word_route():
    data = request.json
    word = data['word']
    result = trie.add(word)
    return jsonify({'result': result})

# Route to handle adding a list of words
@app.route('/add_words', methods=['POST'])
def add_words_route():
    data = request.json
    words = data['words']
    result = trie.addList(words)
    return jsonify({'result': result})

# Route to handle removing a word
@app.route('/remove_word', methods=['POST'])
def remove_word_route():
    data = request.json
    word = data['word']
    result = trie.delete(word)
    return jsonify({'result': result})

# Route to handle searching a word
@app.route('/search_word', methods=['POST'])
def search_word_route():
    data = request.json
    word = data['word']
    result = trie.search(word)
    return jsonify({'result': result})

# Route to handle prefix match
@app.route('/prefix_match', methods=['POST'])
def prefix_match_route():
    data = request.json
    prefix = data['prefix']
    result = trie.autocompleteList(prefix)
    return jsonify({'result': result})

# Route to handle displaying the Trie
@app.route('/display_trie')
def display_trie_route():
    return jsonify({'result': trie.display()})

if __name__ == '__main__':
    app.run(debug=True)
