#lang racket

(cons 1 (cons (cons 2 (cons (cons 3 (cons 4 '())) '())) '()))

(cons (cons 1 (cons (cons 2 '()) '())) '())

(cons 1 [cons[cons[cons 2 [cons 3 '()]] [cons[cons 4 [cons 5 '()]]'()]]'()])

(cons [cons 1 '()] [cons[cons [cons 2 '()] '()][cons 3 '()]])