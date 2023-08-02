(define (duplicate lst)
    (if (null? lst)
    lst
    (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
)

(display (duplicate (list 1 2 3)))
