
from collections import deque

def get_ans(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return []

    queue = deque()
    queue.append((beginWord, [beginWord]))  # word, path

    while queue:
        current_word, path = queue.popleft()

        if current_word == endWord:
            return path

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)  # avoid revisiting
                    queue.append((next_word, path + [next_word]))

    return []


start = "hit"
end = "dot"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

ans=get_ans(start, end, wordList)
print(ans)
