import random
import game_data
import art


def pick():
    random_item = random.randint(0, 49)
    list_item = game_data.data[random_item]
    return list_item


def compare(choice_a, choice_b):
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"


def check_answer(user, actual):
    if user == actual:
        return True
    else:
        return False


print(art.logo)
score = 0
a = pick()
b = pick()
continue_playing = True
while continue_playing:
    a = b
    b = pick()
    if b == a:
        b = pick()

    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
    print(art.vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')
    answer = compare(a, b)
    guess = input("\nPlease guess A or B\n")
    if check_answer(guess, answer):
        score += 1
        print(f"\nThat's right! Score: {score}\n")
    else:
        print(f"\nGAME OVER!\nFinal score: {score}")
        continue_playing = False
