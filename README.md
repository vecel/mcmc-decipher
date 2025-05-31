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
decode text in a way that it is readable and understandable
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
<div align="justify">
In this section we discuss our studies on algorithm and probabilistic approach of decoding the crypted messages. We aim to identify limitations, characteristics and qualities depending on the factors such as message length, language corpus length, initial starting key and language group.
</div>

### Quality of decryption regarding text length and corpus length
<div align="justify">
We analyzed how different message and corpus lengths impact the algorithm's performance. We examined combinations of text's lengths: 100, 250, 500, 1000 with corpus lengths equal to 100k, 250k, 1M, 5M, 20M.
</div>
<br>
<div align="justify">
For each encrypted message and corpus pair we ran default implementation of the algorithm 50 times recording how many times we got exact, close, and numeric solution. Below we define these metrics.<br><br>
<b>Exact</b> solution is a solution exactly matching the original, not encrypted message.<br> 
<b>Close</b> solution is a solution whose likelihood score does not differ from original messages' score by given trust level. In our analysis we used trust level value equal to 0.1. We use this metric to measure how many times a readable solution was reached. We define a readable solution as one that a person can read and understand easily.<br>
<b>Numeric</b> solution is a solution with high content of numbers. We called a solution numeric if at least half of its characters were numbers.<br>
</div>
<br>
<div align="justify">
We visualise the results using three heatmaps that display the ratios of these solutions.
</div>
<br>

![heatmaps](images/text_length_vs_corpus_length_heatmaps.png)

#### Observations
<div align="justify">
<ol>
<li>
 Correct solutions were almost never found despite using larger corpora. We can see that the biggest (20M characters) corpus got some stable correct solutions, but performance of 4 out of 50 attempts in the best scenario is very poor.
</li>
<li>
Bigger corpus yields better close solutions ratio with strange peak in corpus length of 250k. We will discuss it in the next section.
</li>
<li>
Numeric solutions ratio decreases with corpus length. For small corpora most of the found solutions were numeric while for the biggest corpus this ratio varies around 0.14.
</li>
</ol>
</div>

#### Close versus Numeric
<div align="justify">
We faced an anomaly of having tremendous ratio of close solutions for small corpus (250k). The intuition says that this metric should increase with corpus' size. The explanation is that not every close solution is actually close to the original message. Because by close we mean similar likelihood score we do not actually measure whether the solution is readable by a human. It turns out that for smaller corpuses numeric solutions have better scores than original messages (see 100k characters corpus). The explanation of phenomena of having about 0.80 close solutions ratio for corpus of length 250k is that in this case original solution's score was similar to numeric solutions scores. We can see that we often ended in numeric solutions (with ratio about 0.78). For bigger corpora numeric solutions have lower score than the original message, so solutions classified as close are indeed easy to understand by a human. 
</div>
<br>
<div align="justify">
For example using the whole corpus, numeric solutions score fluctuated about -2282 while correct message score was -1089. Plot below presents the results of running algorithm 50 times for text of length about 500 characters and corpus of length 28M.
</div>
<br>

![](images/decoding_score.png)

### Frequency based initial decoding key
### Quality of decryption depending on the language group
### Sources
1. https://medium.com/data-science/breaking-the-enigma-code-in-python-with-mcmc-marvel-themed-9ceb358dd8ae
2. https://github.com/JackWillz/Projects/tree/master/MCMC%20-%20Enigma%20Thanos

[1]: https://medium.com/data-science/breaking-the-enigma-code-in-python-with-mcmc-marvel-themed-9ceb358dd8ae