# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:51:31 2023

@author: phamh
"""




import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

#Read 4 Excel sheets with Actual and Predicted
df_all = pd.read_excel("Actual and Predicted - clean.xlsx", 0, header= 0)
df_50 = pd.read_excel("Actual and Predicted - clean.xlsx", 1, header= 0)
df_75 = pd.read_excel("Actual and Predicted - clean.xlsx", 2, header= 0)
df_100 = pd.read_excel("Actual and Predicted - clean.xlsx", 3, header= 0)



#Confusion matrix for All timeframes

#Separate dataframe into classes
hand_shake_class = df_all[df_all["Actual"] == 1]
high_five_class = df_all[df_all["Actual"] == 2]
hug_class = df_all[df_all["Actual"] == 3]
fist_bump_class = df_all[df_all["Actual"] == 4]
shoulder_tap_class = df_all[df_all["Actual"] == 5]
arm_touch_class = df_all[df_all["Actual"] == 6]
elbow_bump_class = df_all[df_all["Actual"] == 7]
hold_hands_class = df_all[df_all["Actual"] == 8]

#Create and print confusion matrix without Heat Map for All timeframes
confusion_matrix = pd.crosstab(df_all['Actual'], df_all['Predicted'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)

#Create and print confusion matrix with Heat Map for All timeframes
ax2 = sns.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g')
ax2.set_title('Haptic Greetings Confusion Matrix');
ax2.set_xlabel('\nPredicted Greeting');
ax2.set_ylabel('Actual Greeting ');

## Ticket labels - List must be in alphabetical order
ax2.xaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
ax2.yaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
## Display the visualization of the Confusion Matrix.
plt.show()


#Create Actual and Predicted lists from dataframe 
actual_list_all = list(df_all['Actual'])
predicted_list_all = list(df_all['Predicted'])
#print(df_all)

#Classification Report


classification_report_all = classification_report(actual_list_all, predicted_list_all)
print(classification_report_all)
print(accuracy_score(actual_list_all, predicted_list_all))





#Confusion matrix for 50% timeframes

#Separate dataframe into classes
hand_shake_class = df_50[df_50["Actual"] == 1]
high_five_class = df_50[df_50["Actual"] == 2]
hug_class = df_50[df_50["Actual"] == 3]
fist_bump_class = df_50[df_50["Actual"] == 4]
shoulder_tap_class = df_50[df_50["Actual"] == 5]
arm_touch_class = df_50[df_50["Actual"] == 6]
elbow_bump_class = df_50[df_50["Actual"] == 7]
hold_hands_class = df_50[df_50["Actual"] == 8]

#Create and print confusion matrix without Heat Map for 50% timeframes
confusion_matrix = pd.crosstab(df_50['Actual'], df_50['Predicted'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)

#Create and print confusion matrix with Heat Map for 50% timeframes
ax2 = sns.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g')
ax2.set_title('Haptic Greetings Confusion Matrix');
ax2.set_xlabel('\nPredicted Greeting');
ax2.set_ylabel('Actual Greeting ');

## Ticket labels - List must be in alphabetical order
ax2.xaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
ax2.yaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
## Display the visualization of the Confusion Matrix.

plt.show()


#Create Actual and Predicted lists from dataframe
actual_list_50 = list(df_50['Actual'])
predicted_list_50 = list(df_50['Predicted'])
#print(df_50)

#Classification Report
print(classification_report(actual_list_50, predicted_list_50))
print(accuracy_score(actual_list_50, predicted_list_50))








#Confusion Matrix for 75% timeframes

#Separate dataframe into classes
hand_shake_class = df_75[df_75["Actual"] == 1]
high_five_class = df_75[df_75["Actual"] == 2]
hug_class = df_75[df_75["Actual"] == 3]
fist_bump_class = df_75[df_75["Actual"] == 4]
shoulder_tap_class = df_75[df_75["Actual"] == 5]
arm_touch_class = df_75[df_75["Actual"] == 6]
elbow_bump_class = df_75[df_75["Actual"] == 7]
hold_hands_class = df_75[df_75["Actual"] == 8]




#Create and print confusion matrix without Heat Map for 75% timeframes
confusion_matrix = pd.crosstab(df_75['Actual'], df_75['Predicted'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)


#Create and print confusion matrix with Heat Map for 75% timeframes
ax2 = sns.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g')
ax2.set_title('Haptic Greetings Confusion Matrix');
ax2.set_xlabel('\nPredicted Greeting');
ax2.set_ylabel('Actual Greeting ');

## Ticket labels - List must be in alphabetical order
ax2.xaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
ax2.yaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
## Display the visualization of the Confusion Matrix.

plt.show()

#Create Actual and Predicted lists from dataframe
actual_list_75 = list(df_75['Actual'])
predicted_list_75 = list(df_75['Predicted'])
#print(df_75)

#Classification Report
print(classification_report(actual_list_75, predicted_list_75))
print(accuracy_score(actual_list_75, predicted_list_75))





#confusion matrix for 100% timeframes

#Separate dataframe into classes
hand_shake_class_100 = df_100[df_100["Actual"] == 1]
high_five_class_100 = df_100[df_100["Actual"] == 2]
hug_class_100 = df_100[df_100["Actual"] == 3]
fist_bump_class_100 = df_100[df_100["Actual"] == 4]
shoulder_tap_class_100 = df_100[df_100["Actual"] == 5]
arm_touch_class_100 = df_100[df_100["Actual"] == 6]
elbow_bump_class_100 = df_100[df_100["Actual"] == 7]
hold_hands_class_100 = df_100[df_100["Actual"] == 8]


#Create and print confusion matrix without Heat Map for 100% timeframes
confusion_matrix = pd.crosstab(df_100['Actual'], df_100['Predicted'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)

#Create and print confusion matrix with Heat Map for 100% timeframes
ax2 = sns.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g')
ax2.set_title('Haptic Greetings Confusion Matrix');
ax2.set_xlabel('\nPredicted Greeting');
ax2.set_ylabel('Actual Greeting ');

## Ticket labels - List must be in alphabetical order
ax2.xaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
ax2.yaxis.set_ticklabels(['Hand Shake', 'High Five', 'Hug', 'Fist Bump', 'Shoulder Tap ', 'Arm Touch', 'Elbow Bump', 'Hold Hands'], rotation=45)
## Display the visualization of the Confusion Matrix.

plt.show()

#Create Actual and Predicted lists from dataframe
actual_list_100 = list(df_100['Actual'])
predicted_list_100 = list(df_100['Predicted'])
#print(df_100)


#Classification Report
print(classification_report(actual_list_100, predicted_list_100))
print(accuracy_score(actual_list_100, predicted_list_100))


