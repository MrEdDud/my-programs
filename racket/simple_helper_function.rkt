#lang racket

(define counth (λ (x y n)
                 (cond
                   ((empty? y) n)
                   ((= (first y) x) (counth x (rest y) (+ n 1)))
                   (else (counth x (rest y) n)))))

(define count (λ (x y) (counth x y 0)))

(count 7 '(1 2 3 7 5 6 7 7 9))