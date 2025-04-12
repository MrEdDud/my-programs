#lang racket

(define isin? (λ (x y)
                (cond
                  ((empty? y) #f)
                  ((= (first y) x) #t)
                  (else (isin? x (rest y))))))

(isin? 7 '(1 2 3 4))