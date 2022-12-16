import art, game_data
from random import choice

person_a = choice(game_data.data)
person_b = choice(game_data.data)
game_over = False
score = 0

def person_selection(current_person):
    """Swap the current person to a different person on the list."""
    new_person = choice(game_data.data)
    while new_person == current_person:
        new_person = choice(game_data.data)
    return new_person

def score_calculator(answer, other_option):
    """Check if user score a point and returns 1 point"""
    if answer > other_option:
        return 1
    else:
        return 0
    
while not game_over:
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
    person_selected = input("\nbWho has more Followers? Type 'A' or 'B': ").lower()
    
    if person_selected == "a":
        compare_to = person_b['follower_count']
        answer = person_a['follower_count']
    else:
        compare_to = person_a['follower_count']
        answer = person_b['follower_count']
    old_score = score    
    score += score_calculator(answer, compare_to)
    if score > old_score:
        person_a = person_b
        person_b = person_selection(person_b)
    else:
        game_over = True

print(f"Sorry, that's wrong. Final score: {score}")