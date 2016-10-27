import re

from django.shortcuts import get_object_or_404


class TableForm(object):
    """
    Takes a table form format for certain collection and extracts data
    from input elements.

    Every input name should be: _collection_key_pk
    """
    def __init__(self, collection):
        self.collection = collection
        self.fields = {}

    def add_field(self, name, default, transform=None):
        if transform is None:
            transform = {}

        self.fields[name] = {
            'regex': re.compile(r'^_%s_%s_(?P<pk>\d+)$' % (self.collection, name)),
            'default': default,
            'transform': transform
        }

    def process(self, post_data):
        items = {}

        for name in post_data:
            for field in self.fields:
                match = self.fields[field]['regex'].match(name)

                if match is not None:
                    pk = match.group('pk')

                    if pk not in items:
                        items[pk] = {}

                    data = post_data[name]
                    transform = self.fields[field]['transform']
                    if data in transform:
                        items[pk][field] = transform[data]
                    else:
                        items[pk][field] = data
                    break

        for item in items.values():
            for field in self.fields:
                if field not in item:
                    item[field] = self.fields[field]['default']

        return items

    def save(self, clazz, items):
        for pk, values in items.items():
            pretest = get_object_or_404(clazz, pk=pk)

            for key, data in values.items():
                setattr(pretest, key, data)

            pretest.save()

    def process_and_save(self, clazz, post_data):
        items = self.process(post_data)
        self.save(clazz, items)
