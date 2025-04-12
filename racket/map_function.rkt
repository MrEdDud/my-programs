#lang racket

; Adds 5 to every element in the list
(define add5 (λ (n) (+ n 5)))
(map add5 '(1 3 2 5 4 6))

; Takes the first element of each list and returns them in a list
(map first '((2 3) (3 1 2) (2 1) (7)))

; Reverses each list inside the list of lists
(map reverse '((2 3) (3 1 2) (2 1) (7)))