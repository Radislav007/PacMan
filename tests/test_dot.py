import pygame
import pytest
from unittest.mock import Mock
from src.dot import Dot


@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_dot_is_created_correctly():
    dot = Dot(1, 2, 10)
    assert isinstance(dot.image, pygame.Surface)
    assert dot.rect.topleft == (1 * 10 + 10 // 2 - dot.rect.width // 2,
                                2 * 10 + 10 // 2 - dot.rect.height // 2)
    assert not dot.is_power


def test_power_dot_color_and_size():
    dot = Dot(0, 0, 20, is_power=True)
    color = dot.image.get_at((10, 10))
    assert color[:3] == (255, 255, 0)
    assert dot.is_power


def test_draw_method():
    screen = Mock(spec=pygame.Surface)
    dot = Dot(0, 0, 10)

    dot.draw(screen)

    screen.blit.assert_called_once_with(dot.image, dot.rect)
