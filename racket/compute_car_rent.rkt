#lang racket

; Question 1
(struct car (car_model number_plate rental_price) #:mutable )

; Question 2
(define ford-list (list 
  (car "Ford_Focus" "123AB" 300)
  (car "Ford_Focus" "1241253" 400)
  (car "Ford_Focus" "1414" 500)))

(define bmw-list (list 
  (car "BMW_X1" "345CD" 700)
  (car "BMW_X1" "543633CD" 600)
  (car "BMW_X1" "345CDEFG" 500)))

(define mercedes-list (list 
  (car "Mercedes-Benz_Maybach" "678abcEF" 1000)
  (car "Mercedes-Benz_Maybach" "678324EF" 1200)
  (car "Mercedes-Benz_Maybach" "67ddef8EF" 3000)))

(define car-list '(ford-list bmw-list mercedes-list))

; Question 3
(define modify-price (λ (x y)
                       (map (λ (car)
                              (cond
                                ((empty? car) "Enter car type")
                                ((number? y) (set-car-rental_price! car y))))
                            x)
                       ))
(modify-price ford-list 300)
(car-rental_price (first ford-list))

; Question 4
(define computeRent (λ (num_plate dist discount_flag)
                      (map (λ (sublist)
                             (map (λ (car)
                                    (cond
                                      ((equal? num_plate) "Output")))
                                  sublist))
                           car-list)
                      )
  )



(computeRent "345CD" 2000 #f)