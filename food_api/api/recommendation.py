# import pandas as pd
# import os
# from django.conf import settings
# import numpy as np
# from scipy.spatial.distance import pdist, squareform

# # categories List
# def get_all_categories():
#     categories = ['آبگوشت', 'آش', 'استیک', 'اشکنه', 'برانچ', 'بورانی', 'تخم مرغ', 'جوجه کباب', 'خوراک حبوبات', 'خوراک سبزیجات', 'خوراک مرغ',
#                   'خوراک گوشت', 'خورشت', 'دریایی', 'دستورات مکمل', 'دسر', 'سالاد', 'ساندویچ و اسنک', 'سوخاری', 'سوپ', 'سیب زمینی', 'غذای سبک',
#                   'لازانیا', 'نوشیدنی سرد', 'نوشیدنی گرم', 'وعده آزاد', 'پاستا', 'پلو و دمی', 'پیتزا', 'پیش غذا', 'کباب', 'کتلت - شامی', 'کوفته_کبه', 'کوکو', 'کیک', 'گراتن']
#     return categories
# categories= get_all_categories()
# # Load foods Data
# def load_foods_data():

#     # Load DataFrame
#     food_dataCSV = os.path.join(settings.BASE_DIR, 'api', 'food11.csv')

#     data1 = pd.read_csv(food_dataCSV, index_col='recipe_id')

#     # Initialize categories List
#     categories_list = []

#     # Iterate over Rows and Add categories Columns
#     for idx, item in data1.iterrows():
#         categories = item.categories.split('|')
#         for category in categories:
#             c = category.lower()

#             # This is not a category
#             if c == '(no categories listed)':
#                 continue

#             # Check if column 'c' exists
#             if not c in data1.columns:
#                 data1[c] = 0
#                 categories_list.append(c)

#             # Set the Value
#             data1.loc[idx,c] = 1

#     # Sort categories List
#     categories_list = sorted(categories_list)
#     #normalization
#     min_value = data1['calories'].min()
#     max_value = data1['calories'].max()

#     data1['calories'] = (data1['calories'] - min_value) / (max_value - min_value)

#     # Selected Columns of the DataFrame
#     columns = ['title', 'calories'] + categories_list

#     # Select Columns
#     data1 = data1[columns]

#     # Return Final DataFrame
#     return data1
# foods = load_foods_data()

# def load_ratings_data():

#     # Load DataFrame
#     rateCSV = os.path.join(settings.BASE_DIR, 'api', 'rates (1).csv')
#     data=pd.read_csv(rateCSV)

#     # Return Final DataFrame
#     return data

# # Load the Ratings Matrix (Pivot Table)
# def load_ratings_matrix():

#     # Load Ratings DataFrame
#     data = load_ratings_data()

#     # Get Pivot Table
#     matrixrate= pd.pivot_table(data, index='user_id', columns='recipe_id', values='ratings')

#     # Return Pivot Table
#     return matrixrate
# # matrixrate=load_ratings_matrix()

# # def get_similarity_matrix():

# #     # Load foods
# #     foods = load_foods_data()

# #     # calories Similarity
# #     Calory = foods['calories'].to_numpy().reshape(-1, 1)
# #     DistanceCalory = pdist(Calory)
# #     sigma = 10
# #     SimilarityCalory = np.exp(-(DistanceCalory/sigma)**2)
# #     SimilarityCalory = squareform(SimilarityCalory)

# #     # categories Similarity
# #     categor = foods[categories]
# #     DistanceCategor = pdist(categor, metric='cosine')
# #     SimilarityCategory = 1 - DistanceCategor
# #     SimilarityCategory = squareform(SimilarityCategory)

# #     # Total Similarity
# #     WeightCategory = 0.85
# #     weightcalory = 1 - WeightCategory
# #     TotalSimilarity = WeightCategory*SimilarityCategory + weightcalory *SimilarityCalory
# #     sdf = pd.DataFrame(TotalSimilarity, index=foods.index, columns=foods.index)
# #     sdf.fillna(0, inplace=True)
# #     return sdf
# # similaritymatrix=get_similarity_matrix()
# # similaritymatrix

# # import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity

# def content_based_recom(user_id):
#     # matrixrateCSV = os.path.join(settings.BASE_DIR, 'api', 'matrixrate.csv')

#     food_dataCSV = os.path.join(settings.BASE_DIR, 'api', 'food11.csv')

#     # return "testtttttttt"
#     # # Load the necessary data
#     matrixrate=load_ratings_matrix()
#     # matrixrate = pd.read_csv(matrixrateCSV)
#     # print(matrixrate)
#     food_data = pd.read_csv(food_dataCSV)

#     # # Filter matrixrate and food_data based on user_id
#     user_ratings = matrixrate[matrixrate['user_id'] == user_id]

#     print(user_ratings)
#     user_food_ids = user_ratings['recipe_id'].tolist()

#     # Create a subset of food_data based on user_food_ids
#     subset_food_data = food_data[food_data['recipe_id'].isin(user_food_ids)]

#     # Calculate similarity matrix
#     similarity_matrix = cosine_similarity(subset_food_data.iloc[:, 1:])

#     # Get the index of the user's last-rated food
#     last_rated_food_index = user_ratings['recipe_id'].idxmax()

#     # Get the similarity scores for the last rated food
#     similarity_scores = similarity_matrix[last_rated_food_index]

#     # Sort the food indices based on similarity scores
#     sorted_food_indices = similarity_scores.argsort()[::-1]

#     # Get the top N recommended food names
#     top_n = 5
#     recommended_food_names = subset_food_data.iloc[sorted_food_indices[:top_n], 0].tolist()

#     return recommended_food_names

# # Load foods data
# # foods = load_foods_data()

# # # Load ratings matrix
# # matrixrate = load_ratings_matrix()

# # # Get similarity matrix
# # similaritymatrix = get_similarity_matrix()

import pandas as pd
import numpy as np
import os
from django.conf import settings
from scipy.spatial.distance import pdist,squareform
# categories List
categories=['آبگوشت', 'آش', 'استیک', 'اشکنه', 'برانچ', 'بورانی', 'تخم مرغ', 'جوجه کباب', 'خوراک حبوبات', 'خوراک سبزیجات', 'خوراک مرغ',
                      'خوراک گوشت', 'خورشت', 'دریایی', 'دستورات مکمل', 'دسر', 'سالاد', 'ساندویچ و اسنک', 'سوخاری', 'سوپ', 'سیب زمینی', 'غذای سبک',
                      'لازانیا', 'نوشیدنی سرد', 'نوشیدنی گرم', 'وعده آزاد', 'پاستا', 'پلو و دمی', 'پیتزا', 'پیش غذا', 'کباب', 'کتلت - شامی', 'کوفته_کبه', 'کوکو', 'کیک','گراتن']

# food categories
def get_all_categories():
    return categories

# Load foods Data
def load_foods_data():

    # Load DataFrame
    food_csv = os.path.join(settings.BASE_DIR, 'api', 'food11.csv')
    data1 = pd.read_csv(food_csv, index_col='recipe_id')

    # Initialize categories List
    categories_list = []

    # Iterate over Rows and Add categories Columns
    for idx, item in data1.iterrows():
        categories = item.categories.split('|')
        for category in categories:
            c = category.lower()

            # This is not a category
            if c == '(no categories listed)':
                continue

            # Check if column 'c' exists
            if not c in data1.columns:
                data1[c] = 0
                categories_list.append(c)

            # Set the Value
            data1.loc[idx,c] = 1

    # Sort categories List
    categories_list = sorted(categories_list)

    # Selected Columns of the DataFrame
    columns = ['title', 'calories'] + categories_list

    # Select Columns
    data1 = data1[columns]

    # Return Final DataFrame
    return data1

foods = load_foods_data()
# Load Ratings Data
def load_ratings_data():

    # Load DataFrame
    rate_csv = os.path.join(settings.BASE_DIR, 'api', 'rates (1).csv')
    data=pd.read_csv(rate_csv)

    # Return Final DataFrame
    return data

# Load the Ratings Matrix (Pivot Table)
def load_ratings_matrix():

    # Load Ratings DataFrame
    data = load_ratings_data()

    # Get Pivot Table
    matrixrate= pd.pivot_table(data, index='user_id', columns='recipe_id', values='ratings')

    # Return Pivot Table
    return matrixrate


def get_similarity_matrix():

    # Load foods
    foods = load_foods_data()

    # calories Similarity
    Calory = foods['calories'].to_numpy().reshape(-1, 1)
    DistanceCalory = pdist(Calory)
    sigma = 10
    SimilarityCalory = np.exp(-(DistanceCalory/sigma)**2)
    SimilarityCalory = squareform(SimilarityCalory)

    # categories Similarity
    categor = foods[categories]
    DistanceCategor = pdist(categor, metric='cosine')
    SimilarityCategory = 1 - DistanceCategor
    SimilarityCategory = squareform(SimilarityCategory)

    # Total Similarity
    WeightCategory = 0.85
    weightcalory = 1 - WeightCategory
    TotalSimilarity = WeightCategory*SimilarityCategory + weightcalory *SimilarityCalory
    sdf = pd.DataFrame(TotalSimilarity, index=foods.index, columns=foods.index)
    sdf.fillna(0, inplace=True)
    return sdf



def loader_matrix():
    matrixrate=load_ratings_matrix()

    return matrixrate

# Content-based Recommendation
#recommendation based on total similarity
def content_based_recom(user_id):
    n = 5
    matrixrate=load_ratings_matrix()
    similaritymatrix=get_similarity_matrix()


    # Ratings of the User
    rate = matrixrate.loc[int(user_id)]
    has_rating = rate[rate >= 0].index
    fav_foods = rate[rate == 4].index

    # Calculate Total Similarity
    totalsimilarity = 0
    for i in fav_foods:
        totalsimilarity += similaritymatrix[i]

    # Exclude food with Rating
    totalsimilarity[has_rating] = 0

    # Recommendations
    recommendations1 = totalsimilarity.sort_values(ascending=False).index[:n]
    recommendations1 = recommendations1.to_list()
    return recommendations1

# recommendations1= content_based_recom(user_id=10, matrixrate=matrixrate, similaritymatrix=similaritymatrix, n=3)
# foods.loc[recommendations1]