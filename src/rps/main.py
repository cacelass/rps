import random
from enum import IntEnum
from typing import List

# Historial de jugadas del usuario
memoria: List[int] = []

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

def assess_game(user_action: GameAction, computer_action: GameAction) -> GameResult:
    """Determina el resultado del juego entre usuario y computadora."""
    if not isinstance(user_action, GameAction):
        raise TypeError(f"user_action debe ser GameAction, no {type(user_action).__name__}")
    if not isinstance(computer_action, GameAction):
        raise TypeError(f"computer_action debe ser GameAction, no {type(computer_action).__name__}")

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    elif computer_action in Victories[user_action]:
        print(f"{user_action.name} beats {computer_action.name}. You won!")
        return GameResult.Victory
    else:
        print(f"{computer_action.name} beats {user_action.name}. You lost!")
        return GameResult.Defeat

def get_computer_action() -> GameAction:
    """Selecciona la acción de la computadora según frecuencia o aleatoria."""
    def frequency_analysis() -> int:
        counts = [memoria.count(i) for i in range(len(GameAction))]
        total = sum(counts)
        percentages = [c / total for c in counts]
        max_percentage = max(percentages)

        if max_percentage >= 0.40:
            most_common_index = percentages.index(max_percentage)
            winning_options = [k for k, v in Victories.items() if GameAction(most_common_index) in v]
            return random.choice(winning_options)
        else:
            return random.randint(0, len(GameAction) - 1)

    if len(memoria) > 5:
        computer_selection: int = frequency_analysis()
    else:
        computer_selection: int = random.randint(0, len(GameAction) - 1)

    computer_action: GameAction = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action

def get_user_action() -> GameAction:
    """Solicita la acción del usuario y valida el tipo de entrada."""
    game_choices = [f"{ga.name}[{ga.value}]" for ga in GameAction]
    game_choices_str = ", ".join(game_choices)
    while True:
        try:
            user_selection: int = int(input(f"\nPick a choice ({game_choices_str}): "))
            user_action: GameAction = GameAction(user_selection)
            return user_action
        except (ValueError, KeyError):
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")

def play_another_round() -> bool:
    """Pregunta al usuario si desea jugar otra ronda."""
    another_round: str = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'

def main() -> None:
    """Ejecuta el flujo principal del juego."""
    while True:
        user_action: GameAction = get_user_action()
        memoria.append(user_action.value)
        computer_action: GameAction = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break

if __name__ == "__main__":
    main()
    """Juego de Piedra, Papel, Tijeras, Lagarto, Spock entre usuario y computadora."""