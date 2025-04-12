#lang racket

(struct menu-item (dish-name price))
(define spanish (menu-item "Paella" "£20"))
(define italian (menu-item "Pizza" "£25"))
(define french (menu-item "Crossaint" "£5"))
(define german (menu-item "Sausages" "£10"))

(menu-item-dish-name italian)