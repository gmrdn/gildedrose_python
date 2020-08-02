# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_sellin_decreases_each_day(self) :
        items = [Item("Spatule", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)

    def test_quality_decreases_each_day(self) :
        items = [Item("Spatule", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_quality_degrades_twice_as_fast_after_sellin(self) :
        items = [Item("Spatule", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1) 
        self.assertEqual(items[0].quality, 18)

    def test_quality_is_never_negative(self) :
        items = [Item("Spatule", 1, 1), Item("Fourchette", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)


    def test_aged_brie_increases_quality(self) :
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21) 

    def test_quality_is_never_over_50(self) : 
        items = [Item("Aged Brie", 1, 49), Item("Aged Brie", 0, 49)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[1].quality, 50)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[1].quality, 50)

    def test_legendary_item_never_lose_quality(self) :
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes_increase_quality_up_to_sellin_date(self) :
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() # sellin 10
        self.assertEqual(items[0].quality, 2)
        gilded_rose.update_quality() # sellin 9
        self.assertEqual(items[0].quality, 4)
        gilded_rose.update_quality() # sellin 8
        gilded_rose.update_quality() # 7
        gilded_rose.update_quality() # 6
        self.assertEqual(items[0].quality, 10)
        gilded_rose.update_quality() # sellin 5
        self.assertEqual(items[0].quality, 12)
        gilded_rose.update_quality() # sellin 4
        gilded_rose.update_quality() # 3
        gilded_rose.update_quality() # 2
        gilded_rose.update_quality() # 1
        self.assertEqual(items[0].quality, 24)
        gilded_rose.update_quality() # sellin 0
        self.assertEqual(items[0].quality, 27)
        gilded_rose.update_quality() # sellin -1
        self.assertEqual(items[0].quality, 0)

    def test_conjured_items_degrade_quality_twice_as_fast(self) :
        items = [Item("Conjured Spoon", 2, 23)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21) 
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 15) 
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3) 
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0) 


if __name__ == '__main__':
    unittest.main()
