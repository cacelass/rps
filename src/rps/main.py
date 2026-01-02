import random
from enum import IntEnum

memoria = []

class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

# Tabla de victorias: qué le gana a qué
Victories = {
    GameAction.Rock:     [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper:    [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard:   [GameAction.Spock, GameAction.Paper],
    GameAction.Spock:    [GameAction.Scissors, GameAction.Rock]
}

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    elif computer_action in Victories[user_action]:
        print(f"{user_action.name} beats {computer_action.name}. You won!")
        return GameResult.Victory
    else:
        print(f"{computer_action.name} beats {user_action.name}. You lost!")
        return GameResult.Defeat

def get_computer_action():
    def frequency_analysis():
        counts = [memoria.count(i) for i in range(len(GameAction))]
        total = sum(counts)
        percentages = [c / total for c in counts]
        max_percentage = max(percentages)

        if max_percentage >= 0.40:
            most_common_index = percentages.index(max_percentage)
            # Elige aleatoriamente una acción que gane a la más frecuente
            winning_options = [k for k, v in Victories.items() if GameAction(most_common_index) in v]
            return random.choice(winning_options)
        else:
            return random.randint(0, len(GameAction) - 1)

    if len(memoria) > 5:
        computer_selection = frequency_analysis()
    else:
        computer_selection = random.randint(0, len(GameAction) - 1)

    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action

def get_user_action():
    game_choices = [f"{ga.name}[{ga.value}]" for ga in GameAction]
    game_choices_str = ", ".join(game_choices)
    while True:
        try:
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            user_action = GameAction(user_selection)
            return user_action
        except (ValueError, KeyError):
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")

def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'

def main():
    while True:
        user_action = get_user_action()
        memoria.append(user_action.value)
        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break

if __name__ == "__main__":
    main()
