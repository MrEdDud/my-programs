#lang racket

; Question 1
(define epic-list '(1 2 3 4 5))
(for/list ([x epic-list]) (* x 2))

; Question 2
(for/list ([x epic-list]) (+ x 5))

; Question 3
(for/list ([x (reverse epic-list)]) (- x 4))

; Question 4
(for/list ([x epic-list])
  (cond
    ((even? x) (+ x 2))
    (else x)))
