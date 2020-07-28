# SNOW-3G-encryption-algorithm

This is an implementation of the SNOW 3G encryption algorithm written in Python.
It consists of the core of my degree's final project.

The objective of this project is to provide a tool that generates encryption sequences for the analysis and study of the parameters of the sequences.

SNOW 3G is a stream cipher algorithm oriented to 32 bits words based on PRNG over extended fields of Galois. The cipher has two parts, the LFSR is the linear part and the FSM provides the non-linear part.

The algorithm has two operation modes. First of all, the cipher sets initialization mode, then it switch to generation mode.
  - Initialization mode: in this mode, the LFSR receives the seed as initial state. At the same time, the FSM synchronizes by setting all its states to zero. The cipher does not generate any sequences, after 32 iterations of the loop, the final state is the new seed for the generation mode.
  - Generation mode: after receives the new seed, the cipher generates sequences each clock pulse.

Apart of this, I've been developing a simple interface which asks for all the necessary data.
 - 'k' and 'IV': these variables are the initial seed. k and IV are 32 bits variable. [Hex]
 - 'm': this variable set the cipher to the functioning mode.
  - m=1: initialization mode + generation mode
  - m=2: generation mode (at this mode, the cipher skips the first mode and generates other types of sequences)
 - 'n': sequences length
 - fich_name: name of the fich which saves all data
 
Example:
  - k='8ce33e2cc3c0b5fc1f3de8a6dc66b1f3'
  - IV='d3c5d592327fb11cde551988ceb2f9b7'
  - m=1
  - n=4
  - fich_name=whatever haha
  
  - output=[BitArray('0xeff8a342'), BitArray('0xf751480f'), BitArray('0x8383b51d'), BitArray('0xdf4815fa')]

To validate the correct functioning of the cipher, first of all I checked the correct functioning of the most basic functions (MULx, MULxPOW, MULalpha, DIValpha) with the examples provided by the specification itself. Then, to validate the output I used the portal https://asecuritysite.com/encryption/snow which provides two examples.

This script has been written in Python v3.8 and it uses the bitstring library.
