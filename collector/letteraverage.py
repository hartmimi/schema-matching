from __future__ import division, absolute_import
from . import ItemCollector
from .itemcount import ItemCountCollector
from .lettercount import ItemLetterCountCollector
from .itemaverage import normalize


class ItemLetterAverageCollector(ItemCollector):

    def __init__(self, previous_collector_set = None):
      ItemCollector.__init__(self, previous_collector_set)


    result_dependencies = (ItemLetterCountCollector, ItemCountCollector)


    def get_result(self, collector_set):
        return collector_set[ItemLetterCountCollector].get_result() / collector_set[ItemCountCollector].get_result()
