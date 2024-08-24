import sys, time, random

typing_speed = 120
def print_slow(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(.03)
    print('')


def dice(max):
    if max == 20:
        d20 = random.randint(1, 20)
        return d20
    elif max == 12:
        d12 = random.randint(1, 12)
        return d12
    elif max == 10:
        d10 = random.randint(1, 10)
        return d10
    elif max == 8:
        d8 = random.randint(1, 8)
        return d8
    elif max == 6:
        d6 = random.randint(1, 6)
        return d6
    elif max == 4:
        d4 = random.randint(1, 4)
        return d4
    else:
        print(f"Error: invalid dice value")
    