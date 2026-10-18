# Exercise 8.12.1 - Ask a Virtual Assistant
# In this chapter, we only scratched the surface of what regular expressions can do. To get an idea of what’s possible,
# ask a virtual assistant, “What are the most common special characters used in Python regular expressions?”
# You can also ask for a pattern that matches particular kinds of strings. For example, try asking:
# Write a Python regular expression that matches a 10-digit phone number with hyphens.
# Write a Python regular expression that matches a street address with a number and a street name,
# followed by ST or AVE.
# Write a Python regular expression that matches a full name with any common title like Mr or Mrs followed by any
# number of names beginning with capital letters, possibly with hyphens between some names.
# And if you want to see something more complicated, try asking for a regular expression that matches any legal URL.
# A regular expression often has the letter r before the quotation mark, which indicates that it is a “raw string”.
# For more information, ask a virtual assistant, “What is a raw string in Python?”

# Claude Opus 5.5 had the following to say:

#
# ======================================================================================================================
#   LIVE FROM AUSTIN, TEXAS: "THE HIGH SCORE" - Round 8: Regular Expressions
#   Contestants: Snoop Dogg (Long Beach, CA) vs. Willie Nelson (Abbott, TX)
#   Rules: Answer the question, then take a hit. Get one wrong and you pass the joint.
# ======================================================================================================================
#
# ANNOUNCER: Gentlemen, first question. What are the most common special characters used in Python regular expressions?
#
# SNOOP: *exhales slowly* Ayy, check it out, nephew. Regular expressions is like a dress code for strings, ya dig?
#   You tell Python what the string gotta look like, and it lets in only the ones that fit. Here go the crew:
#
#     .     Matches any single character except a newline. The wildcard. Rolls with anybody.
#     ^     Start of the string. Gotta be first in line, like me at the dispensary.
#     $     End of the string. Last call, baby.
#     *     Zero or more of the thing before it. Could be none, could be a whole lotta.
#     +     One or more. At LEAST one. Like puffs per round.
#     ?     Zero or one, makes the thing before it optional. Also makes * and + "lazy" when you put it after 'em.
#     {m,n} Between m and n repeats. {3} means exactly three. Precise, like my rhymes.
#     [ ]   A character class. [aeiou] matches any one vowel. [^aeiou] matches anything that ain't one.
#     |     OR. cat|dog matches either one. Options, nephew.
#     ( )   A group. Bundles stuff together and captures what matched so you can pull it out later.
#     \     Escape. Turns a special character into a regular one: \. is a real period, not the wildcard.
#
# WILLIE: *takes a long, thoughtful drag* Well now, Snoop, that's a fine list. But you left off the shorthand
#   characters, and those are about as handy as a guitar with all six strings:
#
#     \d    Any digit, 0 through 9.             \D   Anything that ain't a digit.
#     \w    A "word" character: letter, digit, or underscore.   \W   The opposite.
#     \s    Whitespace: space, tab, newline.    \S   Anything that ain't whitespace.
#     \b    A word boundary. Matches the spot between a word character and a non-word character,
#           so r'\bcat\b' finds "cat" but not the "cat" hiding inside "concatenate".
#
# ANNOUNCER: Both answers accepted. Both contestants take a hit.
#
# ----------------------------------------------------------------------------------------------------------------------
# ANNOUNCER: Round two. Write a Python regular expression that matches a 10-digit phone number with hyphens.
#
# WILLIE: I've been on the road since before area codes, son. Here's how she goes:
#
#     phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
#
#   Three digits, a hyphen, three digits, a hyphen, four digits. That \b on each end makes sure
#   you don't grab the middle of some longer number, like 1-800-555-1234-5678. Simple, like a good country song.
#   Three chords and the truth. Or in this case, three groups and some hyphens.
#
# SNOOP: That's clean, Unc. Fo' shizzle.
#
# ----------------------------------------------------------------------------------------------------------------------
# ANNOUNCER: Round three. Write a Python regular expression that matches a street address with a number and a street
# name, followed by ST or AVE.
#
# SNOOP: *coughs* Hold up, hold up. Okay. I got this one, 'cause I know my way around Long Beach:
#
#     address_pattern = r'\b\d+\s+(?:[A-Z][a-z]*\s+)*[A-Z][a-z]*\s+(?:ST|AVE)\b\.?'
#
#   Let me break it down slow for the folks at home:
#     \d+                  The house number. One or more digits.
#     \s+                  Some space.
#     (?:[A-Z][a-z]*\s+)*  Any extra words in the street name, each one capitalized, like "Martin Luther King".
#                          The ?: means "group this, but don't bother capturing it." Non-capturing group.
#     [A-Z][a-z]*          The last word of the street name.
#     \s+(?:ST|AVE)\b      Space, then either ST or AVE, then a word boundary so "STREET" don't sneak in.
#     \.?                  An optional period, for folks who write "AVE." all fancy.
#
#   So "1234 Ocean AVE" matches. "21 Jump ST" matches. "Snoop Lane" don't, 'cause there's no number and no ST or AVE.
#   If you want lowercase "st" and "ave" too, pass re.IGNORECASE, but then the capital-letter check gets loose too.
#
# WILLIE: *nods, hands Snoop the joint* That's a mighty fine regex, Snoop.
#
# ----------------------------------------------------------------------------------------------------------------------
# ANNOUNCER: Round four. Write a Python regular expression that matches a full name with any common title like Mr or
# Mrs, followed by any number of names beginning with capital letters, possibly with hyphens between some names.
#
# WILLIE: Now this is a name game, and I know a thing or two about names. Mine's on a highway. Here:
#
#     name_pattern = r'\b(?:Mr|Mrs|Ms|Miss|Dr|Prof)\.?(?:\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*)+'
#
#   Piece by piece, like tuning Trigger:
#     (?:Mr|Mrs|Ms|Miss|Dr|Prof)  The title. The | means "any one of these."
#     \.?                         An optional period, so "Mr." and "Mr" both work.
#     \s+[A-Z][a-z]+              A space, then a name: one capital letter followed by lowercase letters.
#     (?:-[A-Z][a-z]+)*           Zero or more hyphenated pieces stuck on, like "Smith-Jones".
#     ( ... )+                    The whole name chunk repeats one or more times, for as many names as you've got.
#
#   So "Mr. Willie Hugh Nelson" matches, "Mrs. Mary Smith-Jones" matches, and "Dr Calvin Cordozar Broadus" matches,
#   which, if I'm not mistaken, is my opponent's given name.
#
# SNOOP: Ha! He did his homework. Respect, Unc. Though nobody calls me Dr. That's my homie Dre.
#
# ----------------------------------------------------------------------------------------------------------------------
# ANNOUNCER: Bonus round, for double points. A regular expression that matches any legal URL.
#
# SNOOP: *long pause* ... Man, that's the one that'll get you, nephew. Legal URLs got schemes, usernames,
#   passwords, domains, IP addresses, ports, paths, query strings, fragments, percent-encoding, international
#   characters... The official rulebook for it, RFC 3986, is long enough to roll up and smoke. A regex that catches
#   EVERY legal URL is gonna be hundreds of characters of pure chaos. Here's a practical one that handles
#   the everyday http and https stuff:
#
#     url_pattern = (r'\bhttps?://'                           # scheme: http:// or https://
#                    r'(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}'      # domain: snoopdogg.com, www.example.co.uk
#                    r'(?::\d{1,5})?'                         # optional port, like :8080
#                    r'(?:/[^\s?#]*)?'                        # optional path, like /music/albums
#                    r'(?:\?[^\s#]*)?'                        # optional query string, like ?track=gin-and-juice
#                    r'(?:#[\w-]*)?')                         # optional fragment, like #chorus
#
# WILLIE: And here's the wisdom that comes with age, Snoop: when you need to really check a URL, don't fight it with
#   a regex. Use the tools Python already gives you. urllib.parse.urlparse() splits a URL into its parts, and you
#   can check those parts one at a time. Regex is good for FINDING things that look like URLs in a pile of text.
#   It's a poor fit for deciding whether something is legal. Even finding gets tricky: if a URL ends a sentence,
#   is that last period part of the path or just punctuation? The regex can't know. Same as I tell folks about
#   a lot of things.
#
# ANNOUNCER: Judges are conferring... both answers accepted!
#
# ----------------------------------------------------------------------------------------------------------------------
# ANNOUNCER: Final question. What is a raw string in Python, and why do regular expressions use the r in front?
#
# WILLIE: *puts on his reading glasses* A raw string is a string with an r in front of it, like r'\d+'. It tells
#   Python, "Leave my backslashes alone." Normally Python treats a backslash as the start of an escape sequence:
#   '\n' is a newline, '\t' is a tab. In a raw string, '\n' is just two characters: a backslash and an n.
#
# SNOOP: And that matters 'cause regex is FULL of backslashes, ya dig? Peep this:
#
#     '\b'   in a normal string is the backspace character. Python eats it before the regex ever sees it.
#     r'\b'  in a raw string is backslash-b, which the regex engine reads as a word boundary. That's what you wanted.
#
#   Without the r, you'd have to double up every backslash: '\\d{3}-\\d{4}'. That's messy. Keep it raw, keep it real.
#   One catch: a raw string can't end in a single backslash. r'oops\' is a syntax error.
#
# ANNOUNCER: And that's the round! Both contestants answered every question correctly, which means...
#
# WILLIE: It's a tie.
#
# SNOOP: *passes the joint* Same time next chapter, Unc?
#
# WILLIE: On the road again, nephew. On the road again.
#
# ======================================================================================================================

