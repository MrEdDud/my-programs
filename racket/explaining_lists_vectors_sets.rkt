#lang racket

; List problem => A program with an appointment system where each patient has a specific time they need to be at
"LIST PROBLEM" ; Title of the problem

(define bookings-list '("Bob" "Jimmy")) ; Defined a function which holds a list
(define f1(λ (x y) ; Defined a function and lambda with 2 arguements
            (cond ; Started a cond statement
              ((empty? x) "Enter your name") ; If x, the name input, is empty then it will return 'Enter your name'
              (else (append (rest y) (list x)))))) ; Else it will append the rest of y, a list, and x

(string-append "Next patient is " (first bookings-list)) ; Output a message using string concatenation

(f1 "Steve" bookings-list) ; Calling the function with 2 arguements

; I used a list for this problem because lists are immutable which means values in the list cannot be changed
; They are ordered which means that the people in the queue will not change in order
; Finally lists are not fixed in length meaning that I can add more people to the list

"-----------------------------------------------------------" ; Just for seperating the outputs of the different questions
; Vector problem => A program for a factory which produces a fixed amount of items
"VECTOR PROBLEM" ; Title of the problem

(define items-produced (vector "Keyboard" "Mouse" "Microphone")) ; Defined a function which holds a vector
(define change-production (λ (x y z) ; Defined a function and lambda with 3 arguements
                            (cond ; Started a cond statement
                              ((empty? x) "Enter item") ; If arguement x is empty then ouput a message
                              ((empty? y) "Enter which item you want to change") ; If arguement y is empty then ouput a message
                              ((= y 1)(vector-set! z (- y 1) x) z) ; If y is equal to 1 then change the first item in the vector with x, a string, then output z, the vector 
                              ((= y 2)(vector-set! z (- y 1) x) z) ; If y is equal to 2 then change the second item in the vector with x, a string, then output z, the vector 
                              ((= y 3)(vector-set! z (- y 1) x) z) ; If y is equal to 3 then change the third item in the vector with x, a string, then output z, the vector 
                              (else "Type the correct number")))) ; Else then output a message

(change-production "Speaker" 2 items-produced) ; Calling the function with 3 arguements

; I used a vector for this problem because vectors are mutable, meaning that values inside the vector can be changed
; Vectors are also usually fixed in length after being defined
; Finally vectors are ordered meaning that I can select the specific elements I want to modify

"-----------------------------------------------------------" ; Just for seperating the outputs of the different questions
; Set problem => Making a program which allows users to enter their national ID
"SET PROBLEM" ; Title of the problem

(define national-ID (λ (x) ; Defined a function and lambda with 1 arguement
                      (cond ; Started a cond statement
                        ((empty? x)"No ID entered") ; If the set is empty then return a message
                        (else (set-union x (set 112233)))))) ; Else add x to the existing set

(national-ID (set 112233)) ; Calling the function with 1 arguement, it being a set

; The main reason I chose a set for this situation is because sets do not recognise duplicate values which makes each value unique
; Sets are also unordered
; Depending on the situation, sets can be mutable or immutable
; However in my situation my set is immutable because when I use 'set-union' I make a new set