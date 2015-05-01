---
layout: page
title: Testing Scientific Software
subtitle: Building a Test Suite
minutes: 5
---

Putting our tests in a script and
using `assert` statements instead of `print` statements
has greatly improved the quality of our tests.
But even this approach has a few problems:

1. When a test fails (i.e., when an assertion's condition evaluates to 'false'),
the test script stops running, and we only know about the first failure.
We won't know till we fix our code and run the tests again if something else is wrong.

2. We're still re-setting the system after each test.
There is a lot of duplicate code, and that's almost *always* a bad idea.

What we'd *like* to do is to have our tests all run independently,
and look at which ones passed and which failed.
Then, we can make informed decisions about what needs fixing.
We'd also like a way to automatically reset the system after each test.

Fortunately, there's a way to do just this:

#FIXME: organize tests into a test suite