import re

# Let's put the contestants' patterns to the test.
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
address_pattern = r'\b\d+\s+(?:[A-Z][a-z]*\s+)*[A-Z][a-z]*\s+(?:ST|AVE)\b\.?'
name_pattern = r'\b(?:Mr|Mrs|Ms|Miss|Dr|Prof)\.?(?:\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*)+'
url_pattern = (r'\bhttps?://'
               r'(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}'
               r'(?::\d{1,5})?'
               r'(?:/[^\s?#]*)?'
               r'(?:\?[^\s#]*)?'
               r'(?:#[\w-]*)?')

text = ('Call Mr. Willie Hugh Nelson at 512-555-0420 or visit him at 1234 Ocean AVE. '
        'Mrs. Mary Smith-Jones lives at 21 Martin Luther King ST and her number is 310-555-1994. '
        'Dr Calvin Cordozar Broadus has a site at https://www.snoopdogg.com/music?track=gin-and-juice#chorus.')

print('Phone numbers:', re.findall(phone_pattern, text))
print('Addresses:    ', re.findall(address_pattern, text))
print('Names:        ', re.findall(name_pattern, text))
print('URLs:         ', re.findall(url_pattern, text))

# Raw strings vs. regular strings
print(len('\b'), len(r'\b'))  # 1 2


