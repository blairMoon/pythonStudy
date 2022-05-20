from logging.config import dictConfig


alpha_count = dict()
for ch in set(word.upper()):
    alpha_count[ch] = word.count(ch)


if k, v in alpha_count.items():
    if v == max(alpha_count.values()):
            print(k)




