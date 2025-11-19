# Second Largest

## Prompt
Given a clocked sequence of unsigned values, output the second-largest value seen so far in the sequence. If only one value is seen, then the output (`dout`) should equal 0. Note that the values are treated as separate candidates for being the second largest value.

When the reset-low signal (`resetn`) goes low, all previous values seen in the input sequence should no longer be considered for thee calculation of the second largest value, and the output `dout` should restart from 0 on the next cycle.

## Input & Output Signals
- `clk`: Clock signal.
- `resetn`: Synchronous reset-low signal.
- `din`: Input data sequence.
- `dout`: Second-largest value seen so far.

## Output signals during reset
- `dout`: 0 when `resetn` is active.

## Example
- Data width: 32
- Clock cycle 1
    - `resetn`: `h0`
    - `din`: `h2`
- Clock cycle 2
    - `resetn`: `h1`
    - `din`: `h2`
- Clock cycle 3
    - `resetn`: `h1`
    - `din`: `h6`
- Clock cycle 4
    - `resetn`: `h1`
    - `din`: `h0`
- Clock cycle 5
    - `resetn`: `h1`
    - `din`: `he`
- Clock cycle 6
    - `resetn`: `h1`
    - `din`: `hc`
- Clock cycle 7
    - `resetn`: `h0`
    - `din`: `h0`
- Clock cycle 8
    - `resetn`: `h1`
    - `din`: `h1`
- Clock cycle 9
    - `resetn`: `h1`
    - `din`: `h2`
