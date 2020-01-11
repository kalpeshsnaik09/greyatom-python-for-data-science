# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Code starts here

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
loan_status
#plt.bar(loan_status.index,loan_status[])


# --------------
#Code starts here




property_and_loan=data[['Property_Area','Loan_Status']]
property_and_loan=property_and_loan.groupby(['Property_Area','Loan_Status']).size().unstack()
# property_and_loan.plot(kind='bar',stacked=False)
# plt.xlabel('Property Area')
# plt.ylabel('Loan Status')
# plt.xticks(rotation=45)
# plt.show()


# --------------
#Code starts here

education_and_loan=data[['Education','Loan_Status']]

education_and_loan=education_and_loan.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density' ,label='Not Graduate')



#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']


