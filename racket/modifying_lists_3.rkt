#lang racket

; Both lists
(define L1 '(1 2 3 4 5))
(define L2 '(6 7 8 9 10))

; Task a
(rest (rest (rest L2)))

; Task b
(append (rest(rest(rest L1))) L2)

; Task c
(append (list(first L1)) (list(first L2)))

; Task d
(first(reverse L2))
