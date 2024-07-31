from collections import defaultdict

words = defaultdict(int)

data_dir = 'google-ngrams'

# Process each of the 24 files
for n in range(24):
    fname = f'1-{n:05d}-of-00024'
    print(f'Processing {fname}...')

    with open(f'{data_dir}/{fname}') as f:
        for line in f:
            # Example:
            # cabbage   1959,1,1    1961,10,6   2001,100,15
            # word      year,count in that year, works in that year
            # Only the word and count matter
            word,*parts = line.split()

            # Normalize the word
            word = word.lower()

            # Ignore words containing non [a-z] characters
            valid = True
            for c in word:
                if not ('a' <= c <= 'z'):
                    valid = False
                    break
            if not valid:
                continue
            # It appears that an un-tagged word (eg, "cabbage")
            # has the full count for that word,
            # while the tagged forms (eg, "cabbage_NOUN")
            # are each a subset of that full count.
            # The sum of the tagged counts <= the untagged count,
            # but always approximately equal.

            # Add up the counts
            for part in parts:
                year,count,works = part.split(',')
                words[word] += int(count)

# Write words and their counts to file
top = sorted(words.items(), key=lambda x: x[1], reverse=True)
with open('1grams-normcase-azonly.txt', 'w') as f:
    for word,count in top:
        # Skip dregs (leaves about 15% most common tokens)
        if count < 1000:
            break
        f.write(f'{word}\t{count}\n')