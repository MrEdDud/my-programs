#lang racket

; Write a function that takes a list containing characters and numbers (in random order)
; And outputs a string containing the character and a list containing the numbers and the letter preceding each of the numbers
; (i.e. if the list start with a number the preceding letter can be set to 'o')

(define string-from-list(λ (x)
          (cond
            ((empty? x) x)
            ((string? (first x)) (cons (first x) (string-from-list (rest x)) ) )
            ((number? (first x)) (cons (first x) '()) (string-from-list (rest x)) ))
            (helper-num-string x '())))

(define helper-num-string(λ (x y)
                           (cond
                             ((empty? x) x)
                             ((number? (first x)) (cons (first x) y))
                             (y))))

(string-from-list '("h" 1 2 3 "e" "l" 4 5 "l" "o"))