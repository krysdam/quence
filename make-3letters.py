from collections import defaultdict


def words_from_file(fname:str) -> list:
    """Read the words from a text file. Skip # lines and blank lines."""
    words = []
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == '#':
                continue
            words.extend(line.split())
    return words

# Read in blocklists
blocklist_words = words_from_file('blocklist_words.txt')
blocklist_first3 = words_from_file('blocklist_first3.txt')
blocklist_last3 = words_from_file('blocklist_last3.txt')


# Read in 1grams
words = {}
with open('1grams-normcase-azonly.txt') as f:
    for line in f:
        word,count = line.split()
        if len(word) < 3:
            continue
        count = int(count)

        # Skip dregs
        if count < 1_000:
            break

        # Skip removed words
        if word in blocklist_words:
            continue

        words[word] = count


def pull_from_each_word(process, blocklist:list):
    """Process each Google 1gram, and return the total count of each output.

    "Counts" are 1gram frequencies from Google Ngrams.
    
    process: function to apply to each 1gram. Eg: lambda s: s[:3]
    blocklist: list of process outputs to ignore. Eg: exclude 'xii'
    
    Returns:
    outputs: dict from output to total count of 1grams that produced it
    sources: dict from output to list of first 10 1grams that produced it
    """

    outputs = defaultdict(int)
    sources = defaultdict(list)

    for word, count in words.items():
        output = process(word)
        if output in blocklist:
            continue
        outputs[output] += count
        if len(sources[output]) < 10:
            sources[output].append(word)
    
    return outputs, sources


def top_n_from_dict(d:dict, n:int) -> list:
    """Return the top n keys from a dict, sorted by value."""
    return sorted(d, key=d.get, reverse=True)[:n]

# Pull first-3-letters and last-3-letters from each word
first3s, _sources = pull_from_each_word(lambda x: x[:3], blocklist_first3)
last3s, _sources = pull_from_each_word(lambda x: x[-3:], blocklist_last3)

# Crop to top 6**4 (four 6-sided dice rolls)
first3s = top_n_from_dict(first3s, 6**4)
last3s = top_n_from_dict(last3s, 6**4)

# Sort alphabetically
first3s = sorted(first3s)
last3s = sorted(last3s)


# Write to files
with open('first3.txt', 'w') as f:
    for word in first3s:
        f.write(word + '\n')

with open('last3.txt', 'w') as f:
    for word in last3s:
        f.write(word + '\n')