#lang racket

; Excercise 1
(define f1 (λ (x y)
             (append (reverse x) (reverse y))))
(f1 '(1 2 3 4) '(6 7 8))

; Excercise 2
(define f2 (λ (x)
             (cons (first(first x))
                   (cons(last(last x)) '()))))
(f2 '((1 2 3) ("a" "b" "c") (6 7 8 "d" "e")))