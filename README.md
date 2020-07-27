# SNOW-3G-encryption-algorithm

This is an implementation of the SNOW 3G encryption algorithm written in Python.
It consists of the core of my University's final project.

The objective of this project is to provide a tool that generates encryption sequences for the analysis and study of the parameters of the sequences.

SNOW 3G is a stream cipher algorithm oriented to 32 bits words based on PRNG over extended fields of Galois. The cipher has two parts, the LFSR is the linear part and the FSM provides the non-linear part.

The algorithm has two operation modes. First of all, the cipher enters initialization mode, then it switch to generation mode.
  - Initialization mode: in this mode, the LFSR receives the seed as initial state. At the same time, the FSM synchronizes by setting all its states to zero. The cipher does not generate any sequences, after 32 iterations of the loop, the final state is the new seed for the generation mode.
  - Generation mode: after receives the new seed, the cipher generates sequences each clock pulse.
