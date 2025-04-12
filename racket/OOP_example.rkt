#lang racket

(define book-class%
  (class object%
    (init-field (pages 5)) ; sets default value of 'pages'
    (define/public (letters)
      (* pages 500))
    (super-new)))

(define book1 (new book-class%)) ; using 'new' to create an object called 'book1' for the class
(send book1 letters)

(define book2 (new book-class% [pages 100])) ; sets pages to 100
(send book2 letters)
"------------------"
(define account% (class object%
                   (super-new) ; initialises the superclass

                   (field (balance 0)) ; makes a field (class variable)

                   (define/public (add n) ; a method which adds money to balance
                     (set! balance (+ n balance)))

                   (define/public (get-balance) balance)))

(define mysimpleaccount (new account%)) ; creates an account
(send mysimpleaccount add 100) ; adds 100 to account
(send mysimpleaccount add 50) ; adds 50 to account
(send mysimpleaccount get-balance) ; shows new balance