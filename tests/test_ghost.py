import os
import pygame
import pytest
from unittest.mock import patch
from src.ghost import Ghost
from src.settings import WIDTH

os.environ["SDL_VIDEODRIVER"] = "dummy"


@pytest.fixture
def init_pygame():
    pygame.init()
    pygame.display.set_mode((WIDTH, 480))
    yield
    pygame.quit()


@patch('pygame.image.load')
def test_ghost_creation(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(1, 2, 32, 'blinky', level=1)

    assert ghost.rect.x == 1 * 32
    assert ghost.rect.y == 2 * 32
    assert ghost.move_dir == 'up'
    assert ghost.direction == (0, 0)


@patch('pygame.image.load')
def test_move_to_start(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(1, 2, 32, 'blinky', level=1)

    ghost.rect.x = 100
    ghost.rect.y = 200
    ghost.move_to_start()

    assert ghost.rect.x == 32
    assert ghost.rect.y == 64


@patch('pygame.image.load')
def test_is_collide_false(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(1, 2, 32, 'blinky', level=1)

    walls = [pygame.Rect(200, 200, 32, 32)]
    assert ghost.is_collide(0, 0, walls) is False


@patch('pygame.image.load')
def test_is_collide_true(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(1, 2, 32, 'blinky', level=1)

    wall = pygame.Rect(ghost.rect.x, ghost.rect.y, 32, 32)
    assert ghost.is_collide(0, 0, [wall]) is True


@patch('pygame.image.load')
def test_teleportation_left(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(0, 0, 32, 'blinky', level=1)

    ghost.rect.x = WIDTH  # Привид вийшов за праву межу
    ghost.update([], False)

    assert ghost.rect.left == 0


@patch('pygame.image.load')
def test_animate_power_mode(mock_load, init_pygame):
    surface = pygame.Surface((10, 10))
    mock_load.return_value = surface
    ghost = Ghost(0, 0, 32, 'blinky', level=1)

    ghost.animate(True)
    assert ghost.image.get_size() == (32, 32)
    ghost.animate(False)
    assert ghost.image.get_size() == (32, 32)


@patch('pygame.image.load')
def test_update_direction(mock_load, init_pygame):
    mock_load.return_value = pygame.Surface((10, 10))
    ghost = Ghost(0, 0, 32, 'blinky', level=1)

    ghost.directions = {'right': (1, 0)}
    ghost.keys = ['right']
    ghost.direction = (1, 0)

    ghost.update([], False)

    assert ghost.rect.x > 0
