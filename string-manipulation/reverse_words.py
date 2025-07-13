""" reverse words in a string """


def reverse_words(s: str):
    words = s.strip().split()
    n = len(words)

    # easy way to reverse the list: words[::-1]
    for i in range(n-2):
        words[i], words[n-i-1] = words[n-i-1], words[i]

    return ' '.join(words)


input_str = "from   kaaviya ok   hello world"
print(input_str)
print(reverse_words(input_str))
