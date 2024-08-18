import secrets
import math


first3 = []
last3 = []

with open('first3.txt', 'r') as f:
    first3 = f.read().splitlines()

with open('last3.txt', 'r') as f:
    last3 = f.read().splitlines()


class Cast():
    """A collection of strings that can be used to generate a password.

    Label: a single character to indicate this cast in a pattern.
    Representative: an iconic member of the cast used for showing the pattern.
    Members: all members of the cast.
    
    For example, lowercase letters:
        The members are a-z.
        "l" is the conventional label for letters in password patterns.
        "a" is an iconic lowercase letter.

    Labels and repsentatives are separate because
    in some cases, the representative must be multiple characters
    (e.g. "fir" for the first three letters of a name),
    while it's convenient to have a single character for the label.
    """
    def __init__(self, label, representative, members):
        self.label = label
        self.representative = representative
        self.members = members

    def generate(self):
        return secrets.choice(self.members)

    def __str__(self):
        return self.representative

casts = [
    Cast('l', 'a', 'abcdefghijklmnopqrstuvwxyz'),
    Cast('d', '1', '0123456789'),
    Cast('s', '!', '!@#$%^&*=+'),
    Cast('F', 'fir', first3),
    Cast('L', 'las', last3),
]

patterns = [
    'dddsss',
    'FL',
    'FL.FL',
    'FL.FL.FL',
    'FL.FL.FL.FL',
    'FL.FL.FL.FL.FL',
    '',
    'FLsFLsFL',
    'FLsFdddsFL',
    'FLsFLsFLsFL',
    'llllllslllllldllllll',
]


def generic_password(pattern:str) -> str:
    """Create a generic (all-representative) password from a pattern."""
    password = ''
    for c in pattern:
        for cast in casts:
            if c == cast.label:
                password += cast.representative
                break
        else:
            password += c
    return password

def generate_password(pattern:str) -> str:
    """Create a random password from a pattern."""
    password = ''
    for c in pattern:
        for cast in casts:
            if c == cast.label:
                password += cast.generate()
                break
        else:
            password += c
    return password

def calculate_entropy(pattern:str) -> float:
    """Calculate the entropy of a pattern."""
    entropy = 0
    for c in pattern:
        for cast in casts:
            if c == cast.label:
                entropy += math.log2(len(cast.members))
                break
        else:
            entropy += 0
    return entropy


# For each pattern,
# print the generic password, the generated password, and the entropy.
for pattern in patterns:
    if pattern == '':
        print()
        continue

    generic = generic_password(pattern)
    password = generate_password(pattern)
    entropy = calculate_entropy(pattern)
    print(f'{generic:35} [{entropy:3.0f} bits]: {password}')