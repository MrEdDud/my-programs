#lang racket

(struct player (name level experience) #:mutable ) ; A struct which is mutable

(define player1 (player "merlin" 1 100)) ; Player 1
(define player2 (player "steve" 100 5000)) ; Player 2
(define player-list (list player1 player2)) ; A list of all the CURRENT players

(define add-player (λ (lst name level experience) ; Function which adds a new player to player list
  (append lst (list (player name level experience))))) ; Appends the details given to the list

(set! player-list (add-player player-list "newbie" 10 250)) ; Sets the player list to have one more player
(display player-list) ; 'Displays' the list