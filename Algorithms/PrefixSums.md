<!-- TOC -->

- [Prefix Sums](#prefix-sums)

<!-- /TOC -->
# Prefix Sums
Given a question like Lil jami, you would repeatedly have to find the sum of a portion of your array.

&nbsp;&nbsp;&nbsp;&nbsp;Most of you would find it fairly easy to complete the question. But to make runtime minimal, that is a different story. The general
idea is to have an array (or list) of length N, and update its values as the input is given. Then, repeatedly output the sum of the
items in the portion they ask for. That is rather inefficient though, as you will perform up to N*K operations, which could be up to
10^12 (in Lil jami’s case).
