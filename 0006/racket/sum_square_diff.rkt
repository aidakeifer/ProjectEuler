#lang racket
(define (sum_squares n)
  (define (_sum n sum)
    (if (<= n 0)
      sum
      (_sum (- n 1) (+ sum (* n n)))
    )
  )
  (_sum n 0)
)


(define (square_sums n)
  (define (_sum n sum)
    (if (<= n 0)
      sum
      (_sum (- n 1) (+ sum n))
    )
  )
  (define sum 0)
  (set! sum (_sum n 0))
  (* sum sum)
)


(define count 100)
(- (square_sums count) (sum_squares count))
