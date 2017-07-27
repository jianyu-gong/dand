# Identify Fraud from Enron Email
#### Author: Jianyu Gong
#### Date: June 5th, 2017

## Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?
This project aims to identify the fraud from the Enron employees based on the public Enron financial and email dataset. The fraud is considered as a person of interest (POI).
Machine learning is used to accomplish the goal in this case because they can process the datasets much faster than human. Different algorithms can be adjusted and tested to achieve the best result. The background of Enron dataset is shown below:
### Total Number of Data Points
```python
import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print 'The number of dictionary is:', len(enron_data)
```
There are 146 data points in the dataset.
### Allocation across Clasees (POI/Non-POI)
```python
import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
num = 0
for n in enron_data:
	if enron_data[n]['poi'] == 1:
		num += 1
print 'Number of POIs:', num
```
There are 18 POIs and 128 Non-POIs
### Number of Features Used
```python
import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
num = 0
feature_list = []
for n in enron_data['METTS MARK']:
	feature_list.append(n)
print "Total numbers of feature:", len(feature_list)
print feature_list
```
```python
Total numbers of feature: 21
Features are: ['salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 
'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 
'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person']
```
### Features with Missing Values
Only 'poi' feature doesnot have missing values and other 20 features have missing values as "NaN".
### Outliers
```python
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop( 'TOTAL', 0 )
data = featureFormat(data_dict, features)

data_sorted = sorted(data, key=lambda tup: tup[0])

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
```
"salary" and "bonus" are selected as two features to identify the outlier. After ploting the scatter plot, it can be easily find that the biggest Enron outlier is 'TOTAL'. Other financial features are studied as well and the biggest Enron outlier is still 'TOTAL'. After removing 'TOTAL, according to the scatter plot, there are probably four more outliers. However, those four points are kept because two of them are Enron's biggest bosses and they are valid data points.

## What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.
### New Features
- from_this_to_poi_person_percentage
- bonus_salary ratio
'from_this_to_poi_person_percentage' can be calculated by using 'from_this_to_poi_person' dividied by total number of emails sent. It can somehow represent the email activity frequency between POI and this person. Thus, it may be helpful to identify fraud.
'bonus_salary_ratio' can be used to find out the employees with low salaries and high bonuses or with high salaries and low bonuses who may potentially be fraud.
### Feature Scaling
Feature scaling is applied when using support vector machines (SVM) algorithm and naive bayes algorithm but not decision tree algorithm because decision tree algorithm is based on threhold values. Therefore, scaling is not necessary for decision tree algorithm.
### Feature Selection
Decision tree classifier is used and all the parameters are set to be default. The feature importance and feature score are shown below:

#### Decision Tree Algorithm
| Features | Feature Importance | Feature Score |
| :--- | :--: | :--: |
| bonus | 0.06 | 30.72 |
| bonus_salary_ratio | 0.0 | 21.12 |
| salary | 0.07 | 15.86 |
| from_this_person_to_poi_percentage | 0.23 | 15.84 |
| shared_receipt_with_poi | 0.31 | 10.72 |
| total_stock_value | 0.07 | 10.63 |
| exercised_stock_options | 0.11 | 9.68 |
| total_payments | 0.02 | 8.95 |
| deferred_income | 0.0 | 8.79 |
| restricted_stock | 0.15 | 8.06 |
| long_term_incentive | 0.0 | 7.55 |
| loan_advances | 0.0 | 7.03 |
| from_poi_to_this_person | 0.0 | 4.96 |
| expenses | 0.07 | 4.18 |
| to_messages | 0.0 | 2.62 |
| director_fees | 0.0 | 1.64 |
| restricted_stock_deferred | 0.0 | 0.72 |
| from_messages | 0.0 | 0.44 |
| from_this_person_to_poi | 0.0 | 0.11 |
| deferral_payments | 0.0 | 0.01 |



Univariate feature selection process, select k-best, is applied. In order to determine the "k", "k" is tried from "2" to "all". All the parameters of decision tree classifer remain default. Also, the precision score, recall score and accuracy are recorded based on the results from tester.py.

