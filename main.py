from funct import *
def main():
    user_s = 0
    print('введите ваше имя пожалуйста')
    name = input()
    print('давайте начнем')
    words = read_f()
    for word in words:
        word_sh = shuffle_words(word)
        print(f'угадайте слво {word_sh}')
        user_inp = input()
        if user_inp==word:
            user_s+=10
            print('верно вы получается 10 очков')
        else:
            print(f'неверно верный отчет это {word}')
    write_record(name, user_s)
    stat = static()
    print(f'всего игр сыграно {stat.get("len")}')
    print(f'рекорд {stat.get("max")}')
main()
