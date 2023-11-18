"""Здесь надо написать тесты с использованием pytest для модуля item."""
from typing import Any

import pytest

from src.item import Item


@pytest.fixture
def test_item() -> Any:
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_item) -> Any:
    assert test_item.calculate_total_price() == 200000


def test_apply_discount(test_item) -> Any:
    Item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 8000.0
