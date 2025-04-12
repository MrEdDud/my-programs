#lang racket

(define even-filter (λ (x)
                      (cond
                        ((empty? x) x)
                        ((even? (first x)) (cons (first x) (even-filter(rest x))))
                        (else (even-filter (rest x))) )))

(even-filter '(1 2 3 4 5 6 7 8 9))