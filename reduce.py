# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats the process until one value remains
# sintaxis: reudce(function,iterable)

import functools

letters = ["T","E","N","N","I","S"]
word = functools.reduce(lambda x,y:x+y, letters) # reduce() being used here, the function inside adds the letters,
                                                # and returns a cumulative value o a single word
print(word)