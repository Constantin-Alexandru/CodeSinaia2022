###
# Class owning the set of hints given in the course
# of playing one game of Wordle
class WordChecker:

    ###
    # Class constructor:

    letters = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, words):
        self.valid_words = words
        self.must_letters = []
        self.must_pos = [[0 for _ in range(5)] for _ in range(26)]
        self.possible_pos = [[1 for _ in range(5)] for _ in range(26)]
        self.hints = []

    def let_ord(self, ch) -> int:
        return ord(ch) - ord('a')

    def order_list(self):

        dict_letters = dict()

        for ch in self.must_letters:
            if ch not in dict_letters:
                dict_letters[ch] = 1
            else:
                dict_letters[ch] += 1

        for i in range(5):
            self.valid_words = [x for x in self.valid_words if
                                self.must_pos[self.let_ord(x[i])][i] == 1 or self.possible_pos[self.let_ord(x[i])][i]]
            self.valid_words = [x for x in self.valid_words if all(
                [ch in x for ch in self.must_letters])]

        toRemove = []

        for word in self.valid_words:
            letter_count = dict()
            for i in range(5):
                if word[i] not in letter_count:
                    letter_count[word[i]] = 1
                else:
                    letter_count[word[i]] += 1

            for ch in word:
                if ch in dict_letters:
                    if dict_letters[ch] > letter_count[ch]:
                        toRemove.append(word)

        for word in toRemove:
            if word in self.valid_words:
                self.valid_words.remove(word)

        letter_count = []

        for i in range(5):
            letter_count_pos = [0 for _ in range(26)]
            for word in self.valid_words:
                letter_count_pos[self.let_ord(word[i])] += 1

            letter_count.append(letter_count_pos)

        scores = []

        for i in self.valid_words:
            score = 1

            unique = []

            for j in range(5):
                score *= letter_count[j][self.let_ord(i[j])]
                if i[j] not in unique:
                    unique.append(i[j])

            score *= len(unique)
            scores.append(score)

        for i in range(len(scores) - 1):

            for j in range(i + 1, len(scores)):
                if scores[i] < scores[j]:
                    self.valid_words[i], self.valid_words[j] = self.valid_words[j], self.valid_words[i]
                    scores[i], scores[j] = scores[j], scores[i]

    def check(self, word):
        green = False
        yellow = False
        matches_found = 0
        self.hints = []
        for i in range(len(word)):
            ch = word[i]

            if green:
                green = False
                self.must_pos[self.let_ord(ch)][i - matches_found] = 1
                if ch not in self.must_letters:
                    self.must_letters.append(ch)
                for j in range(26):
                    if j != self.let_ord(ch):
                        self.possible_pos[j][i - matches_found] = 0
                self.hints.append(ch)
            elif yellow:
                self.possible_pos[self.let_ord(ch)][i - matches_found] = 0
                if ch not in self.must_letters:
                    self.must_letters.append(ch)
                self.hints.append(ch)
                yellow = False
            elif ch == "+":
                green = True
                matches_found += 1
            elif ch == "~":
                yellow = True
                matches_found += 1
            else:
                if ch not in self.must_letters:
                    for j in range(5):
                        self.possible_pos[self.let_ord(ch)][j] = 0
                else:
                    self.possible_pos[self.let_ord(ch)][i - matches_found] = 0

        unique = []

        for ch in self.hints:
            if ch not in unique:
                unique.append(ch)

        for ch in unique:
            if self.hints.count(ch) > 1:
                while self.must_letters.count(ch) < self.hints.count(ch):
                    self.must_letters.append(ch)

        self.order_list()
        return self.valid_words

    ###
    # Returns a string representation of the entire object

    def __str__(self):
        return f"TODO: WordChecker internal state."
