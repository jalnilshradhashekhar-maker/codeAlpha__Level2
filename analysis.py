import pandas as pd

df = pd.read_csv("Dataset .csv")

print("LEVEL 2 DATA ANALYSIS")
print("=" * 50)

rating_bins = pd.cut(df["Aggregate rating"], bins=[0,1,2,3,4,5])
rating_dist = rating_bins.value_counts().sort_index()
common_rating = rating_dist.idxmax()
avg_votes = df["Votes"].mean()

print("TASK 1: RESTAURANT RATINGS")
print("Most common rating range:", common_rating)
print("Average votes:", round(avg_votes, 2))
print("=" * 50)

top_combinations = df["Cuisines"].value_counts().head(5)
high_rated_combinations = df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(5)

print("TASK 2: CUISINE COMBINATIONS")
print("Most common combinations:")
for c in top_combinations.index:
    print(c, ":", top_combinations[c])
print("Highest rated combinations:")
for c in high_rated_combinations.index:
    print(c, ":", round(high_rated_combinations[c], 2))
print("=" * 50)

top_city_clusters = df["City"].value_counts().head(5)

print("TASK 3: GEOGRAPHIC ANALYSIS")
for city in top_city_clusters.index:
    print(city, ":", top_city_clusters[city])
print("=" * 50)

chain_counts = df["Restaurant Name"].value_counts()
chains = chain_counts[chain_counts > 1].head(5)
chain_analysis = df[df["Restaurant Name"].isin(chains.index)].groupby(
    "Restaurant Name")[["Aggregate rating", "Votes"]].mean()

print("TASK 4: RESTAURANT CHAINS")
for chain in chain_analysis.index:
    print(
        chain,
        "Rating:", round(chain_analysis.loc[chain, "Aggregate rating"], 2),
        "Votes:", round(chain_analysis.loc[chain, "Votes"], 2)
    )

print("=" * 50)
print("LEVEL 2 COMPLETED")
