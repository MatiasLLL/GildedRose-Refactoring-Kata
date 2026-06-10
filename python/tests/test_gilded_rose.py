import unittest

from gilded_rose import GildedRose, Item

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


class GildedRoseTest(unittest.TestCase):
    def update(self, name, sell_in, quality):
        item = Item(name, sell_in, quality)
        GildedRose([item]).update_quality()
        return item

    # Normal items

    def test_normal_item_degrades_by_one_before_sell_date(self):
        item = self.update("Normal item", sell_in=5, quality=10)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(9, item.quality)

    def test_normal_item_degrades_twice_as_fast_after_sell_date(self):
        item = self.update("Normal item", sell_in=0, quality=10)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(8, item.quality)

    def test_normal_item_quality_is_never_negative(self):
        item = self.update("Normal item", sell_in=5, quality=0)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_normal_item_quality_stops_at_zero_after_sell_date(self):
        item = self.update("Normal item", sell_in=0, quality=1)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    # Aged Brie

    def test_aged_brie_increases_in_quality(self):
        item = self.update(AGED_BRIE, sell_in=5, quality=10)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(11, item.quality)

    def test_aged_brie_increases_twice_as_fast_after_sell_date(self):
        item = self.update(AGED_BRIE, sell_in=0, quality=10)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(12, item.quality)

    def test_aged_brie_quality_never_exceeds_fifty(self):
        item = self.update(AGED_BRIE, sell_in=5, quality=50)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_aged_brie_quality_caps_at_fifty_after_sell_date(self):
        item = self.update(AGED_BRIE, sell_in=0, quality=49)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)

    # Sulfuras

    def test_sulfuras_never_changes(self):
        item = self.update(SULFURAS, sell_in=5, quality=80)
        self.assertEqual(5, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_sulfuras_never_changes_even_after_sell_date(self):
        item = self.update(SULFURAS, sell_in=-1, quality=80)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(80, item.quality)

    # Backstage passes

    def test_backstage_increases_by_one_when_concert_is_far_away(self):
        item = self.update(BACKSTAGE, sell_in=15, quality=10)
        self.assertEqual(14, item.sell_in)
        self.assertEqual(11, item.quality)

    def test_backstage_increases_by_one_at_eleven_days(self):
        item = self.update(BACKSTAGE, sell_in=11, quality=10)
        self.assertEqual(10, item.sell_in)
        self.assertEqual(11, item.quality)

    def test_backstage_increases_by_two_at_ten_days(self):
        item = self.update(BACKSTAGE, sell_in=10, quality=10)
        self.assertEqual(9, item.sell_in)
        self.assertEqual(12, item.quality)

    def test_backstage_increases_by_two_at_six_days(self):
        item = self.update(BACKSTAGE, sell_in=6, quality=10)
        self.assertEqual(5, item.sell_in)
        self.assertEqual(12, item.quality)

    def test_backstage_increases_by_three_at_five_days(self):
        item = self.update(BACKSTAGE, sell_in=5, quality=10)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(13, item.quality)

    def test_backstage_increases_by_three_on_last_day(self):
        item = self.update(BACKSTAGE, sell_in=1, quality=10)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(13, item.quality)

    def test_backstage_quality_drops_to_zero_after_concert(self):
        item = self.update(BACKSTAGE, sell_in=0, quality=10)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_backstage_quality_never_exceeds_fifty(self):
        item = self.update(BACKSTAGE, sell_in=5, quality=49)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)

    # Conjured items

    def test_conjured_item_degrades_twice_as_fast(self):
        item = self.update("Conjured Mana Cake", sell_in=5, quality=10)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(8, item.quality)

    def test_conjured_item_degrades_four_times_as_fast_after_sell_date(self):
        item = self.update("Conjured Mana Cake", sell_in=0, quality=10)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(6, item.quality)

    def test_conjured_item_quality_is_never_negative(self):
        item = self.update("Conjured Mana Cake", sell_in=5, quality=1)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(0, item.quality)


if __name__ == "__main__":
    unittest.main()
