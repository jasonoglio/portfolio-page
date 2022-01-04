
# https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs
# https://www.youtube.com/watch?v=6plVs_ytIH8&t=1114s
# https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688
# https://pythonbasics.org/flask-upload-file/
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# https://www.youtube.com/watch?v=6WruncSoCdI
# https://pythonise.com/series/learning-flask/flask-uploading-files
# https://viveksb007.github.io/2018/04/uploading-processing-downloading-files-in-flask
# https://github.com/viveksb007/camscanner_watermark_remover




from flask import Flask, render_template, request, flash, redirect, make_response


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import kneed
from statistics import mode

app = Flask(__name__)
app.secret_key="neriskasc9245kadfb"

@app.route('/base')
def base():
    return render_template("base.html")

# @ signifies a decorator - way to wrap a function and modifying it's behavior
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kmeans')
def kmeans():
    return render_template("kmeans.html")


# i used this video to make the upload page
# https://www.youtube.com/watch?v=6WruncSoCdI

# with the form code from this page
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

@app.route('/uploads', methods=["GET", "POST"])
def upload():
    global dict_list
    global df
    # i made these global so i can call them into other functions

    if request.method == "POST":
        if request.files:
            #data = request.files["file"]
            df = pd.read_excel(request.files["file"])
            df = pd.DataFrame(df)


            # look at terminal for file data
            #print(data)

            #df = pd.DataFrame(data)
            head = df.head
            print(df.head())

            col_names = list(df)
            index_list = list(range(len(col_names)))
            dict_list = [{'Column': index_list[i], 'Title': col_names[i]} for i in range(len(index_list))]

            return render_template("uploads.html", dict_list=dict_list)


@app.route('/blank')
def blank():
    return render_template("blank.html")



@app.route('/download', methods=["GET", "POST"])
def download():
    # https://stackoverflow.com/questions/64243070/executing-python-script-with-flask-from-button
    # the input button on the html file has 'download as the name that is why it calls this function
    if "download" in request.form:

#        df_drop = df.drop(list(df)[13:], axis=1)
#        df_drop_nan = df_drop.dropna()
#        df_drop_nan = df_drop_nan.drop('obs', 1)
#        total_run_list = []
#        total_run_count = 0
#        while total_run_count < 15:
#            sil_score = 999999
#            elbow_score = 1
#            Sum_of_squared_distances = []
#            test_max = len(df_drop_nan.index) // 6
#            number_of_runs = 0
#            result_runs = 0
#            result_list = []
#            while sil_score != elbow_score:
#                try:
#                    K = range(2, test_max)
#                    for k in K:
#                        km = KMeans(n_clusters=k, max_iter=200, n_init=10)
#                        km = km.fit(df_drop_nan)
#                        score = silhouette_score(df_drop_nan, km.labels_)
#                        Sum_of_squared_distances.append(km.inertia_)
#                    #plt.plot(K, Sum_of_squared_distances, 'bx-')
#                    #plt.xlabel('k')
#                    #plt.ylabel('Sum_of_squared_distances')
#                    #plt.title('Elbow Method For Optimal k')
#                    #plt.show()
#                    kl = kneed.KneeLocator(K, Sum_of_squared_distances, curve='convex', direction='decreasing')
#                    print('Elbow calculation = ')
#                    elbow_score = kl.elbow
#                    print(elbow_score)
#                    silhouette_coefficients = []
#                    for k in K:
#                        km = KMeans(n_clusters=k, max_iter=200, n_init=10)
#                        km = km.fit(df_drop_nan)
#                        score = silhouette_score(df_drop_nan, km.labels_)
#                        # for silhouette score to work range (K here) cannot start at 1
#                        silhouette_coefficients.append(score)
#                    #plt.style.use("fivethirtyeight")
#                    #plt.plot(K, silhouette_coefficients)
#                    #plt.xticks(K)
#                    #plt.xlabel("Number of Clusters")
#                    #plt.ylabel("Silhouette Coefficient")
#                    #plt.show()
#                    print('Silhouette score = ')
#                    sil_score = silhouette_coefficients.index(max(silhouette_coefficients)) + 2
#                    print(sil_score)  # addind 2 because K range starts at
#                    # the line above this gets the index where the item form the list is max
#                    # TO DO:
#                    # can i make a way to run this with different K's until i unify the answer?
#                    k_means_df = pd.DataFrame(Sum_of_squared_distances)
#                    test_max = elbow_score + sil_score
#                    Sum_of_squared_distances = []
#                    silhouette_coefficients = []
#                    number_of_runs += 1
#                except:
#                    print('run failed, resetting initial number of test clusters')
#                    test_max = len(df_drop_nan.index) // 6
#            print('The analysis ran ' + str(number_of_runs) + ' times. The recommended cluster count is ' + str(
#                sil_score))
#            total_run_count += 1
#            total_run_list.append(sil_score)
#        mode_number = mode(total_run_list)
#        print('Final recommended cluster (mode of 15 complete runs) = ' + str(mode_number))
#       km = KMeans(n_clusters=mode_number, max_iter=200, n_init=10)
#        km = km.fit(df_drop_nan)
#        labels = km.predict(df_drop_nan)
#        labels = pd.DataFrame(labels)
#        labels = labels.rename(columns={0: 'labels'})
#        df_drop_nan = df_drop_nan.reset_index(drop=True)
#        df_drop_nan['labels'] = labels['labels']



        # https://stackoverflow.com/questions/38634862/use-flask-to-convert-a-pandas-dataframe-to-csv-and-serve-a-download
        # change df to df_drop_nan while taking off all the comments
        resp = make_response(df.to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp


@app.route('/delete', methods=["GET", "POST"])
def delete_row():
    global df

    if "delete" in request.form:
        print(request.form['delete'])
        drop_num = int(request.form['delete'])
        df = df.drop(list(df)[drop_num], axis=1)

        col_names = list(df)
        index_list = list(range(len(col_names)))
        dict_list = [{'Column': index_list[i], 'Title': col_names[i]} for i in range(len(index_list))]

        return render_template("uploads.html", dict_list=dict_list)


if __name__ == "__main__":
    app.run(debug=True)


