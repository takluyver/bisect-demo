# A demo of `git bisect`

`square.py` squares a number you give it. But it's broken with negative
numbers! I know I checked this with the first version I wrote. When did I break
it?

**git bisect** can help. It goes through the history of git commits to find the
first one where something doesn't work.
