#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = [
                 'poi',
                # 'to_messages',
                 'salary', 
                # 'deferral_payments',
                # 'total_payments',
                 'exercised_stock_options',
                 'bonus',
                # 'restricted_stock',
                 'shared_receipt_with_poi',
                # 'restricted_stock_deferred',
                 'total_stock_value',
                # 'expenses',
                # 'loan_advances',
                # 'from_messages',
                # 'from_this_person_to_poi',
                # 'director_fees',
                # 'deferred_income',
                # 'long_term_incentive',
                # 'from_poi_to_this_person',
                 'bonus_salary_ratio',
                 'from_this_person_to_poi_percentage'
                ]

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

data_dict.pop("TOTAL")
data_dict.pop("THE TRAVEL AGENCY IN THE PARK")
data_dict.pop("LOCKHART EUGENE E")

### Task 3: Create new feature(s)

# from_this_person_to_poi as a percentage of from_messages
for employee, features in data_dict.iteritems():
    if features['from_this_person_to_poi'] == "NaN" or features['from_messages'] == "NaN":
        features['from_this_person_to_poi_percentage'] = "NaN"
    else:
        features['from_this_person_to_poi_percentage'] = float(features['from_this_person_to_poi']) / float(features['from_messages'])

### bonus_salary_ratio
for employee, features in data_dict.iteritems():
	if features['bonus'] == "NaN" or features['salary'] == "NaN":
		features['bonus_salary_ratio'] = "NaN"
	else:
		features['bonus_salary_ratio'] = float(features['bonus']) / float(features['salary'])

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)



### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline


feature_scaler = MinMaxScaler()
feature_selection = SelectKBest()
dtc = DecisionTreeClassifier()
svc = SVC()
nbc = GaussianNB()

# If svc is used, comment line 100, uncomment line 101, 117, 118 and 119
steps = [ ### 1. Feature Scalling ###
          #('min_max_scalling', feature_scaler),
		  ### 2. Feature Selection ###]
		  ('feature_selection', feature_selection),
		  ### 3. Choose a Classifier ###
		  ('dtc', dtc)
		  #('svc', svc)
		  #('nbc', nbc)
		 ] 
### If other classifer is used, uncomment line 101 or 102 and comment Line 100

pipeline = Pipeline(steps)


### Parameters 
parameters = dict(
                    feature_selection__k=[7], 
                    dtc__criterion=['gini', 'entropy'],
                    dtc__max_depth=[None, 1, 2, 3, 4],
                    dtc__min_samples_split=[1, 2, 3, 4, 25],
                    dtc__class_weight=[None, 'balanced'],
                    dtc__random_state=[42]
                #   svc__C=[0.1, 1, 10, 100, 1000],
                #   svc__kernel=['rbf'],
                #   svc__gamma=[0.001, 0.0001]               
                  )


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split, StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report


### Create Training Sets and Test Sets
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

sss = StratifiedShuffleSplit(labels_train, 
                            n_iter = 20, 
                            test_size = 0.5, 
                            random_state = 42)

gs = GridSearchCV(pipeline, 
                  param_grid = parameters, 
                  scoring = "f1", 
                  cv = sss, 
                  error_score = 0)

gs.fit(features_train, labels_train)

labels_predictions = gs.predict(features_test)

clf = gs.best_estimator_
print "\n", "Best parameters are: ", gs.best_params_, "\n"

features_selected = []
for i in clf.named_steps['feature_selection'].get_support(indices=True):
	features_selected.append(features_list[i+1])

scores = clf.named_steps['feature_selection'].scores_
importances = clf.named_steps['dtc'].feature_importances_
import numpy as np
indices = np.argsort(importances)[::-1]
print 'The ', len(features_selected), " features selected and their importances:"

for i in range(len(features_selected)):
    print "feature no. {}: {} ({}) ({})".format(i+1,features_selected[indices[i]],importances[indices[i]], scores[indices[i]])


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