| k | Precision Score | Recall Score | Accuracy |
| :--- | :--: | :--: | :--: |
| 1 | 0.222 | 0.147 | 0.818 |
| 2 | 0.189 | 0.185 | 0.785 |
| 3 | 0.282 | 0.309 | 0.803 |
| 4 | 0.252 | 0.262 | 0.798 |
| 5 | 0.255 | 0.274 | 0.796 |
| 6 | 0.265 | 0.273 | 0.802 |
| 7 | 0.305 | 0.309 | 0.814 |
| 8 | 0.284 | 0.286 | 0.809 |
| 9 | 0.294 | 0.287 | 0.813 |
| 10 | 0.289 | 0.281 | 0.812 |
| 11 | 0.302 | 0.292 | 0.816 |
| 12 | 0.292 | 0.279 | 0.814 |
| 13 | 0.290 | 0.276 | 0.813 |
| 14 | 0.290 | 0.275 | 0.813 |
| 15 | 0.281 | 0.262 | 0.813 |
| 16 | 0.299 | 0.281 | 0.816 |
| 17 | 0.287 | 0.275 | 0.812 |
| 18 | 0.291 | 0.276 | 0.814 |
| 19 | 0.284 | 0.265 | 0.813 |
| 20 | 0.278 | 0.265 | 0.810 | 

![figure_1](https://user-images.githubusercontent.com/25847196/27357592-cb57a9f0-55e0-11e7-8f38-20f60af63129.png)

Based on the table and figure above, it can be found that when k = 7, both recall score and precision score are higher than 0.3. Also, the accuracy is relative high too. Therefore, seven features with the largest 7 feature scores are selected. It is seen that feature score of bonus_salary_ratio and from_this_person_to_poi_percentage are 21.12(2nd) and 15.84(4th) respectively. Thus, the two new features are important features.
Selected features: bonus, bonus_salary_ratio, salary, from_this_person_to_poi_percentage, shared_receipt_with_poi, shared_receipt_with_poi and exercised_stock_options.

## What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms? 
Three algorithms (Naive Bayes Algorithm, SVM Algorithm and Decision Tree Algorithm) are discussed. Afer being evaluated by tester.py, only decision tree algorithm can achieve a precision of 0.35 and a recall of 0.68 which are both above 0.3. Results of all the three algorthm are shown below:

| Features | Precision Score | Recall Score |
| :--- | :--: | :--: |
| Naive Bayes | 0.31 | 0.19 |
| SVM | 0.49 | 0.03 |
| Decision Tree Algorithm | 0.35 | 0.68 |

Therefore, decision tree algorithm is selected to identify the POI.

## What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? What parameters did you tune? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier).
When using a classifier, several parameters can be tuned to achieve a better performance (e.g. higher accuracy, higher precision score and higher recall score). 
Take desicion tree classifier as an example. According to the decision tree classifier documentation, the parameters are listed below:
- criterion: string, optional (default=”gini”)
- splitter : string, optional (default=”best”)
- max_features : int, float, string or None, optional (default=None)
- max_depth : int or None, optional (default=None)
- min_samples_split : int, float, optional (default=2)
- min_samples_leaf : int, float, optional (default=1)
- min_weight_fraction_leaf : float, optional (default=0.)
- max_leaf_nodes : int or None, optional (default=None)
- class_weight : dict, list of dicts, “balanced” or None, optional (default=None)
- random_state : int, RandomState instance or None, optional (default=None)
- min_impurity_split : float, optional (default=1e-7)
- presort : bool, optional (default=False)

Tuning parameters manually can be tons of work therefore GridSearchCV is applied to select optimized parameters based on 'f1' score  in this project automatically. The best paraters are shown below:

- k = 7 (SelectKBest)
- criterion = 'gini'
- max_depth = None
- min_samples_split = 25
- class_weight = 'balanced'
- random_state = 42

Setting proper values for each parameter is challenging too. In some cases, only a few parameter combinations can achieve desirable performance. Therefore, tuning parameters is crucial.
### What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis? 
Validation set is used to check the how well your model has been trained. The validation result can be reflected by accuracy, precision, recall and etc. 
Because the Enron data set is so small, Stratified Shuffle Split cross validation was useful because it essentially created multiple datasets out of a single one to get more accurate results. 
In this project, the sample size is small. Furthermore, the number of POIs are much smaller than that of no-POIs. In order to ensure a equal ratio of POIs:non-POIs in both training and testing set during the validation process, Stratified Shuffle Split cross validation is applied to achieve a better performance.

### Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance. 
In this case, the recall score represents how many POIs are pick out among all the POIs. The precision score represents, among the predicted POIs, how many are true POIs.

| Features | Precision Score | Recall Score |
| :--- | :--: | :--: |
| Naive Bayes | 0.31 | 0.19 |
| SVM | 0.49 | 0.03 |
| Decision Tree Algorithm | 0.35 | 0.68 |

This table has been shown in previous section. In this project, it is aimed to find out all the POIs. Therefore, the recall score which represents the how many POIs are picked out is important. The decision tree classifier has the highest recall score among those three. Therefore, decision tree algorithm is the final choice.
