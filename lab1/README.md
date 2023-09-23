Целью данной лабораторной работы являлось написание скрипта,
при запуске которого будет генерироваться .smt файл и запускаться 
smt-solver, который в свою очередь будет проверять композицию на разрешаемость.<br/>
*Например*<br/>
Входные данные:<br/>
ab -> bc<br/>
ba -> fc<br/>
ac -> fb<br/>

Результат, полученный от smt-solver следующий:<br/>
sat<br/>
(<br/>
  (define-fun a1a () Int<br/>
    12)<br/>
  (define-fun b2a () Int<br/>
    2)<br/>
  (define-fun b2b () Int<br/>
    15)<br/>
  (define-fun a2f () Int<br/>
    9)<br/>
  (define-fun b2f () Int<br/>
    0)<br/>
  (define-fun b1f () Int<br/>
    0)<br/>
  (define-fun a1c () Int<br/>
    4)<br/>
  (define-fun b1a () Int<br/>
    15)<br/>
  (define-fun a2a () Int<br/>
    9)<br/>
  (define-fun b1c () Int<br/>
    6)<br/>
  (define-fun a1b () Int<br/>
    4)<br/>
  (define-fun b2c () Int<br/>
    15)<br/>
  (define-fun a2c () Int<br/>
    13)<br/>
  (define-fun b1b () Int<br/>
    6)<br/>
  (define-fun a1f () Int<br/>
    13)<br/>
  (define-fun a2b () Int<br/>
    12)<br/>
)<br/><br/>
sat в начале ответа solver'а означает разрешимость, а далее приведены числовые коэффиценты.

