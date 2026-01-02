import pytest
from rps.main import GameResult, GameAction, assess_game


@pytest.mark.draw
def test_draw():
    assert GameResult.Tie == assess_game(GameAction.Spock, GameAction.Spock)
    assert GameResult.Tie == assess_game(GameAction.Lizard, GameAction.Lizard)
    assert GameResult.Tie == assess_game(GameAction.Rock, GameAction.Rock)
    assert GameResult.Tie == assess_game(GameAction.Scissors, GameAction.Scissors)
    assert GameResult.Tie == assess_game(GameAction.Paper, GameAction.Paper)


@pytest.mark.spock
def test_spock_loses():
    # Spock pierde con Lizard y Paper
    assert GameResult.Victory == assess_game(GameAction.Paper, GameAction.Spock)
    assert GameResult.Victory == assess_game(GameAction.Lizard, GameAction.Spock)

@pytest.mark.spock
def test_spock_wins():
    # Spock gana a Rock y Scissors
    assert GameResult.Defeat == assess_game(GameAction.Rock, GameAction.Spock)
    assert GameResult.Defeat == assess_game(GameAction.Scissors, GameAction.Spock)


@pytest.mark.lizard
def test_lizard_loses():
    # Lizard pierde con Rock y Scissors
    assert GameResult.Victory == assess_game(GameAction.Rock, GameAction.Lizard)
    assert GameResult.Victory == assess_game(GameAction.Scissors, GameAction.Lizard)

@pytest.mark.lizard
def test_lizard_wins():
    # Lizard gana a Spock y Paper
    assert GameResult.Defeat == assess_game(GameAction.Spock, GameAction.Lizard)
    assert GameResult.Defeat == assess_game(GameAction.Paper, GameAction.Lizard)


@pytest.mark.rock
def test_rock_loses():
    # Rock pierde con Spock y Paper
    assert GameResult.Victory == assess_game(GameAction.Spock, GameAction.Rock)
    assert GameResult.Victory == assess_game(GameAction.Paper, GameAction.Rock)

@pytest.mark.rock
def test_rock_wins():
    # Rock gana a Scissors y Lizard
    assert GameResult.Defeat == assess_game(GameAction.Scissors, GameAction.Rock)
    assert GameResult.Defeat == assess_game(GameAction.Lizard, GameAction.Rock)


@pytest.mark.paper
def test_paper_loses():
    # Paper pierde con Scissors y Lizard
    assert GameResult.Victory == assess_game(GameAction.Scissors, GameAction.Paper)
    assert GameResult.Victory == assess_game(GameAction.Lizard, GameAction.Paper)

@pytest.mark.paper
def test_paper_wins():
    # Paper gana a Rock y Spock
    assert GameResult.Defeat == assess_game(GameAction.Rock, GameAction.Paper)
    assert GameResult.Defeat == assess_game(GameAction.Spock, GameAction.Paper)


@pytest.mark.scissors
def test_scissors_loses():
    # Scissors pierde con Spock y Rock
    assert GameResult.Victory == assess_game(GameAction.Spock, GameAction.Scissors)
    assert GameResult.Victory == assess_game(GameAction.Rock, GameAction.Scissors)

@pytest.mark.scissors
def test_scissors_wins():
    # Scissors gana a Lizard y Paper
    assert GameResult.Defeat == assess_game(GameAction.Lizard, GameAction.Scissors)
    assert GameResult.Defeat == assess_game(GameAction.Paper, GameAction.Scissors)
