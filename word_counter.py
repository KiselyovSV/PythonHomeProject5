print("Word_counter start")
str = input("Для подсчёта слов введите текст: \n").lower()
punc_list = {"'", ".", ";", ":", "!", "?", "/", ",", "#", "@", "$", "&" }
for i in punc_list:
    str = str.replace(i, " ")
words = dict()
for i in str.split():
    if i in words.keys():
        words[i] += 1
    else:
        words[i] = 1
for key, value in words.items():
    print(f"{key} - {value}")
