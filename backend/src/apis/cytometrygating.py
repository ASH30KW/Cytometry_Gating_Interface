import io
import base64
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
import matplotlib.pyplot as plt
from flask import make_response
from PIL import Image as pil_image
from itertools import permutations
from sklearn.cluster import KMeans
from sklearn.cluster import Birch
from sklearn.decomposition import PCA
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from cp_utils.auth import withTokenOnly, authorizations
from flask_restx import Namespace, Resource, fields, abort
from sklearn.cluster import MeanShift

api = Namespace('cytometrygating', description='', authorizations=authorizations)
Imgs_Type = api.model("Imgs_Type", {
    "ImgsType": fields.String(required=True, description="The Type of Imgs"),
})
Seg_Feature = api.model("Seg_Feature", {
    "Feature": fields.String(required=True, description="The Feature of SegData"),
    "xlabel": fields.String(required=True, description="The label of x"),
    "ylabel": fields.String(required=True, description="The label of y"),
})
MyModel = api.model("MyModel", {
    "PointsIndex": fields.List(fields.Integer(description="Point"))
})

############################################################################
###########Cytometry Gating Web Interface undergraduate thesis##############
############################################################################

###############################Manual Gating################################
@api.route('/Imgs/<ImgsType>/<int:id>')
class CytometryImgs(Resource):
    def get(self, ImgsType, id):
        if(ImgsType=="lym"):
            result = self.img(ImgsType, id)
            return result
        elif(ImgsType=="eos"):
            result = self.img(ImgsType, id)
            return result
        elif(ImgsType=="mon"):
            result = self.img(ImgsType, id)
            return result        
        elif(ImgsType=="neu"):
            result = self.img(ImgsType, id)
            return result     
    def img(self, ImgsType, id):
        tmpfile = io.BytesIO()
        fig = plt.figure(frameon=False)
        imgs_files = Path(__file__).parents[1] /"cgwi"/"imgs"
        img = np.asarray(pil_image.open(imgs_files/f"{ImgsType}"/f'gradient_{id}.png'))
        plt.imshow(img)
        plt.axis('off')
        fig.savefig(tmpfile, format='png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        output = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return output  
    
@api.route('/ClusterImg/<int:id>')
class CytometryClusterImgs(Resource):
    def get(self,id):
        tmpfile = io.BytesIO()
        fig = plt.figure(frameon=False)
        imgs_files = Path(__file__).parents[1] /"cgwi"/"clusterimgs"
        img = np.asarray(pil_image.open(imgs_files/f'gradient_{id}.png'))
        plt.imshow(img)
        plt.axis('off')
        fig.savefig(tmpfile, format='png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        output = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return output     
    
@api.route('/Features')
class SegData(Resource):
    def get(self):
        seg_path = Path(__file__).parents[1] /"cgwi"/"csv"/"data.csv"
        data = pd.read_csv(seg_path)
        result = make_response(data.to_json())
        result.headers["Content-Type"] = "application/json"
        return result

@api.route('/NewData')
class NewData(Resource):
    def post(self):
        points = api.payload["PointsIndex"]
        seg_path = Path(__file__).parents[1] /"cgwi"/"csv"/"data.csv"
        data = pd.read_csv(seg_path)
        A = range(448)
        t = np.array(list(filter(lambda x: x not in points, A)))
        for i in t:
            data[data["sequence"]==i] = np.nan
        r = make_response(data.to_json())
        r.headers["Content-Type"] = "application/json"
        return r        

################################Machine Learning supported Gating Gating################################
@api.route('/Cluster/<Feature>/<xlabel>/<ylabel>')
class Cluster(Resource):
    def get(self, Feature, xlabel, ylabel):
        file_path = Path(__file__).parents[1] / "cgwi"/"csv"
        labels = pd.read_csv(file_path/'labels.csv')
        le = LabelEncoder()
        labels_true = le.fit_transform(labels['label'])
        clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred, preprocessed_data = Cluster.switch(self, Feature, xlabel, ylabel)
        d = {
        'col0x':clustered0x,
        'col0y':clustered0y,
        'col1x':clustered1x,
        'col1y':clustered1y,
        'col2x':clustered2x,
        'col2y':clustered2y,
        'col3x':clustered3x,
        'col3y':clustered3y,
        'ENC': pd.Series(4),
        'Accuracy':pd.Series(self.accuracy(labels_true, labels_pred)),
        'Homogeneity': pd.Series(metrics.homogeneity_score(labels_true, labels_pred)),
        'V_measure': pd.Series(metrics.v_measure_score(labels_true, labels_pred)),
        'Adjusted_Rand_Index':  pd.Series(metrics.adjusted_rand_score(labels_true, labels_pred)),
        'Adjusted_Mutual_Information':  pd.Series(metrics.adjusted_mutual_info_score(labels_true, labels_pred)),
        'Silhouette_Coefficient': pd.Series(metrics.silhouette_score(preprocessed_data, labels_pred, metric='sqeuclidean')),
        }
        df = pd.DataFrame.from_dict(d, orient='index')
        mydf = df.transpose()
        result = make_response(mydf.to_json())
        result.headers["Content-Type"] = "application/json"
        return result

    def switch(self, Feature, idx, idy):
        if(Feature=="kmean"):
            result = Cluster.kmean(self, idx, idy)
            return result
        elif(Feature=="meanshift"):
            result = Cluster.meanshift(self, idx, idy)
            return result
        elif(Feature=="spectral"):
            result = Cluster.spectral(self, idx, idy)
            return result        
        elif(Feature=="agglomerative"):
            result = Cluster.agglomerative(self, idx, idy)
            return result
        elif(Feature=="birch"):
            result = Cluster.birch(self, idx, idy)
            return result
    def kmean(self, idx, idy):
        preprocessed_data = self.readdata()
        n_clusters=4
        km = KMeans(
            n_clusters=n_clusters, init='random',
            n_init=10, max_iter=300, 
            tol=1e-04, random_state=0
        )
        labels_pred_km = km.fit_predict(preprocessed_data)
        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for i in range(448):   
            if labels_pred_km[i] == 0:
                cluster0.append(i)
            elif labels_pred_km[i] == 1:
                cluster1.append(i)
            elif labels_pred_km[i] == 2:
                cluster2.append(i)
            elif labels_pred_km[i] ==3:
                cluster3.append(i)
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)        
        clustered0x = morphs.iloc[cluster0][idx]
        clustered0y = morphs.iloc[cluster0][idy]
        clustered1x = morphs.iloc[cluster1][idx]
        clustered1y = morphs.iloc[cluster1][idy]
        clustered2x = morphs.iloc[cluster2][idx]
        clustered2y = morphs.iloc[cluster2][idy]
        clustered3x = morphs.iloc[cluster3][idx]
        clustered3y = morphs.iloc[cluster3][idy]
        return clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred_km, preprocessed_data
    def meanshift(self, idx, idy):
        preprocessed_data = self.readdata()
        ms = MeanShift(bandwidth=8, n_jobs=-1, bin_seeding=True)
        ms.fit(preprocessed_data)
        labels_pred_ms = ms.labels_
        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for i in range(448):   
            if labels_pred_ms[i] == 0:
                cluster0.append(i)
            elif labels_pred_ms[i] == 1:
                cluster1.append(i)
            elif labels_pred_ms[i] == 2:
                cluster2.append(i)
            elif labels_pred_ms[i] ==3:
                cluster3.append(i)
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)        
        clustered0x = morphs.iloc[cluster0][idx]
        clustered0y = morphs.iloc[cluster0][idy]
        clustered1x = morphs.iloc[cluster1][idx]
        clustered1y = morphs.iloc[cluster1][idy]
        clustered2x = morphs.iloc[cluster2][idx]
        clustered2y = morphs.iloc[cluster2][idy]
        clustered3x = morphs.iloc[cluster3][idx]
        clustered3y = morphs.iloc[cluster3][idy]
        return clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred_ms, preprocessed_data
    def spectral(self, idx, idy):
        preprocessed_data =self.readdata()
        n_clusters = 4
        sc = SpectralClustering(
            affinity='rbf', 
            gamma=.0001,
            n_clusters=n_clusters, assign_labels='kmeans', 
            n_init=10, eigen_tol=1e-04, random_state=0)
        labels_pred_sc = sc.fit_predict(preprocessed_data)
        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for i in range(448):   
            if labels_pred_sc[i] == 0:
                cluster0.append(i)
            elif labels_pred_sc[i] == 1:
                cluster1.append(i)
            elif labels_pred_sc[i] == 2:
                cluster2.append(i)
            elif labels_pred_sc[i] ==3:
                cluster3.append(i)
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)        
        clustered0x = morphs.iloc[cluster0][idx]
        clustered0y = morphs.iloc[cluster0][idy]
        clustered1x = morphs.iloc[cluster1][idx]
        clustered1y = morphs.iloc[cluster1][idy]
        clustered2x = morphs.iloc[cluster2][idx]
        clustered2y = morphs.iloc[cluster2][idy]
        clustered3x = morphs.iloc[cluster3][idx]
        clustered3y = morphs.iloc[cluster3][idy]
        return clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred_sc, preprocessed_data
    def agglomerative(self, idx, idy):
        n_clusters = 4
        agg = AgglomerativeClustering(
            n_clusters=n_clusters, 
        )
        preprocessed_data = self.readdata()
        labels_pred_agg = agg.fit_predict(preprocessed_data) 
        n_clusters = agg.n_clusters_
        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for i in range(448):   
            if labels_pred_agg[i] == 0:
                cluster0.append(i)
            elif labels_pred_agg[i] == 1:
                cluster1.append(i)
            elif labels_pred_agg[i] == 2:
                cluster2.append(i)
            elif labels_pred_agg[i] ==3:
                cluster3.append(i)
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)        
        clustered0x = morphs.iloc[cluster0][idx]
        clustered0y = morphs.iloc[cluster0][idy]
        clustered1x = morphs.iloc[cluster1][idx]
        clustered1y = morphs.iloc[cluster1][idy]
        clustered2x = morphs.iloc[cluster2][idx]
        clustered2y = morphs.iloc[cluster2][idy]
        clustered3x = morphs.iloc[cluster3][idx]
        clustered3y = morphs.iloc[cluster3][idy]
        return clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred_agg, preprocessed_data
        
    def birch(self, idx, idy):
        preprocessed_data =self.readdata()
        brc = Birch(n_clusters=4, threshold=0.7, branching_factor=50)
        brc.fit(preprocessed_data)
        labels_pred_birch = brc.predict(preprocessed_data)
        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for i in range(448):   
            if labels_pred_birch[i] == 0:
                cluster0.append(i)
            elif labels_pred_birch[i] == 1:
                cluster1.append(i)
            elif labels_pred_birch[i] == 2:
                cluster2.append(i)
            elif labels_pred_birch[i] ==3:
                cluster3.append(i)
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)        
        clustered0x = morphs.iloc[cluster0][idx]
        clustered0y = morphs.iloc[cluster0][idy]
        clustered1x = morphs.iloc[cluster1][idx]
        clustered1y = morphs.iloc[cluster1][idy]
        clustered2x = morphs.iloc[cluster2][idx]
        clustered2y = morphs.iloc[cluster2][idy]
        clustered3x = morphs.iloc[cluster3][idx]
        clustered3y = morphs.iloc[cluster3][idy]
        return clustered0x, clustered0y, clustered1x, clustered1y,clustered2x, clustered2y, clustered3x, clustered3y, labels_pred_birch, preprocessed_data
    def readdata(self):
        seg_path = Path(__file__).parents[1] / "cgwi"/"csv"/"data.csv"
        morphs = pd.read_csv(seg_path)
        no_Nan_morphs = morphs.dropna()
        scaler = StandardScaler()
        scaler.fit(no_Nan_morphs)
        scaled_data = scaler.transform(no_Nan_morphs)
        use_pca = True
        n_components = 24
        pca = PCA(n_components=min(n_components, len(no_Nan_morphs.columns)))
        if use_pca:
            preprocessed_data = pca.fit_transform(scaled_data)
        else:
            preprocessed_data = scaled_data
        return preprocessed_data

    def accuracy(self,labels_true, labels_pred):
        n_clust = len(np.unique(labels_pred))
        labels_perms = permutations(range(n_clust))
        labels_pred_nonneg = labels_pred[labels_pred >= 0]
        labels_true_nonneg = labels_true[labels_pred >= 0]
        labels_true_clipped =  labels_true_nonneg[labels_true_nonneg < n_clust]
        labels_pred_clipped =  labels_pred_nonneg[labels_true_nonneg < n_clust]
        max_score = 0
        for perm in list(labels_perms):
            tmp_score = sum(np.array(perm)[labels_true_clipped] == labels_pred_clipped)/len(labels_pred_nonneg)
            if tmp_score > max_score:
                max_score = tmp_score
        return max_score
    
############################################################################
###########Cytometry Gating Web Interface undergraduate thesis##############
############################################################################