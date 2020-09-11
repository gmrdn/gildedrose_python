# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def update_item(self, item):
        pass

    @staticmethod
    def expire(item):
        item.quality = 0

    @staticmethod
    def decrease_sellin_by_one(item):
        item.sell_in = item.sell_in - 1

    @staticmethod
    def qualityNotMaxed(item):
        return item.quality < 50

    @staticmethod
    def stillHasQuality(item):
        return item.quality > 0

    @staticmethod
    def afterSellin(item):
        return item.sell_in < 0

    def decrease_quality_by_nb_until_zero(self, item, nb):
        for _i in range(nb):
            if self.stillHasQuality(item):
                item.quality = item.quality - 1

    def increase_quality_by_one_until_max(self, item):
        if self.qualityNotMaxed(item):
            item.quality = item.quality + 1


class ConcreteStrategyNormalItem(Strategy):
    def update_item(self, item):
        self.decrease_quality_by_nb_until_zero(item, 1)
        self.decrease_sellin_by_one(item)
        if self.afterSellin(item):
            self.decrease_quality_by_nb_until_zero(item, 1)


class ConcreteStrategyLegendaryItem(Strategy):
    def update_item(self, item):
        pass


class ConcreteStrategyConjuredItem(Strategy):
    def update_item(self, item):
        self.decrease_quality_by_nb_until_zero(item, 2)
        self.decrease_sellin_by_one(item)
        if self.afterSellin(item):
            self.decrease_quality_by_nb_until_zero(item, 2)


class ConcreteStrategyImprovingUntilExpiration(Strategy):
    def update_item(self, item):
        self.increase_quality_by_one_until_max(item)
        if item.sell_in < 11:
            self.increase_quality_by_one_until_max(item)
        if item.sell_in < 6:
            self.increase_quality_by_one_until_max(item)
        self.decrease_sellin_by_one(item)
        if self.afterSellin(item):
            self.expire(item)


class ConcreteStrategyImprovingItem(Strategy):
    def update_item(self, item):
        self.increase_quality_by_one_until_max(item)
        self.decrease_sellin_by_one(item)
        if self.afterSellin(item):
            self.increase_quality_by_one_until_max(item)


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def update_item(self, item) -> None:
        self._strategy.update_item(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        if self.is_improving_over_time(item):
            context = Context(ConcreteStrategyImprovingItem())
        elif self.is_improving_until_event(item):
            context = Context(ConcreteStrategyImprovingUntilExpiration())
        elif self.is_legendary(item):
            context = Context(ConcreteStrategyLegendaryItem())
        elif self.is_conjured(item):
            context = Context(ConcreteStrategyConjuredItem())
        else:
            context = Context(ConcreteStrategyNormalItem())

        context.update_item(item)

    @staticmethod
    def is_legendary(item):
        return item.name in ["Sulfuras, Hand of Ragnaros"]

    @staticmethod
    def is_conjured(item):
        return item.name.startswith("Conjured")

    @staticmethod
    def is_improving_until_event(item):
        return item.name.startswith("Backstage passes")

    @staticmethod
    def is_improving_over_time(item):
        return item.name in ["Aged Brie"]


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