# Exercise 8.12.2
def head(source_file, num_lines, output_file):
    reader = open(source_file)
    if output_file:
        writer = open(output_file, 'w')
        for line in reader:
            if num_lines == 0:
                return
            writer.write(line)
            num_lines -= 1
    else:
        for line in reader:
            if num_lines == 0:
                return
            print(line)
            num_lines -= 1

#head('test.txt', 3, '')
#head('test.txt', 3, 'test2.txt')

# Exercise 8.12.3

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_none(word, forbidden):
    for letter in word.upper():
        for position in forbidden.upper():
            if letter == position:
                return False
    return True

def check_word(word):
    word = word.lower()
    if len(word) != 5:
        return False
    if not uses_none(word, "spadclrk"):
        return False
    if not uses_any(word, "e"):
        return False
    return re.fullmatch(r'..[^e][^e][^e]', word) is not None

count = 0
for line in open('words.txt'):
    if check_word(line.strip()):
        count += 1
print(f"Possible words: {count}")
# 8.12.3 Answer - 90
# 8.12.4 Answer - 54

# Exercise 8.12.5

def check_for_paleness(line):
    if re.match(r'.*pale\w|pallor.*', line):
        return True
    return False

count = 0
for line in open("TheCountOfMonteCristo.txt"):
    if check_for_paleness(line):
        count += 1

print(f"There are {count} lines that contain some form of pale")