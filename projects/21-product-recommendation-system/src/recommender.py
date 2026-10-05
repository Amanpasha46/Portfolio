import argparse
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


def prepare(path):
    df = pd.read_csv(path)
    required = {"customer_id", "product_id", "quantity"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.dropna(subset=["customer_id", "product_id"])
    return df[df["quantity"] > 0].copy()


def recommend(df, k=5):
    customers = pd.Index(df.customer_id.unique())
    products = pd.Index(df.product_id.unique())
    ci = {v:i for i,v in enumerate(customers)}
    pi = {v:i for i,v in enumerate(products)}
    rows = df.customer_id.map(ci).to_numpy()
    cols = df.product_id.map(pi).to_numpy()
    mat = csr_matrix((np.ones(len(df)), (rows, cols)), shape=(len(customers), len(products)))
    similarity = cosine_similarity(mat.T, dense_output=False)
    result = {}
    for customer, row_id in ci.items():
        scores = np.asarray((mat[row_id] @ similarity).toarray()).ravel()
        scores[mat[row_id].indices] = -np.inf
        top = np.argsort(-scores)[:k]
        result[customer] = products[top].tolist()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()
    df = prepare(args.input)
    recs = recommend(df, args.k)
    out = pd.DataFrame([(c,p,r) for c,items in recs.items() for r,p in enumerate(items,1)], columns=["customer_id","product_id","rank"])
    out.to_csv("recommendations.csv", index=False)
    print(f"Generated {len(out)} recommendations")


if __name__ == "__main__":
    main()
