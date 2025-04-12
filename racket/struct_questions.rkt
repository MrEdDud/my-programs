#lang racket

; Question 2
(struct film (title director running-time))
(define titanic (film "Titanic" "James Cameron" "195 minutes"))

(struct book (title author))
(define cat-in-the-hat (book "Cat in the Hat" "Dr Suess"))

(struct car (make model price))
(define ford (car "Ford" "Mustang" "£1000000000000"))

; Question 3
(film-director titanic)
(car-price ford)

; Question 4
(define q-four (λ (x)
                 (cond
                   ((empty? x) "Enter film name")
                   ((equal? (film-director x) "Scorsese") (film-title x))
                   (else "Not by Scorsese"))))

(define film2 (film "Amazing film" "Scorsese" "200 minutes"))
(q-four film2)