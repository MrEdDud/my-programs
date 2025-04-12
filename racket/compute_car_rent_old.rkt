#lang racket

; Question 1
(struct car (car_model number_plate rental_price) #:mutable )

; Question 2
(define car1 (car "Ford_Focus" "123AB" 300))
(define car2 (car "Ford_Focus" "1241253" 400))
(define car3 (car "Ford_Focus" "1414" 500))
(define car4 (car "BMW_X1" "345CD" 700))
(define car5 (car "Mercedes-Benz_Maybach" "678EF" 1000))

(define car_list (list car1 car2 car3 car4 car5))

; Question 3
(define modify-price (λ (lst cm pr)
                       (cond
                         [(empty? lst) "end of treatment"]
                         [(equal? cm (car-car_model (first lst)))
                          (set-car-rental_price! (first lst) pr)
                          (modify-price (rest lst) cm pr)]
                         [else (modify-price (rest lst) cm pr)])))
                       
(modify-price car_list "Ford_Focus" 700)
(displayln (car-rental_price car1))

; Question 4
(define computeRent (λ (x dist flag)
                      (cond
                        ((and (car? x) flag)
                         (* (+ (car-rental_price x) (* dist 0.8)) 0.75))
                        ((and (car? x) (not flag))
                         (+ (car-rental_price x) (* dist 0.8)))
                        (else "not a car struct"))))

(computeRent car3 2000 #f)