# A demo of `git bisect`

`square.py` squares a number you give it. But it's broken with negative
numbers! I know I checked this with the first version I wrote. When did I break
it?

    $ python3 square.py 5
    25
    $ python3 square.py -6
    0

**git bisect** can help. It goes through the history of git commits to find the
first one where something doesn't work.

This example demonstrates *how* to use git bisect, but it doesn't really show
*why*. It's easy here to look at the script and see what's going wrong. Bisect
is more useful when you have a big complicated codebase, and it's not obvious
where a bug is coming from.

The [git bisect documentation](https://git-scm.com/docs/git-bisect)
has much more detail about what it can do.

## Bisecting manually

To start git bisecting, we have to tell it a point when the code is *bad*—
this is the current commit—and one where it's *good*, i.e. before it got broken.
In this repository, I've made a tag `my-first-code` when I know this was working,
but it can be trickier to figure out in real life.

    $ git bisect start
    $ git bisect bad
    $ git bisect good my-first-code 
    Bisecting: 7 revisions left to test after this (roughly 3 steps)
    [84e9e6343a2cb00b12439c4a9022f9666b9ac0df] Use argparse for command line

Now it's checked out a new revision, half way between our good and bad ones.
We need to try it and tell git if it's good (working) or bad (broken).

    $ python3 square.py -6
    0
    $ git bisect bad
    Bisecting: 3 revisions left to test after this (roughly 2 steps)
    [ebe7c91e9d7c558a61ebed24b45adf181f5020f7] Multiplication is just repeated addition

Each time we say `git bisect bad` or `git bisect good`, git will give us a new
commit to try. After a few times, it has narrowed it down to one commit—[this
one](https://github.com/takluyver/bisect-demo/commit/ebe7c91e9d7c558a61ebed24b45adf181f5020f7).

    ebe7c91e9d7c558a61ebed24b45adf181f5020f7 is the first bad commit
    commit ebe7c91e9d7c558a61ebed24b45adf181f5020f7
    Author: Thomas Kluyver
    Date:   Wed Nov 29 18:34:06 2017 +0000

    Multiplication is just repeated addition

    :100644 100644 f68ade3b07c88b099742b55b9cf4de591687b941 03989097f0eb54a10646b6b02c89079b2fc56b20 M	square.py

Finally, finish bisecting and go back to where we were:

    $ git bisect reset
    Previous HEAD position was 59f2008... Check that we get an integer
    Switched to branch 'master'
    Your branch is up-to-date with 'origin/master'.

## Bisecting automatically

If we bisect manually, we still have to figure out if it's working each time.
That can be tedious, so can we make the computer do it for us?

There's a test in this folder, `test_square.py`. You can run it with `py.test`,
and see that it fails. We can tell git bisect to run this automatically to
check for working code.

First, make a copy of the test file. The test was only added after the bug
was introduced, so when git goes back in history, it will delete the file that's
tracked in git. Making a copy gets around this.

    $ cp test_square.py test_square2.py

Start bisecting like before:

    $ git bisect start
    $ git bisect bad
    $ git bisect good my-first-code 
    Bisecting: 7 revisions left to test after this (roughly 3 steps)
    [84e9e6343a2cb00b12439c4a9022f9666b9ac0df] Use argparse for command line

Now we tell git to run `py.test`:

    $ git bisect run py.test

Your terminal will rapidly fill up with information as git jumps around and
re-runs your tests. When it stops, you should see the same result as manual
bisecting.

    ebe7c91e9d7c558a61ebed24b45adf181f5020f7 is the first bad commit
    commit ebe7c91e9d7c558a61ebed24b45adf181f5020f7
    Author: Thomas Kluyver
    Date:   Wed Nov 29 18:34:06 2017 +0000

    Multiplication is just repeated addition

    :100644 100644 f68ade3b07c88b099742b55b9cf4de591687b941 03989097f0eb54a10646b6b02c89079b2fc56b20 M	square.py
    bisect run success

Don't forget to finish bisecting and go back to where you were:

    $ git bisect reset
    Previous HEAD position was 59f2008... Check that we get an integer
    Switched to branch 'master'
    Your branch is up-to-date with 'origin/master'.

Git can run any script you give it. The only requirement is that it exits
successfully (exit code 0) if your code is good, and errors (exit code not 0)
if your code is bad.
