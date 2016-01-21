# pyWalk
A random walker using Python's Turtle module.

At the moment, this is a simple random walker. The turtle turns to the left
by a random direction, with granularity of one degree. The turtle then takes
a step of fixed size. The number of steps that this is repeated is a
parameter to the function.

## TODO
1. The direction is chosen from a uniform random distribution. It would be
   nice to be able to use a different distribution. Specifcally, forcing the
   angle between steps to be fixed (with the left/right direction random)
   would better simulate polymers.
2. The walk can self-intersect. Ensuring a self-avoiding walk is a very
   difficult problem, so allowing self-avoidance is a low priority.
3. Variable step sizes.
4. Output the turtle's intermediate locations to allow for statistics.
