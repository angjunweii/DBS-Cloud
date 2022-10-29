#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        rates = float(request.form.get("rates"))
        regression=joblib.load("regression.joblib")
        tree=joblib.load("tree.joblib")
        r1=regression.predict([[rates]])
        r2=tree.predict([[rates]])
        return render_template("index.html",result1=r1,result2=r2)
    else:
        return render_template("index.html",result1="waiting",result2="waiting")


# In[5]:


if __name__ == "__main__":
    app.run()


# In[ ]:




