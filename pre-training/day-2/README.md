What's the difference between a list and a dict?
A list is just a collection of items in order. We can access things by their position like students[0] gives us the first student. It's good when the order matters or we just want to store a bunch of values together.

A dict is more like a label system. Instead of a position, every value has a name (key). So instead of remembering that index 2 is the score, we can just write student["scores"] and it's clear what it means.

When do I use each?
I use a list when I have multiple things of the same kind like a list of scores, or a list of names.
I use a dict when one thing has multiple properties like a student who has a name, a subject, and scores. It makes more sense to group them with labels than to remember which index is which.
