from collections import defaultdict
import pygame
import pytest
from unittest.mock import patch

from src.pacman import Pacman
from src.settings import PACMAN_SPEED


@pytest.fixture(autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


@patch('pygame.image.load')
def test_pacman_initialization(mock_load):
    mock_image = pygame.Surface((10, 10))
    mock_load.return_value = mock_image

    pacman = Pacman(row=1, col=2, size=32)

    assert pacman.size == 32
    assert pacman.rect.topleft == (32, 64)
    assert pacman.life == 3
    assert pacman.image is not None
    assert len(pacman.frames) == 4


@patch('pygame.image.load')
def test_pacman_move_right_without_collision(mock_load):
    mock_image = pygame.Surface((10, 10))
    mock_load.return_value = mock_image
    pacman = Pacman(0, 0, 32)

    keys = defaultdict(lambda: False)
    keys[pygame.K_RIGHT] = True

    start_pos = pacman.rect.topleft
    pacman.move(keys, [])
    end_pos = pacman.rect.topleft

    assert end_pos[0] > start_pos[0]
    assert end_pos[1] == start_pos[1]


@patch('pygame.image.load')
def test_pacman_move_collision(mock_load):
    mock_image = pygame.Surface((10, 10))
    mock_load.return_value = mock_image
    pacman = Pacman(0, 0, 32)

    keys = defaultdict(lambda: False)
    keys[pygame.K_RIGHT] = True

    wall = pygame.Rect(
        pacman.rect.x + PACMAN_SPEED,
        pacman.rect.y,
        pacman.rect.width,
        pacman.rect.height
    )
    start_pos = pacman.rect.topleft
    pacman.move(keys, [wall])
    end_pos = pacman.rect.topleft

    assert end_pos == start_pos


@patch('pygame.image.load')
def test_pacman_reset_position(mock_load):
    mock_image = pygame.Surface((10, 10))
    mock_load.return_value = mock_image
    pacman = Pacman(1, 2, 32)

    pacman.rect.topleft = (100, 100)
    pacman.reset_position()

    assert pacman.rect.topleft == (pacman.start_x, pacman.start_y)
    assert pacman.frame_index == 0
