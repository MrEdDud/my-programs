#lang racket/gui

(struct user (username email password dob))
(struct events (band date location city cost))

(define event1 (events "QUEEN" "22-06-2025" "Wembley Stadium" "London, UK" "£100"))
(define event2 (events "AC/DC" "24-02-2025" "New Century Hall" "Manchester, UK" "£20"))
(define event-list (list event1 event2))
(define saved-events (list))
;===========================================================================================================================================================================
;; R1.1

; Making the main window
(define frame (new frame% [label "Concert app"] [width 400][height 650]))

; Panels
(define v_panel (new vertical-panel% [parent frame] [alignment '(center center)]))
(define h_panel (new horizontal-panel% [parent v_panel] [alignment '(center center)]))

(new message% [parent h_panel][label "Are you a "]) ; Text

; Making the Band button
(new button% [parent h_panel] [label "Band"] ; Setting the parent and the name
     [callback (λ (button button-event)
                 (send band_signup show #t) ; Shows the next frame
                 (send frame show #f))]) ; Hides the first frame

; Making the Fan button
(new button% [parent h_panel] [label "Fan"] ; Setting the parent and the name
     [callback (λ (button button-event)
                 (send fan_signup show #t) ; Shows the next frame
                 (send frame show #f))]) ; Hides the first frame)
;===========================================================================================================================================================================
;; R1.2

; Making a new frame for the sign up page for FANS
(define fan_signup (new frame% [label "Fan Sign-up"] [width 400][height 650]))

; Back button
(new button% [parent fan_signup][label "Back"]
     [callback (λ (button button-event)
                 (send frame show #t)
                 (send fan_signup show #f))])

(define group-box-panel (new group-box-panel% [parent fan_signup] [label "Fan Signup"])) ; Made a group box panel
; All the fields for the sign up page
(define username (new text-field% [parent group-box-panel] [label "Username"])) ; Setting the parent and the name
(define email (new text-field% [parent group-box-panel] [label "Email"])) ; Setting the parent and the name
(define dob (new text-field% [parent group-box-panel] [label "Date of birth"])) ; Setting the parent and the name
(define password (new text-field% [parent group-box-panel] [label "Password"])) ; Setting the parent and the name
(define conditions (new check-box% [parent group-box-panel] [label "Terms and conditions"] [value #f])) ; Setting the parent, the name and the value

; Making a button to send the user to the next page
(new button% [parent group-box-panel] [label "Submit"]
     [callback (λ (button button-event)
                 (send fan_menu show #t) ; Shows the next frame
                 (send fan_signup show #f))]) ; Hides the current frame

; Making a new frame for the sign up page for BANDS
(define band_signup (new frame% [label "Band Sign-up"] [width 400][height 650]))

; Back button
(new button% [parent band_signup][label "Back"]
     [callback (λ (button button-event)
                 (send frame show #t)
                 (send band_signup show #f))])
; Title
(new message% [parent band_signup][label "Band Signup"]) ; Text
; All the fields for the sign up page
(define bandname (new text-field% [parent band_signup] [label "Band name"])) ; Setting the parent and the name
(define band_email (new text-field% [parent band_signup] [label "Email"])) ; Setting the parent and the name
(define band_password (new text-field% [parent band_signup] [label "Password"])) ; Setting the parent and the name
(define t_and_c (new check-box% [parent band_signup] [label "Terms and conditions"] [value #f])) ; Setting the parent, the name and the value
;===========================================================================================================================================================================
;; START OF RAJAB'S SECTION

;; Function to create and open the new window (window2)
(define (open-concert-window concert-name)
  (define window2 (new frame%
                          [label "Listing"]
                          [width 400]
                          [height 500]))
  
  ;; Top label and message
  (new message% [parent window2] [label concert-name])
  
  ;; Add Text Box with label "Band :"
  (define band-field (new text-field%
                          [parent window2]
                          [label "Band :"]
                          [init-value ""]))
  
  ;; Add Text Box with label "Date :" and initial value "dd/mm/yyyy"
  (define date-field (new text-field%
                          [parent window2]
                          [label "Date :"]
                          [init-value "dd/mm/yyyy"]))
  
  ;; Add Text Box with label "Time :" and initial value "xx:xx"
  (define time-field (new text-field%
                          [parent window2]
                          [label "Time :"]
                          [init-value "xx:xx"]))
  
  ;; Add Text Box with label "Duration :" and initial value "-- hours, -- minutes"
  (define duration-field (new text-field%
                               [parent window2]
                               [label "Duration :"]
                               [init-value "-- hours, -- minutes"]))
  
  ;; Add Text Box with label "Venue :"
  (define venue-field (new text-field%
                            [parent window2]
                            [label "Venue :"]
                            [init-value ""]))
  
  ;; Add Text Box with label "Total Price :" with validation for numeric input
  (define price-field (new text-field%
                            [parent window2]
                            [label "Total Price : £"]
                            [init-value ""]
                            [callback
                             (lambda (field event)
                               (let ([input (send field get-value)])
                                 (when (not (regexp-match? #rx"^[0-9]*\\.?[0-9]*$" input))
                                   (send field set-value "")
                                   (message-box "Error"
                                                "Please enter a valid number!"
                                                window2
                                                'ok))))]))

  ;; Add Back button
  (define back-button (new button%
                            [parent window2]
                            [label "Back"]
                            [callback (lambda (button event)
                                        (send window2 show #f) ; Close window2
                                        (send window show #t))])) ; Return to main window

  (send window2 show #t))

;; Main window (window)
(define window (new frame%
                        [label "Concert Listings"]
                        [width 400]
                        [height 650]))

; Making a button to send the user to the next page
(new button% [parent band_signup] [label "Submit"]
     [callback (λ (button button-event)
                 (send window show #t) ; Shows the next frame
                 (send band_signup show #f))]) ; Hides the current frame

(define vert_panel (new vertical-panel% [parent window] [alignment '(left top)]))

(new message% [parent vert_panel] [label "12/01"])

;; Concert 1
(define concert1 (new horizontal-panel% [parent vert_panel]))
(new button% [parent concert1]
     [label "Concert 1"])
(new button% [parent concert1]
     [label "Edit"]
     [callback (λ (button event) (open-concert-window "Concert 1"))])

;; Concert 2
(define concert2 (new horizontal-panel% [parent vert_panel]))
(new button% [parent concert2]
     [label "Concert 2"])
(new button% [parent concert2]
     [label "Edit"]
     [callback (λ (button event) (open-concert-window "Concert 2"))])

(new message% [parent vert_panel] [label "12/02"])

;; Concert 3
(define concert3 (new horizontal-panel% [parent vert_panel]))
(new button% [parent concert3]
     [label "Concert 3"])
(new button% [parent concert3]
     [label "Edit"]
     [callback (λ (button event) (open-concert-window "Concert 3"))])

;; Concert 4
(define concert4 (new horizontal-panel% [parent vert_panel]))
(new button% [parent concert4]
     [label "Concert 4"])
(new button% [parent concert4]
     [label "Edit"]
     [callback (λ (button event) (open-concert-window "Concert 4"))])

;; Concert 5
(define concert5 (new horizontal-panel% [parent vert_panel]))
(new button% [parent concert5]
     [label "Concert 5"])
(new button% [parent concert5]
     [label "Edit"]
     [callback (λ (button event) (open-concert-window "Concert 5"))])

(new button% [parent window][label "Add New"]
 	[callback (λ (button button-event)
             	(send window1 show #t)
             	(send window show #f))])

;; New Listing window (window1)
(define window1 (new frame%
                        [label "New Listing"]
                        [width 400]
                        [height 650]))

(define vert_panel5 (new vertical-panel% [parent window1] [alignment '(center bottom)]))
(define hori_panel5 (new horizontal-panel% [parent vert_panel] [alignment '(center bottom)]))

(define venue_listing (new text-field%
                      [label "Venue :"]
                      [parent window1]
                      [init-value ""]))

(define date_box (new text-field%
                      [label "Date :"]
                      [parent window1]
                      [init-value "dd/mm/yyyy"]))

(define new_panel (new horizontal-panel%
                       [parent window1]))

(define time1 (new text-field%
                      [parent new_panel]
                      [label "Time :"]
                      [init-value "             xx : xx"]
                      [min-width 10]))

(define time2 (new text-field%
                      [parent new_panel]
                      [label "to"]
                      [init-value "             xx : xx"]
                      [min-width 10]))

(define ticket-price-field
  (new text-field%
       [parent window1]
       [label "Ticket Price : £"]
       [init-value ""]
       [callback
        (lambda (field event)
          (let ([input (send field get-value)])
            (when (not (regexp-match? #rx"^[0-9]*\\.?[0-9]*$" input))
              (send field set-value "")
              (message-box "Error" "Please enter a valid number!" window1 'ok))))]))

(define plus_minus (new horizontal-panel%
                      [parent window1]))
(new button% [parent plus_minus]
     [label "+"])
(new button% [parent plus_minus]
     [label "-"])

(define vert_panel2 (new vertical-panel% [parent window1] [alignment '(center bottom)]))
(define hori_panel2 (new horizontal-panel% [parent vert_panel] [alignment '(center bottom)]))

(define save_listing (new horizontal-panel%
                      [parent window1]))
(new button% [parent vert_panel2]
     [label "Save"])

(define vertical2_panel (new vertical-panel% [parent window1] [alignment '(left center)]))

(new message% [parent vertical2_panel] [label "Max:  1300"])

(new message% [parent vertical2_panel] [label "People:  1230"])

(new message% [parent vertical2_panel] [label "Total Revenue:  12.3K"])

(define panel (new horizontal-panel% [parent window1]))

(new message%
     [label "Automatically stop when max people booked?"]
     [parent panel])

(define check-box
  (new check-box%
       [parent panel]
       [label ""]
       [value #f]))

(new button% [parent window1][label "Cancel"]
 	[callback (λ (button button-event)
             	(send window show #t)
             	(send window1 show #f))])
;===========================================================================================================================================================================
;; START OF EDUARD'S SECTION

;; R3.1

; Making a new frame for the sign up page for Fans Main Menu
(define fan_menu (new frame% [label "Search"] [width 400][height 650]))

; Panels
(define f_menu_v_panel (new vertical-panel% [parent fan_menu] [alignment '(center top)])) 
(define f_menu_h_panel (new horizontal-panel% [parent f_menu_v_panel] [alignment '(center top)]))
(define error_panel (new vertical-panel% [parent fan_menu] [alignment '(center top)]))
(define bottom_panel (new horizontal-panel% [parent fan_menu] [alignment '(center bottom)])) ; Used later in R3.3

; Error messages
(define error-message-1 (new message% [parent error_panel] [label "Enter a concert please"])) (send error-message-1 show #f) ; An error message for not entering anything into the searchbar
(define error-message-2 (new message% [parent error_panel] [label "No concerts by that name"])) (send error-message-2 show #f) ; An error message for not entering any available concerts
(define saved-message-1 (new message% [parent error_panel] [label "Event saved"])) (send saved-message-1 show #f) ; A message which is shown when the user saves a concert
(define unsaved-message-1 (new message% [parent error_panel] [label "Event removed from saved"])) (send unsaved-message-1 show #f) ; A message which is shown when the user saves a concert

; Search bar
(define concert-search-bar (new text-field% [parent f_menu_h_panel] [label "Search Concerts"])) 

(define event-searched event1)

; Search button
(new button% [parent f_menu_h_panel] [label "Search"]
     [callback (λ (button button-event)
                 (define user-input (send concert-search-bar get-value)) ; Getting the user input
                 (printf "User searched for: ~a\n" user-input) ; Used for testing purposes
                 (send concert-1-box-panel show #f) 
                 ; Start of cond
                 (cond
                   ; If the user has not typed anything then send an error message
                   [(>= 0 (string-length user-input)) ; Checking if the user has typed anything
                    (thread (λ () ; Using thread to allow me to make a timed error message
                              (send error-message-1 show #t)
                              (sleep 3)
                              (send error-message-1 show #f)))]
                   ; If the user has typed the correct input then display the concert
                   [(ormap (λ (lst) (displayln (events-band lst)) ; displayln used for testing purposes
                           (equal? (events-band lst) user-input)) event-list)  ; Checking if the user has typed any available concerts
                    (cond
                      [(equal? user-input "QUEEN") (send concert-1-box-panel show #t)]
                      [else (set! event-searched event2)])]
                   ; Else send an error message
                   [else (thread (λ () ; Using thread to allow me to make a timed error message
                              (send error-message-2 show #t)
                              (sleep 3)
                              (send error-message-2 show #f)))])
                 )])

; Concert boxs
(define concert-1-box-panel (new group-box-panel% [parent f_menu_v_panel] [label "Concert 1"])) (send concert-1-box-panel show #f)

(define concert-1-box-layout (new horizontal-panel% [parent concert-1-box-panel] [alignment '(left top)]))

(define concert-1-message (new message% [parent concert-1-box-layout]
                               [label (string-append
                                       "Band/Artist: " (events-band event-searched)
                                       "\nDate: " (events-date event-searched)
                                       "\nLocation: " (events-location event-searched)
                                       "\nCity: " (events-city event-searched)
                                       "\nCost: " (events-cost event-searched))]))

; Filter page
(define filter_page (new frame% [label "Filters"] [width 400][height 650]))

; Filter button
(new button% [parent f_menu_h_panel] [label "Filters"]
     [callback (λ (button button-event)
                 (send filter_page show #t)
                 (send fan_menu show #f))])

; All the filters
(define date (new text-field% [parent filter_page] [label "Date"] [init-value "DD/MM/YYYY"]))
(define postcode (new text-field% [parent filter_page] [label "Postcode"]))
(define band (new text-field% [parent filter_page] [label "Band name"]))
(define price-range (new slider% [parent filter_page] [label "Price range"] [min-value 0] [max-value 500]))
(define genre (new list-box% [parent (new horizontal-panel% [parent filter_page] [style (list 'border)])] [label "Genre"]
                   [choices (list "Rock" "Metal" "Pop" "Hip-Hop" "Rap")] [style (list 'single)] ))

; Done button for filters
(new button% [parent filter_page] [label "Done"]
     [callback (λ (button button-event)
                 (send filter_page show #f)
                 (send fan_menu show #t))])

; Bottom bar buttons
(new button% [parent bottom_panel] [label "Home"] [enabled #f])
(new button% [parent bottom_panel] [label "Saved"]
     [callback (λ (button button-event)
                 (send fan_menu show #f)
                 (send saved_menu show #t)
                 (λ () (display-saved-events)) )])

;===========================================================================================================================================================================

;; R3.2

; Save button
(define concert-1-save-button (new button% [parent concert-1-box-layout] [label "Save"]
                              [callback (λ (button button-event)
                                          (thread (λ () ; Using thread to allow me to make a timed error message
                                                    (send saved-message-1 show #t); Shows message
                                                    (sleep 3)
                                                    (send saved-message-1 show #f)))
                                          (set! saved-events (cons event1 saved-events)) ; Saves the the event to the list
                                          (send concert-1-save-button show #f) ; Disables the save button
                                          (send concert-1-unsave-button show #t) ; Enabled unsave button
                                          (map (λ (x) (displayln (string-append "Current events in saved events:" (events-band x)))) saved-events) ; Testing purposes
                                          )]))

;===========================================================================================================================================================================

;; R3.3

(define saved_menu (new frame% [label "Saved"] [width 400][height 650]))

; Panels
(define s_menu_v_panel (new vertical-panel% [parent saved_menu] [alignment '(center top)])) 
(define s_menu_h_panel (new horizontal-panel% [parent s_menu_v_panel] [alignment '(center top)]))
(define s_bottom_panel (new horizontal-panel% [parent saved_menu] [alignment '(center bottom)]))

; Concert boxs
(define s_concert-1-box-panel (new group-box-panel% [parent s_menu_v_panel] [label "Concert 1"]))

(define s_concert-1-box-layout (new horizontal-panel% [parent s_concert-1-box-panel] [alignment '(left top)]))

(define s_concert-1-message (new message% [parent s_concert-1-box-layout]
                               [label (string-append
                                       "Band/Artist: " (events-band event1)
                                       "\nDate: " (events-date event1)
                                       "\nLocation: " (events-location event1)
                                       "\nCity: " (events-city event1)
                                       "\nCost: " (events-cost event1))]))


; COMPLETELY messed up
(define display-saved-events (for-each (λ (event)
                                         (displayln (string-append "Checking event: " (events-band event)))
                                         (cond
                                           [(equal? (events-band event) "QUEEN") (send s_concert-1-box-panel show #t)]
                                           [(equal? (events-band event) "AC/DC") (send s_concert-1-box-panel show #t)]
                                           [else (send s_concert-1-box-panel show #f)]))
                                       saved-events))

; Bottom bar buttons
(new button% [parent s_bottom_panel] [label "Home"]
     [callback (λ (button button-event)
                 (send fan_menu show #t)
                 (send saved_menu show #f))])
(new button% [parent s_bottom_panel] [label "Saved"] [enabled #f])

;===========================================================================================================================================================================

;; R3.4 Partly

; Unsave button
(define concert-1-unsave-button (new button% [parent concert-1-box-layout] [label "Unsave"] 
                              [callback (λ (button button-event)
                                          (thread (λ () ; Using thread to allow me to make a timed error message
                                                    (send unsaved-message-1 show #t); Shows message
                                                    (sleep 3)
                                                    (send unsaved-message-1 show #f)))
                                          (set! saved-events (remove event1 saved-events))
                                          (send concert-1-save-button show #t) ; Enabled the save button
                                          (send concert-1-unsave-button show #f) ; Disables unsave button
                                          (map (λ (x) (displayln (string-append "Current events in saved events:" (events-band x)))) saved-events) ; Testing purposes)]
                              )])) (send concert-1-unsave-button show #f)

(send frame show #t) ; Displays the GUI