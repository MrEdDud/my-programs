#lang racket
; for i in list
(define double-list
  (λ (l)
    (for/list ([i l]) (* i 2))))

(double-list '(1 2 3 4 5))
"=-=-=-=-=-=-=-=-=-=-=-=-=-="
; for i in vector
(define add-5
  (λ (v)
    (for/vector ([i v]) (+ i 5))))

(add-5 (vector 1 2 3 4 5))
"=-=-=-=-=-=-=-=-=-=-=-=-=-="
; for x in range
(define add5 (λ (v)
               (for ([x(range (vector-length v))])
                 (vector-set! v x (+ (vector-ref v x) 5)))
               (display v)))

(add5 (vector 1 2 3 4 5))