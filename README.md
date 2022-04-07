# advent-of-code-2020

Trying to get some fun with Advent of Code 2020.


Bags
====

[
    red: white, yellow
    orange: white, yellow
    white: gold
    yellow: gold, blue
    gold: olive, plum
    olive: blue, black
    plum: blue, black
    blue: []
    black: []
]

=>

{
    white: red, orange
    yellow: red, orange
    gold: white, yellow
    blue: yellow, olive, plum
    olive: gold
    plum: gold
    black: olive, plum
}

Containers: white*, yellow*, red*, orange*

Answer: 4
