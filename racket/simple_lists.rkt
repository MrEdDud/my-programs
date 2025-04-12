#lang racket

(define mylist '((1 2 3)(4 5 6)(7 8 9)))
(+(second (first mylist))(third (second mylist)))