<!-- TOC -->

- [Prefix Sums](#prefix-sums)

<!-- /TOC -->
# Prefix Sums
Given a question like [Lil jami](http://wcipeg.com/problem/liljami), you would repeatedly have to find the sum of a portion of your array.

&nbsp;&nbsp;&nbsp;&nbsp;Most of you would find it fairly easy to complete the question. But to make runtime minimal, that is a
different story. The general
idea is to have an array (or list) of length N, and update its values as the input is given. Then, repeatedly output the sum of the
items in the portion they ask for. That is rather inefficient though, as you will perform *O*(N*K) operations, which could be up to
1e+12 (in Lil jami’s case).

&nbsp;&nbsp;&nbsp;&nbsp;That is where the need of an algorithm comes in. The goal is to change your array, so that you will perform minimal operations once asked to. Given an array `[a, b, c, d]`, we can convert each item to be the sum of all the items before it and itself. This changes our array to `[a, a+b, a+b+c, a+b+c+d]`. With our new array, we can simply subtract to find the sum wanted.
