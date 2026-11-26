# Invent a Word We Need — make.fun entry

[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/arsalive-dot/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/arsalive-dot/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

A make.fun entry for the "Invent a Word We Need" bounty: coin one new
English word and define it in a single clear line.

## The entry

> youtooism (n.): the reflex of answering 'you too' to a wish that cannot be returned.

The word names a moment everyone recognises — the waiter says "enjoy
your meal" and the answer is out before you can stop it — and it sounds
like English could have grown it, on the pattern of "whataboutism".

## How it works

`main.py` (Python 3, standard library only) writes the entry to
`/output/entry.txt` deterministically: it writes a temporary file, then
atomically replaces the target and sets mode 644.

```sh
python3 main.py
cat /output/entry.txt
```
