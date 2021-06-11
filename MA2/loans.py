# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:38:54 2019

@author: Samgr
"""

def monthly_payment(principal, y_i_rate, num_years):
    mpymt = (y_i_rate * principal) / ( 1 - (1 + y_i_rate)**(-num_years))
    return mpymt 

def remaining_balance(remaining, monthly_payment):
    balance = (remaining - monthly_payment)
    return balance

def calc_monthly_interest(remaining, y_i_rate):
    monthly_interest = float(y_i_rate * remaining) 
    return monthly_interest 

def calc_monthly_principal(principal, monthly_payment, monthly_interest):
    monthly_principal = monthly_payment - monthly_interest
    return monthly_principal

def main():
    
    user_input = input('What is this loan for? ')

    principal = input('Please enter the principal amount for the loan: ') 
    principal = float(principal)
    remaining = principal
    
    y_i_rate = input('Please enter the yearly interest rate (as a percent) for the loan: ') 
    y_i_rate = float(y_i_rate) / 100 / 12
    
    num_years = input('Please enter the number of years for the loan: ')
    num_years = float(num_years) * 12
    
    print("Month", "Balance" , "Principal", "Interest", "Payment")

    for x in range(1, int(num_years + 1)):
    
        monthly_p = monthly_payment(principal, y_i_rate, num_years)
        balance = remaining_balance(remaining, monthly_payment)
        monthly_interest = calc_monthly_interest(remaining, y_i_rate)
        monthly_principal = calc_monthly_principal(principal, monthly_payment, monthly_interest)
        remaining = remaining - principal
        
        print(x,'    ', ' $', remaining_principal, '$', principal, '$', monthly_interest, '$', monthly_p)
    
main()