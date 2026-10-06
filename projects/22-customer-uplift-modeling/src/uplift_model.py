import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def make_demo_data(n=5000, seed=42):
    rng=np.random.default_rng(seed)
    age=rng.integers(18,70,n); orders=rng.poisson(4,n); spend=np.maximum(0,rng.normal(120,70,n)); visits=rng.poisson(6,n)
    treatment=rng.binomial(1,0.5,n)
    baseline=-2.2+0.018*age+0.12*orders+0.002*spend+0.05*visits
    uplift=0.55/(1+np.exp(-0.15*(visits-5)))-0.12
    p=1/(1+np.exp(-(baseline+treatment*uplift)))
    outcome=rng.binomial(1,p)
    return pd.DataFrame({'customer_id':np.arange(1,n+1),'age':age,'orders':orders,'spend':spend,'web_visits':visits,'treatment':treatment,'outcome':outcome})


def fit_uplift(df):
    features=['age','orders','spend','web_visits']
    train,test=train_test_split(df,test_size=.30,random_state=42,stratify=df['treatment'])
    treated=train[train.treatment==1]; control=train[train.treatment==0]
    mt=RandomForestClassifier(n_estimators=250,min_samples_leaf=20,random_state=42,class_weight='balanced').fit(treated[features],treated.outcome)
    mc=RandomForestClassifier(n_estimators=250,min_samples_leaf=20,random_state=42,class_weight='balanced').fit(control[features],control.outcome)
    scored=test[['customer_id','treatment','outcome']+features].copy()
    scored['p_treat']=mt.predict_proba(test[features])[:,1]
    scored['p_control']=mc.predict_proba(test[features])[:,1]
    scored['uplift']=scored.p_treat-scored.p_control
    return scored


def uplift_at_k(scored,fraction=.2):
    k=max(1,int(len(scored)*fraction)); top=scored.sort_values('uplift',ascending=False).head(k)
    return float(top[top.treatment==1].outcome.mean()-top[top.treatment==0].outcome.mean()),k


if __name__=='__main__':
    scored=fit_uplift(make_demo_data()); u,k=uplift_at_k(scored)
    print(f'Top-20% uplift estimate: {u:.4f} across {k} customers')
    print(scored.sort_values('uplift',ascending=False).head(10).to_string(index=False))
