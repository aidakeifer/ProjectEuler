#!/usr/bin/env racket
#lang racket

(define (last l)
  (cond ((null? (cdr l)) (car l))
        (else (last (cdr l)))))


(define (factor num)
  (define (_factor num divisor factors)
    (let-values ([(q r) (quotient/remainder num divisor)])
      (when (eq? r 0)
        (set! num q)
        (set! factors (append factors (list (number->string divisor))))
        (set! divisor 1)
      )
      (if (eq? num 1)
        factors
        (_factor num (+ divisor 1) factors)
      )
    )
  )
  (_factor num 2 '())
)


(define all-factors (make-parameter #f))

(define number-to-factor
  (command-line
    #:program "Prime factorizer"
    #:once-each
    [("-a" "--all") "List all factors, not just largest"
        (all-factors #t)]
    #:args (number)
    (string->number number)
  )
)


(define (do_factoring)
  (define factors (factor  number-to-factor))
  (if (all-factors)
    (string-join factors ", " #:after-last "")
    (last factors)
  )
)

(displayln (do_factoring))
