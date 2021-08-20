import argparse
import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
import gensim
from jvm_embedding import *

scale = 1.0

def similarity(v1, v2):
    #return np.dot(v1, v2)
    return np.linalg.norm(v1 - v2)/scale

def Dimenionality_reduction(model_path, n_components,dim_red):
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=False)
    wv = model.vectors
    mean = np.average(wv,axis=0)
    if dim_red == 1:
        dim_m = PCA(n_components=n_components)
    else:
        dim_m = TruncatedSVD(n_components=n_components)
    
    dim_m.fit(wv - mean)
    components = np.matmul(np.matmul(wv, dim_m.components_.T), dim_m.components_)
    processed_vec = wv - mean - components
    return processed_vec

def compare(processed_vec,test_path,model_path):
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=False)
    model.vectors = processed_vec
    tf_dataset, df, n_methods = build_tf_df(test_path)

    method_embeddings = {}
    for path, method_features in tf_dataset.items():
        method_embeddings[path] = {}
        for  method in method_features.keys():
            feature_dict = method_features[method]
            method_embeddings[path][method] = sum(model[f]*v for f, v in feature_dict.items() if f in model)

    for path1, method_features1 in tf_dataset.items():
        for method1, feature_dict1 in method_features1.items():
            print()
            print(path1, "@", method1, "vs: ")
            res = []
            for path2, method_features2 in tf_dataset.items():
                    for method2, feature_dict2 in method_features2.items():
                        if path1 == path2 and method1 == method2:
                            continue
                        sim = similarity(method_embeddings[path1][method1], method_embeddings[path2][method2])
                        res.append( (path2 + " " + method2, sim))
            res.sort(reverse=False, key=lambda t: t[1])
            for target, sim in res:
                print("    ", target, ":", sim)

    pass

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model_path', nargs='*', help='path of model(s)')
    parser.add_argument('-n', '--n_components', type=int, default=5, help='number of dimensions postprocessing')
    parser.add_argument('-c', '--dim_red', type=int, default=0, help=' Dimenionality Reduction: 0 for TSVD or 1 for PCA')
    parser.add_argument('-t', '--test_path', type=str, help='test_classes')
    args = parser.parse_args()
    for model_path in args.model_path:
        processed_vec = Dimenionality_reduction(model_path,args.n_components,args.dim_red)
        compare(processed_vec,args.test_path,model_path)
if __name__ == '__main__':

    args_parse()