# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.updateItem(item)

    def updateItem(self, item):
        if self.isImprovingOverTime(item):
            self.updateImprovingItem(item)
        elif self.isImprovingUntilEvent(item):
            self.updateImprovingUntilEvent(item)
        elif self.isLegendary(item):
            self.updateLegendaryItem(item)
        elif self.isConjured(item):
            self.updateConjuredItem(item)
        else:
            self.updateNormalItem(item)

    def updateNormalItem(self, item):
        if self.stillHasQuality(item):
            self.decreaseQualityByOne(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item) and self.stillHasQuality(item):
            self.decreaseQualityByOne(item)

    def updateLegendaryItem(self, _item):
        pass

    def updateImprovingUntilEvent(self, item):
        if self.qualityNotMaxed(item):
            self.inscreaseQualityByOne(item)
            if item.sell_in < 11 and self.qualityNotMaxed(item):
                self.inscreaseQualityByOne(item)
            if item.sell_in < 6 and self.qualityNotMaxed(item):
                self.inscreaseQualityByOne(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item):
            item.quality = 0

    def updateImprovingItem(self, item):
        if self.qualityNotMaxed(item):
            self.inscreaseQualityByOne(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item) and self.qualityNotMaxed(item):
            self.inscreaseQualityByOne(item)

    def updateConjuredItem(self, item):
        if self.stillHasQuality(item):
            self.decreaseQualityByOne(item)
        if self.stillHasQuality(item):
            self.decreaseQualityByOne(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item) and self.stillHasQuality(item):
            self.decreaseQualityByOne(item)
            if self.stillHasQuality(item):
                self.decreaseQualityByOne(item)
                

    def decreaseSellinByOne(self, item):
        item.sell_in = item.sell_in - 1

    def isImprovingUntilEvent(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def inscreaseQualityByOne(self, item):
        item.quality = item.quality + 1

    def qualityNotMaxed(self, item):
        return item.quality < 50

    def afterSellin(self, item):
        return item.sell_in < 0

    def decreaseQualityByOne(self, item):
        item.quality = item.quality - 1

    def isLegendary(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def isConjured(self, item):
        return item.name.startswith("Conjured")

    def stillHasQuality(self, item):
        return item.quality > 0

    def isImprovingOverTime(self, item):
        return item.name == "Aged Brie"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
