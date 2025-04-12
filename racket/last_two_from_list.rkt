#lang racket

;(define f1 (λ (string_list)
;             (cond
;               ((empty? string_list) "Empty list")
;               (else
;                (for ([x string_list])
;                  (display (substring x (- (string-length x) 2) ) ) )
;                )
;               )
;             )
;  )

(define list_of_strings "")
(define f1 (λ (string_list)
             (cond
               ((empty? string_list) '())
               (else
                (set! list_of_strings (cons
                 (substring (first string_list) (- (string-length (first string_list)) 2) )
                 (f1 (rest string_list))))
                list_of_strings))))

(define helper (lambda  (x) (string-join (f1 x))))

(helper '("Student" "Observable" "Behaviour"))