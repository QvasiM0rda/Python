from get_payments import get_payments
from substract_past_from_cur import substract_past_from_cur
from output import output

current_year_current_month = get_payments('cy_cm.txt')
current_year_past_month = get_payments('cy_pm.txt')
past_year_current_month = get_payments('py_cm.txt')
past_year_past_month = get_payments('py_pm.txt')

current_year = substract_past_from_cur(current_year_current_month, current_year_past_month)
past_year = substract_past_from_cur(current_year_past_month, past_year_past_month)
output(current_year, 'current.txt')
output(past_year, 'past.txt')
