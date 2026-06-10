from __future__ import annotations

from typing import Final, Protocol

AGED_BRIE: Final = "Aged Brie"
SULFURAS: Final = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS: Final = "Backstage passes to a TAFKAL80ETC concert"
CONJURED_PREFIX: Final = "Conjured"

MIN_QUALITY: Final = 0
MAX_QUALITY: Final = 50


class GildedRose:
    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            updater_for(item).update(item)


class ItemUpdater(Protocol):
    def update(self, item: Item) -> None: ...


class NormalItemUpdater:
    degradation_rate = 1

    def update(self, item: Item) -> None:
        decrease_quality(item, self.degradation_rate)
        item.sell_in -= 1
        if item.sell_in < 0:
            decrease_quality(item, self.degradation_rate)


class AgedBrieUpdater:
    def update(self, item: Item) -> None:
        increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            increase_quality(item)


class SulfurasUpdater:
    def update(self, item: Item) -> None:
        pass


class BackstagePassUpdater:
    def update(self, item: Item) -> None:
        if item.sell_in <= 5:
            increase_quality(item, 3)
        elif item.sell_in <= 10:
            increase_quality(item, 2)
        else:
            increase_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class ConjuredItemUpdater(NormalItemUpdater):
    degradation_rate = 2


UPDATERS_BY_NAME: Final[dict[str, ItemUpdater]] = {
    AGED_BRIE: AgedBrieUpdater(),
    SULFURAS: SulfurasUpdater(),
    BACKSTAGE_PASS: BackstagePassUpdater(),
}
DEFAULT_UPDATER: Final[ItemUpdater] = NormalItemUpdater()
CONJURED_UPDATER: Final[ItemUpdater] = ConjuredItemUpdater()


def updater_for(item: Item) -> ItemUpdater:
    if item.name.startswith(CONJURED_PREFIX):
        return CONJURED_UPDATER
    return UPDATERS_BY_NAME.get(item.name, DEFAULT_UPDATER)


def increase_quality(item: Item, amount: int = 1) -> None:
    item.quality = min(MAX_QUALITY, item.quality + amount)


def decrease_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(MIN_QUALITY, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
