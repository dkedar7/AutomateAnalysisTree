import numpy as np
import pandas as pd

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import f_classif
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold



def VarianceThreshold(feature_matrix,threshold = 0.8):
    selector = VarianceThreshold(threshold=(threshold * (1 - threshold))).fit(feature_matrix)
    return selector


def selectKbest(feature_matrix,label_vector):
    selector = SelectKBest(f_classif, k=80).fit(feature_matrix, label_vector)
    return selector


def RecursiveFeatureElimination(feature_matrix,label_vector,n_feat,kernel="rbf"):
    svc = SVC(kernel=kernel, C=1)
    selector = RFE(estimator = svc, n_features_to_select=n_feat, step=1).fit(feature_matrix, label_vector)
    return selector


def PrincipalComponents(feature_matrix):
    selector = PCA().fit(feature_matrix)
    return selector
