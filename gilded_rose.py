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
            self.updateImprovingUntilExpiration(item)
        elif self.isLegendary(item):
            self.updateLegendaryItem(item)
        elif self.isConjured(item):
            self.updateConjuredItem(item)
        else:
            self.updateNormalItem(item)

    def updateNormalItem(self, item):
        self.decreaseQualityByNbUntilZero(item, 1)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item):
            self.decreaseQualityByNbUntilZero(item, 1)

    def updateLegendaryItem(self, _item):
        pass

    def updateImprovingUntilExpiration(self, item):
        self.increaseQualityByOneUntilMax(item)
        if item.sell_in < 11:
            self.increaseQualityByOneUntilMax(item)
        if item.sell_in < 6:
            self.increaseQualityByOneUntilMax(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item):
            self.expire(item)


    def isLegendary(self, item):
        return item.name in ["Sulfuras, Hand of Ragnaros"]

    def isConjured(self, item):
        return item.name.startswith("Conjured")

    def isImprovingUntilEvent(self, item):
        return item.name.startswith("Backstage passes")

    def isImprovingOverTime(self, item):
        return item.name in ["Aged Brie"]

    def expire(self, item):
        item.quality = 0

    def updateImprovingItem(self, item):
        self.increaseQualityByOneUntilMax(item)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item):
            self.increaseQualityByOneUntilMax(item)

    def updateConjuredItem(self, item):
        self.decreaseQualityByNbUntilZero(item, 2)
        self.decreaseSellinByOne(item)
        if self.afterSellin(item):
            self.decreaseQualityByNbUntilZero(item, 2)
                
    def decreaseSellinByOne(self, item):
        item.sell_in = item.sell_in - 1

    def qualityNotMaxed(self, item):
        return item.quality < 50

    def stillHasQuality(self, item):
        return item.quality > 0

    def afterSellin(self, item):
        return item.sell_in < 0

    def decreaseQualityByNbUntilZero(self, item, nb):
        for _i in range(nb):
            if self.stillHasQuality(item):
                item.quality = item.quality - 1

    def increaseQualityByOneUntilMax(self, item):
        if self.qualityNotMaxed(item):
            item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
