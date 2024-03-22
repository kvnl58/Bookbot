
def countChars (s):
    counts = {}
    lower = s.lower()

    for char in lower:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def countWords(s):
    words = s.split()
    count = 0
    count += len(words)
    return count

def sort_on(dict):
    return dict["char"]

def printReport(wordCount, charCounts):
    print("-- Begin report of books/frankenstein.txt")
    print(f"{wordCount} words found in the document")
    charCountsList = []
    for char in charCounts:
        if char.isalpha():
            charCountsList.append({"char": char, "count": charCounts[char]})
    charCountsList.sort(key=sort_on)
    for charDict in charCountsList:
        print(f"The '{charDict['char']}' character was found {charDict['count']} times")

def main():
    path = "./books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        wordsCount = countWords(file_contents)
        charsCount = countChars(file_contents)
        printReport(wordsCount, charsCount)
        
main()
