# 5. Write a simple quote-of-the-day program. The program should contain a list of
# quotes, and when the user runs the program, a randomly selected quote should be
# printed.

quotes = [
    '"What we think, we become." - Buddha',
    '"Absorb what is useful. Discard what is not. Add what is uniquely your own." - Bruce Lee',
    '"The only journey is the journey within." - Rainer Maria Rilke',
    '"They must often change who would be constant in happiness or wisdom." - Confucius',
    '"We must become the change we want to see." - Mahatma Gandhi',
    '"We are what we repeatedly do. Excellence, then, is not an act but a habit." - Will Durant'

]
while True:
    try:
        pick_quote = int(input("Pick a number between 0-5 (for a random quote): "))
        break
    except ValueError:
        print("Error, Please input an integer.")

print(quotes[pick_quote])