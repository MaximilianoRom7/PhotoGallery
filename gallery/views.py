from django.http import HttpResponse
from django.shortcuts import render


class Pictures:

    def __init__(self):
        # _picks should an array of picture objects
        self._pics = range(100)

    def tableSize(self, n):
        end = 0
        length = len(self._pics)
        while end < length:
            start = end
            end = start + n
            chunk = self._pics[start:end]
            if chunk:
                yield chunk

    @property
    def small(self):
        """
        Creates a small size table, each row has 3 pictures
        """
        return self.tableSize(3)

    @property
    def medium(self):
        """
        Creates a medium size table, each row has 5 pictures
        """
        return self.tableSize(5)

    @property
    def big(self):
        """
        Creates a big size table, each row has 7 pictures
        """
        return self.tableSize(7)

    def __iter__(self):
        for item in self.medium:
            yield item

def index(request):
    # example
    pictures = Pictures()
    context = {'pictures': pictures}
    return render(request, 'gallery/index.html', context)
