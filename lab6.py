def getIncomeTax(salary):
  """Calculates the income tax for a given salary in the UK.

  Args:
    salary: The salary to calculate the income tax for an employee.

  Returns:
    The income tax amount.
  """

  # Calculate the income tax based on the simple tax calculation rules.
  personal_allowance = 11850
  basic_rate_tax_rate = 0.2
  higher_rate_tax_rate = 0.4
  additional_rate_tax_rate = 0.45

  taxable_income = salary - personal_allowance
  basic_rate_tax = min(taxable_income, 34500) * basic_rate_tax_rate
  higher_rate_tax = max(0, min(taxable_income - 34500, 150000)) * higher_rate_tax_rate
  additional_rate_tax = max(0, taxable_income - 150000) * additional_rate_tax_rate

  # Calculate the total income tax.
  total_income_tax = basic_rate_tax + higher_rate_tax + additional_rate_tax

  return total_income_tax


# Test the function with different salaries.
print(getIncomeTax(28000)) 
