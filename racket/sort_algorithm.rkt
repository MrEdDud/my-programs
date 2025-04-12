#lang racket

(define my-insert (λ (i sl)
                    (cond
                      ((empty? sl) (list i))
                      ((<= i (first sl)) (cons i sl))
                      (else (cons (first sl) (my-insert i (rest sl))))
                      )
                    )
  )

(define my-merge (λ (ul sl)
                   (cond
                     ((empty? ul) sl)
                     (else (my-insert (first ul) (my-merge (rest ul) sl)))
                     )
                   )
  )

(my-merge '(2 9 4) '(1 2 3))