program income_calculator
implicit none
integer :: hours_worked, pay_rate, gross_pay
write(*,*) 'Enter hours worked: '
read(*,*) hours_worked
write(*,*) 'Enter pay rate: '
read(*,*) pay_rate
gross_pay = hours_worked * pay_rate
write(*,*) 'Gross pay: ', gross_pay
end program income_calculator
