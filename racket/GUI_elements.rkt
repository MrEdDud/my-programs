#lang racket/gui ; Needed for using GUI's

; Making the window
(define myframe (new frame%
                     [label "My Window"] ; Window name
                     [width 800] [height 500])) ; Width + Height
; Button
(define butt (new button%
                  [parent myframe]
                  [label "Click This"]
                  [callback (λ (o e) (print "Button clicked"))])) ; Outputs message when the button has been clicked
; Check box
(define check-box (new check-box%
                       [label "Check Box"][parent myframe]
                       [value #t]))
; Choice box
(define choice (new choice%
                    [label "Choose"][parent myframe]
                    [choices (list "First choice" "Second choice")]))
; Slider
(define slider (new slider%
                    [label "Slider"][parent myframe]
                    [min-value 0][max-value 100]))
; Text box
(define text-fld (new text-field%
                      [label "Text"]
                      [parent myframe]
                      [init-value "32"])) ; Sets inital text in the text box

; Making a horizontal panel (similar to HTML grids)
(define pan (new horizontal-panel%
                 [parent myframe]))
; 2 buttons in the panel
(new button% [parent pan] [label "Click This"])
(new button% [parent pan] [label "Click This"])

(send myframe show #t) ; Displaying the window by sending 'show' to the class