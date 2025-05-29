import pytest
import pygame
from unittest.mock import Mock, patch
from src.tile import Tile


@pytest.fixture(autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_tile_initialization():
    tile = Tile(row=1, col=2, size=32, color=(255, 0, 0))
    assert tile.size == 32
    assert tile.x == 32  # 1 * 32
    assert tile.y == 64  # 2 * 32
    assert tile.color == (255, 0, 0)
    assert isinstance(tile.rect, pygame.Rect)
    assert tile.rect.topleft == (tile.x, tile.y)


def test_tile_update_color():
    tile = Tile(0, 0, 10, (0, 0, 0))
    tile.update_color((100, 100, 100))
    assert tile.color == (100, 100, 100)


@patch('pygame.draw.rect')
def test_tile_draw(mock_draw):
    screen = Mock()
    tile = Tile(0, 0, 10, (123, 234, 111))
    tile.draw(screen)
    mock_draw.assert_called_once_with(screen, tile.color, tile.rect)
