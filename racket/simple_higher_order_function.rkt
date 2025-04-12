#lang racket

(define list<=? (λ (list1 list2)
                  (<= (length list1) (length list2))))

(sort '((1 2 3) (1 3) (1 2 3 4) (1) () (1 4 3)) list<=?) ; Second arguement is a function