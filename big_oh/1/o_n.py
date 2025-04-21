# O(N)
football_teams = ["Liverpool FC", "FC Inter Milan", "FC Bayern Munich", "Real Madrid CF", "Mamelodi Sundowns FC"]
for team in football_teams:
    print(f"{team} is a championship winning team!!!")

# is prime?
def is_prime(number:int) -> bool:
    """Check if number is a prime"""
    for value in range(2, number):
        if number % value == 0:
            return False
    return True