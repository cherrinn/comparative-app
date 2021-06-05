# Comparative app
## Live demo
https://comparative-app.herokuapp.com/


## Screenshot
### machine learning options
![classifiers](https://user-images.githubusercontent.com/85073127/120878939-f72e7180-c5e9-11eb-8875-acad78fe8702.png)

### selected machine learning
![selected-classifiers](https://user-images.githubusercontent.com/85073127/120878949-11684f80-c5ea-11eb-830c-565c07289e77.png)

### compare result
![compare-result](https://user-images.githubusercontent.com/85073127/120878955-1b8a4e00-c5ea-11eb-88f0-92211585736e.png)

### sample app works
![comparative-sample](https://user-images.githubusercontent.com/85073127/120879149-88521800-c5eb-11eb-8f21-4bbdb5327bc2.gif)

## Prerequisities
Before you begin, ensure you have met the following requirements:

You have a Windows/Linux/Mac machine running Python 3.6+.\
You have installed the latest versions of pip ``
pip install pip ``
and Anaconda ``
https://www.anaconda.com/products/individual#Downloads.
``

## Installation
To install the dependencies, you can simply follow this steps.

#### 1. clone this repositories
Using HTTPS:
```
git clone https://github.com/cherrinn/comparative-app.git
```
Other Options: SSH, GitHub CLI

#### 2. inside root folder you can type this Anaconda command
```
pip install pandas
pip install plotly
pip install scikit-learn
pip install streamlit
```
## Start the project:
```
streamlit run app.py
```
Runs the app in the development mode.
Open http://localhost:8501 to view it in the browser.

## How to Deploy Streamlit Apps to Heroku. (Option)
you need to have Account of Heroku and Github.
1. git clone https://github.com/cherrinn/comparative-app.git
2. git add .
4. git commit -m "Initial commit"
5. heroku login
6. heroku create --appname--
7. heroku git:remote -a --appname--
8. git push heroku master
9. run app with https://appname.herokuapp.com/ **(appname from step 6)**
