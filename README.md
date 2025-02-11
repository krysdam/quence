# Quence

Quence is a password generator that makes short, memorable, high-entropy passwords.

It generates passwords that look like this (entropy shown in parentheses):

- `reshan.ratmer.thremi` (62 bits)
- `triona.yearcy.slitim.samork` (82 bits)
- `alefig.anachs.druboy.oremad.gerero` (103 bits)

# How to use

Quence has two versions: an automatic digital version, and a non-digital version that uses printed paper and dice. The digital version is fast and convenient and has more features, but the paper and dice version doesn't use computer-generated numbers and is therefore easier to confirm as secure.

## Digital version

Run `python3 make-password.py`. The output will look like this:

```
111!!!                              [ 19 bits]: 599^#*
firlas                              [ 20 bits]: whiney
firlas.firlas                       [ 41 bits]: nobbuy.ablaft
firlas.firlas.firlas                [ 62 bits]: lyigus.ingwen.fixeve
firlas.firlas.firlas.firlas         [ 82 bits]: autman.dosota.joueng.repova
firlas.firlas.firlas.firlas.firlas  [103 bits]: floark.rebrod.plodog.biondo.figtes

firlas!firlas!firlas                [ 68 bits]: burith+sequns=duegry
firlas!fir111!firlas                [ 68 bits]: pracke=fem937^sucaul
firlas!firlas!firlas!firlas         [ 92 bits]: binnct%breato&perhyl+popude
aaaaaa!aaaaaa1aaaaaa                [ 91 bits]: hvteqb&rwokjy8yywycu
```

The rightmost column is the randomly generated passwords, the middle column shows their entropy, and the left column shows their template, where `a` is a lowercase letter, `1` is a digit, `!` is a symbol, and `firlas` is a six-letter fake word (See [How it works](#How it works).)

Copy a password to where you want it, then close the terminal. You can also combine different passwords. For example, if you want the format `firlas.firlas.111!!!`, you can combine the `firlas.firlas` password with the `111!!!` password to make `nobbuy.ablaft.599^#*`.

## Paper version

Print `paper.pdf`. Follow the instructions there. You will need that printed document and a six-sided die (having two or four six-sided dice might make it easier.)

# Benefits over traditional password generators

Most password generators either make passwords from random characters, or from random words. Each method has its problems.

Random character generators make passwords that look like this:

- `BI0x=KFkq$` (61 bits)
- `+ULu#nG*NQtTx` (80 bits)
- `8gcfLh!5AKx+a71Xd` (104 bits)

These are very short. But they're hard to memorize, and even if you use a password manager, they're hard to hold in short-term memory (eg, when copying them from your phone's password manager to a friend's computer).

Using only a limited set of characters (such as lowercase letters) makes things a little easier:

- `bfvxnolhhewre` (61 bits)
- `loebxmvpseculilmaa` (85 bits)
- `atvybxwoypgviwzccfyyac` (103 bits)

But even these are tough to memorize or manually copy.

On the other hand, random word generators make passwords that look like this (using [EFF's short wordlist](https://www.eff.org/dice)):

- `dingy.bagel.swoop.coast.swim.state` (62 bits)
- `doll.dandy.ample.oval.stack.creme.drift.radio` (82 bits)
- `slurp.lasso.hub.fetch.sect.elope.stony.grope.tug.drove` (103 bits)

These are much easier to memorize and to manually copy. But they're much longer, so they take longer to type, and there are more places to make a mistake or misremember (ample/amble, creme/cream, etc.).

In contrast, Quence passwords are memorable and short, without sacrificing entropy.

### Memorable

Quence passwords are memorable. Here's a demonstration.

Choose one of the Quence passwords above. Try to memorize it, then open another window and type it in. Repeat until you get it exactly correct. Then try the same thing with the traditional random passwords above. 

If you're like me, it takes you half as much time and effort to memorize Quence passwords compared to traditional random-generated passwords. And if I step away for a few minutes and come back, I can recall the Quence password better than the others.

### Short

Quence passwords are short. Looking at only the 100-bit variants of each of the above password generation methods:

- `8gcfLh!5AKx+a71Xd` (Random characters = 17 characters)
- `atvybxwoypgviwzccfyyac` (Random letters = 22 characters)
- `alefig.anachs.druboy.oremad.gerero` (Quence = 34 characters)
- `slurp.lasso.hub.fetch.sect.elope.stony.grope.tug.drove` (Random words = 54 characters)

Quence passwords are about 40% shorter than random-word passwords on average. (Admittedly, they are also about twice the length of random-character passwords. However, I have not found Quence passwords to be unwieldy, even when they reach to 100 bits, that is, 34 characters).

### High-entropy

Quence, like all these schemes, is scalable to any given entropy. Each three letters of a Quence password (eg: "res", "han", "rat", etc) contributes just over 10 bits. This makes it easy to construct passwords of any desired entropy. For example, you can use a 100-bit version for a master password on a password manager, and 60-bit passwords for less sensitive accounts.

# How it works

Quence generates fake 6-letter words (eg: "reshan", "ratmer", etc). The first 3 letters of a word are drawn from a list of 1,296 3-letter sequences (found in `first3.txt`). This list is a compilation of the sequences of 3 letters that occur most frequently at the beginning of English words, as found in Google Ngrams. Therefore "res" is in the list (from "research", "results", "respect", "resources", etc), but "aar" doesn't make the cut (only in a few words: "aardvark", "Aaron").

The last 3 letters are drawn from a similar list of the 1,296 most common 3-letter sequences at the ends of English words. For example, "han" (from "than", "Jonathan", "Khan", "Nathan", etc).

Gluing a 3-letter sequence from the "firsts" list to a 3-letter sequence from the "lasts" list usually produces a coherent and memorable fake word. Sometimes the two parts are not compatible, and implausible words like "oatnto" are generated. However, most (70-85%) resultant words are coherent.

# A note on entropy

Because each list contains 1,296 elements which are drawn uniformly at random, each drawing of a 3-letter word-half contributes $log_2(1296) \approx 10.3$ bits of entropy, and each 6-letter word contributes twice that, or about 20.6 bits.

However, this entropy analysis assumes the attacker knows the generation scheme. If the attacker only knows a password's pattern is, for example, `aaaaaa.aaaaaa.aaaaaa`, then each 6-letter word contributes $log_2(26) * 6 \approx 28.2$ bits of entropy.
