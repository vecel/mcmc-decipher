# MCMC Decipher
<div align="justify">
An exploration of using Monte Carlo Markov Chain (MCMC) methods to break substitution ciphers - a classic encryption technique where each letter is replaced with another. This project demonstrates how probabilistic modeling and MCMC sampling can be applied to decrypt encoded text by learning likely letter mappings based on language patterns. For the introduction to the project we recommend to read this <a href="https://medium.com/data-science/breaking-the-enigma-code-in-python-with-mcmc-marvel-themed-9ceb358dd8ae">article</a> by Jack J on Medium.
</div>

## Introduction
### Problem
[comment]: <> (Try to center this text while keeping latex code - 26! is over 4 * 10^26)
<div align="justify">
We are facing the problem of deciphering a message encoded with substitution cipher, where each letter from the alphabet is replaced with another one from the same alphabet. Although the method is straightforward to implement, decrypting a message is not trivial. The core difficulty is the number of possible encryption keys which is the number of possible alphabet's permutations. For example English alphabet has 26 letters, which gives 26! potential keys. If we also consider numbers and punctuation we get 43 characters. This gives us 43! potential keys! This makes brute force approach infeasible.

</div>

### Goal
### Core Idea
encoded text given
state space - all encoded text permutations obtained by swaping two keys in encryption dictionary

encoded text associated with encryption dictionary 1-1

proposal states chosen uniformly 

acceptance function : later

after a long time we get the sample from stationary distribution - given by multiplying certain probabilities from perc_dicts based on a corpus

'real' text is the most probable (we hope) so the final sample is supposed to be real decoded text 
### Approach

## Exploaration
[comment]: <> (Place our analysis here in some kind of subsections)
### Frequency based initial decoding key
### Quality of decryption regarding text length and corpus length
### Quality of decryption depending on the language group
### Sources
1. https://medium.com/data-science/breaking-the-enigma-code-in-python-with-mcmc-marvel-themed-9ceb358dd8ae
2. https://github.com/JackWillz/Projects/tree/master/MCMC%20-%20Enigma%20Thanos

[1]: https://medium.com/data-science/breaking-the-enigma-code-in-python-with-mcmc-marvel-themed-9ceb358dd8ae