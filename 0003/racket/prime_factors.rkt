#lang racket
(define (last l)
  (cond ((null? (cdr l)) (car l))
        (else (last (cdr l)))))


(define (factor num)
  (define (_factor num divisor factors)
    (let-values ([(q r) (quotient/remainder num divisor)])
      (when (eq? r 0)
        (set! num q)
        (set! factors (append factors (list divisor)))
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


(last (factor  600851475143))
