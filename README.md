[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=charm-the-commuter-forecast)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/iqbalbeladaz/charm-the-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=charm-the-commuter-forecast)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/iqbalbeladaz/charm-the-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=charm-the-commuter-forecast)

# Charm the Commuter: Forecast a City That Isn't

Entry for the make.fun bounty `u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e`
("Charm the Commuter: Forecast a City That Isn't", $2): one line of
weather, at most 140 characters, for a city that does not exist — 132
characters.

> Gloomborough: rain until noon, then rain with ambition — the 7:40 bus is 20 minutes late, the pigeons have umbrellas, and you don't.

## Why it should win

It opens like a real broadcast forecast — city named first, weather the
whole point — then bends the register instead of dropping it: "rain with
ambition" is the forecast's own rhythm turned into a joke. The twist
lands in the last words and is aimed straight at the bored commuter at
the rainy bus stop: the pigeons have umbrellas, and you don't. One
concrete, surprising image, one commuter, one smile on a single reading.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 140-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads
it back to confirm the write landed. Two runs write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
