# В большой текстовой строке подсчитать количество встречаемых слов,
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку

import collections

wiki_text = "In computer science, binary search, also known as half-interval search,[1] logarithmic search," \
            "[2] or binary chop,[3] is a search algorithm that finds the position of a target value within" \
            " a sorted array.[4][5] Binary search compares the target value to the middle element of the array." \
            " If they are not equal, the half in which the target cannot lie is eliminated and the search" \
            " continues on the remaining half, again taking the middle element to compare to the target value," \
            " and repeating this until the target value is found. If the search ends with the remaining half" \
            " being empty, the target is not in the array." \
            "Binary search runs in logarithmic time in the worst case, making O(log n) comparisons, where " \
            "n is the number of elements in the array.[a][6] Binary search is faster than linear search except " \
            "for small arrays. However, the array must be sorted first to be able to apply binary search. " \
            "There are specialized data structures designed for fast searching, such as hash tables, that can be" \
            " searched more efficiently than binary search. However, binary search can be used to solve a wider " \
            "range of problems, such as finding the next-smallest or next-largest element in the array relative " \
            "to the target even if it is absent from the array."


def most_frqnt_words(text: str) -> list[tuple[int, str]]:
    unique_words = []
    count = []
    word_list = text.replace(",", "").lower().split(" ")

    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    for unique_word in unique_words:
        cnt = 0
        for word in word_list:
            if word == unique_word:
                cnt += 1
        count.append((cnt, unique_word))

    count.sort(reverse=True)

    return count[:10]


print(f'Вариант 1 -> {most_frqnt_words(wiki_text)}', '\n')

print(f'Вариант 2 -> {collections.Counter(wiki_text.replace(",", "").split(" ")).most_common(10)}')
