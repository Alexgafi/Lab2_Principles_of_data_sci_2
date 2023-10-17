# -*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
import matplotlib.pyplot as plt

#Part1

#Q1

f1 = open('C:/Users/adfw980/Downloads/passengerData.csv')

f2 = open('C:/Users/adfw980/Downloads/ticketPrices.xlsx')

Passanger_Data = pd.DataFrame(csv.reader(f1))
    
Ticket_Prices = pd.DataFrame(pd.read_excel('C:/Users/adfw980/Downloads/ticketPrices.xlsx'))

#Q2

Passanger_Data.columns = ['Passanger', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'TicketType']

Ticket_Prices['TicketType'] = Ticket_Prices['TicketType'].astype(str)

pd.merge(Passanger_Data, Ticket_Prices, on='TicketType')

#Q3

Passanger_Data['Age'] = pd.to_numeric(Passanger_Data['Age'], errors='coerce')

max_age = Passanger_Data['Age'].max()

print(max_age)

oldest_people = pd.DataFrame(Passanger_Data.sort_values(by='Age', ascending=False))

print(oldest_people['Name'].tolist())

oldest_person = Passanger_Data[Passanger_Data['Age']==Passanger_Data['Age'].max()]
print(oldest_person['Name'])

#Q4

Merged_Frames = pd.merge(Passanger_Data, Ticket_Prices, on='TicketType')

plt.scatter(Merged_Frames['Fare'], Merged_Frames['Age'])
plt.xlabel('Ticket Price')
plt.ylabel('Age')
plt.title('Ticket Price vs Age')
plt.show()

New_Frame = Merged_Frames[ (Merged_Frames['Sex'] == 'female') & (Merged_Frames['Fare'] >= 40) & (Merged_Frames['Age'] > 40) & (Merged_Frames['Age'] < 50) ]

plt.scatter(New_Frame['Age'], New_Frame['Fare'])
plt.xlabel('Age')
plt.ylabel('Ticket Price')
plt.title('Scatter Plot of Women (40-50) with Expensive Tickets')
plt.show()

#Part2

#Q1

f = open('C:/Users/adfw980/Downloads/titanicSurvival_m.csv')

df1 = pd.DataFrame(csv.reader(f))

#Q2

missing_values_count = df1.isnull().sum()
print(missing_values_count)

#Q3

df1.mean()

#Q4

df1.fillna(0)




plt.scatter(df1['Age'], df1['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age and Fare')
plt.show()

#Q5

df1['Age'].fillna(df1['Age'].mean(), inplace = True)
df1['Fare'].fillna(df1['Fare'].mean(), inplace = True)

plt.scatter(df1['Age'], df1['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age and Fare')
plt.show()

#Part3

#Q1
f3 = open('C:/Users/adfw980/Downloads/TB_burden_countries_2014-09-29 (4).csv')

df2 = pd.DataFrame(csv.reader(f3))
df2.fillna(0)

#Q2

plt.hist(df2[6], bins=10)
plt.hist(df2[8], bins=10)
plt.hist(df2[6], bins=20)
plt.xlabel('e_pop_num')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

plt.hist(df2[9], bins=10)
plt.xlabel('e_prev_100k_hi')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

#Q3

df2[9] = np.log10(df2[9])
plt.hist(df2[9], bins=10)
plt.xlabel('e_prev_100k_hi')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
