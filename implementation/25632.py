def sieve(num):
    is_prime = [True for _ in range(num+1)]
    is_prime[1] = False
    
    for i in range(2, num+1):
        if not is_prime[i]:
            continue
        for j in range(2*i, num+1, i):
            is_prime[j] = False

    return is_prime

def get_primes(sieve, num_a, num_b):
    return set(num for num in range(num_a, num_b+1) if sieve[num])

class decks:
    def __init__(self, name, my_deck):
        self.opps_name = name
        self.my_deck = my_deck
    
    def __call__(self, opponent):
        if not self.my_deck:
            return self.opps_name
        
        intersect = opponent.my_deck & self.my_deck
        
        if intersect:
            to_remove = intersect.pop()
            opponent.remove_from_deck(to_remove)
            self.remove_from_deck(to_remove)
        else:
            self.my_deck.pop()

    def remove_from_deck(self, prime):
        self.my_deck.remove(prime)

def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    primes = sieve(max([a, b, c, d]))
    yt = decks("yj", get_primes(primes, a, b))
    yj = decks("yt", get_primes(primes, c, d))

    out = ""
    while not out:
        out = yt(yj)
        if not out:
            out = yj(yt)
        if out:
            print(out)

if __name__ == "__main__":
    solve()