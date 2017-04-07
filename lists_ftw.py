# Because sometimes you don't want to wrap everything in list():
import itertools


def lfilter(func, itera):
    return list(
        filter(func, itera)
    )


# Thanks to:
# https://stackoverflow.com/a/40015905/2662028
def lmap(func, *itera):
    return list(
        itertools.starmap(func, itertools.zip_longest(*itera))
    )


def lzip(*itera):
    return list(
        itertools.zip_longest(*itera)
    )

