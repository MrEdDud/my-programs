#lang racket

(define x '(2 5 4 1 4 3)) ; Defining a function

(define sumlist (λ (x) ; Defining a function called sumlist
                  (cond ; Starting a cond statement
                    ( (empty? x) "Empty list") ; If list is empty then return "Empty list"
                    ( (= (length x) 1) (first x)) ; If the length of x is equal to 1 then return the first element of the list
                    (else (+ (first x) (sumlist (rest x))))) ; Else add the first of x and the rest of x while calling sumlist
                  ) ; Closing lambda
  ) ; Closing define

(sumlist x) ; Calling sumlist with x as an arguement