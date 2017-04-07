# lists_ftw.py
Because sometimes you don't want to wrap everything in `list()`. Gives you `lfilter`, `lmap`, and `lzip` (which will not collide with any builtins).

```py
from lists_ftw import *
print(
    lfilter(None, [True, False, True])
)
# => [True, True]

print(
    lmap(lambda x: x + 2, [1, 2, 3])
)
# => [3, 4, 5]

print(
    lzip([1, 2, 3], [4, 5, 6])
)
# => [(1, 4), (2, 5), (3, 6)]
```
