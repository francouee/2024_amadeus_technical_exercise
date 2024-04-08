# Technical exercise Amadeus


The goal of the exercise is to **build** a **model** able to **predict** the **probability** of **winning an auction** based on historical bids with:
* $X$ = Features describing the item to bid on
* bid = The price paid for the item (denoted $s$ in the following)
* auctions = The minimum price needed to win the auction
* wins = The earning of related to the auctioned item

Before answering the questions, I place **set some context** around the **global problem** we want to solve : **benefits optimization when participating in auctions**.

## Context

When taking part in auctions, every participants wants to maximize their benefits by optimizing their biding prices. There are two components to take into account :
1. The probability of winning the auction for a bid $s$ and item features X.
2. The item value knowing its features X (could be the probability of a user clicking the advertising in an online ads context).

Mathematically, one participants wish to maximize the following :

$$
\sum_{i=1}^{n} \mathbb{1}_{\text{winning auction i}} . r_i(\text{value}_i - \text{bid}_i) \qquad (1) \\ r_i \text{ an optional discount factor, equal to 1 in the following}
$$

We can think of two ways for solving this problem :
1. Using dynamic programming, where we learn a policy $\Pi(i, a)$ for all states $a=\{X, \text{past winning prices}, \text{past item values}\}$
2. Using statistical learning, modelling both 1. probabilities of winning the auction and 2. the item value.

```{note}
In this work we will only solve the problem using statistical learning methods.
```

## Probabilistic modelling of auctions

Two events need to be modelled :
1. $\text{Winning auction} = W|X, s \sim \text{Bernouilli}(p_{x, s})$, modelled by a bernouilli variable which probability p depends on both the features X and the bidding price s.
2. $\text{Item value} = V|X$, random variable depending on item features X.

The equation $(1)$ can be written as realizations of the the following random variable :

$$
Z = \sum_{i=1}^{n} W_i \mid X_i, s_i \ . \ (V_i \mid X_i - s_i)
$$

We can reason about the expectation of the latter random variable. Also noticing that $W_i \mid X_i, s_i \perp (V_i \mid X_i - s_i)$ we can derive the following expressions [^1] :
[^1]: Supposing that all information about the auction is inside features $X_i$ and the bid $s_i$. Thus $E[X . Y] = E[X] . E[Y]$.

$$
E(Z) = \sum_{i=1}^{n} E(W_i \mid X_i, s_i) \ . \ E(V_i \mid X_i - s_i)
$$

(introduction:auction_formulation)=
$$
E(Z) = \sum_{i=1}^{n} \ \underbrace{p_{x_i, s_i}}_{\text{Probability to win the auction}} \ . \ \underbrace{(E(V_i \mid X_i) - s_i)}_{\text{auction payoff}} \qquad (2)
$$

The latter equation highlight the intuitive importance of the **probability** of **winning the auction** for **optimizing** the auctions **benefits**.

In the next sections we will answer to the 3 following questions :

1. Develop a model to predict the probability of winning an auction based on our bid and the item feature x. If you can think of a way, the model should ideally also be able to predict the confidence of predictions.
2. Derive the probability density function for the winning bid for x=3. What is the probability that the winning bid lies between 1 and 2?
3. Let’s assume that we participate again on an identical set of auctions with the same bids as in the provided dataset. Based on your model, what is the probability of observing costs larger than in the provided dataset?

{cite}`survey_of_auction_theory`