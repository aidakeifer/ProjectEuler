#!/usr/bin/env racket
#lang racket
(define (is_prime num)
  (define (_is_prime num divisor)
    (let-values ([(q r) (quotient/remainder num divisor)])
      (if (eq? r 0)
        (if (eq? q 1)
            #t
            #f
        )
        (_is_prime num (+ divisor 1))
      )
    )
  )
  (_is_prime num 2)
)


(define (nth_prime n)
  (define (_nth_prime n num)
    (when (is_prime num)
      (set! n (- n 1))
    )
    (if (<= n 0)
      num
      (_nth_prime n (+ num 1))
    )
  )
  (_nth_prime n 2)
)


(define which-prime
  (command-line
    #:program "Prime number finder"
    #:args (number)
    (string->number number)
  )
)

(displayln (nth_prime which-prime))
