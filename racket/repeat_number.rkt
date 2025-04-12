#lang racket

(define myFun (λ (num)
                (cond ((<= num 0) "Enter a number above 0")(else
                      (for ([x (in-range num)])
                        (for ([y (in-range x)]) (display (number->string (+ x 1))))
                        (displayln (number->string (+ x 1)) )
                        )
                      )
                      )
                )
  )

(myFun 5)

; python ver
;y = ""
;for x in range(5):
;    y = str(x) * x
;    print(y)