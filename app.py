import meilisearch
import json

client = meilisearch.Client('http://localhost:7700')

json_file = open('restaurants.json')
restaurants = json.load(json_file)
client.index('restaurants').add_documents(restaurants)

client.index('restaurants').update_filterable_attributes([
    '_geo', 'rating'
])
client.index('restaurants').update_sortable_attributes([
    'rating'
])
client.index('restaurants').update_ranking_rules([
    'rating:desc'
])

query = input('Enter your search query: ')
results = client.index('restaurants').search(query, {
    'filter': '_geoRadius(37.7749,-122.4194, 3000)'
})


with open("results.json", 'w') as f:
    json.dump(results, f)
