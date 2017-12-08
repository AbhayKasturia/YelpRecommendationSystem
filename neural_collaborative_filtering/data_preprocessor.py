
import json

res_businesss = set()
category = 'Restaurants'
with open('../data/business.json', 'r', encoding="utf8") as business:
    for line in business:
        bus = json.loads(line)
        categories = bus['categories']
        if category in categories:
            res_businesss.add(bus['business_id'])

print(len(res_businesss))
valid_users = set()
min_review_count = 20
with open('../data/user.json', 'r', encoding="utf8") as users:
    for line in users:
        user = json.loads(line)
        review_count = user['review_count']
        if review_count > min_review_count:
            valid_users.add(user['user_id'])

print(len(valid_users))
r_count = 0
sel_reviews = {}
with open('../data/review.json', 'r', encoding="utf8") as reviews:
    for line in reviews:
        review = json.loads(line)
        user_id = review['user_id']
        business_id = review['business_id']
        if user_id in valid_users and business_id in res_businesss:
            val = (business_id, review['stars'], review['date'])
            if user_id in sel_reviews:
                sel_reviews[user_id].append(val)
            else:
                sel_reviews[user_id] = [val]

for val in sel_reviews.values():
    val.sort(key=lambda r: r[2])

print(len(sel_reviews))

filter_sel_reviews = {}
bId_to_Int_Id = {}
uId_to_Int_Id = {}
user_count = 0
buss_count = 0
for user_id, values in sel_reviews.items():
    if len(values) >= 20:
        updated_val = []
        for val in values:
            if val[0] not in bId_to_Int_Id:
                bId_to_Int_Id[val[0]] = buss_count
                buss_count += 1
            updated_val.append((bId_to_Int_Id[val[0]], val[1], val[2]))
        uId_to_Int_Id[user_id] = user_count
        filter_sel_reviews[user_count] = updated_val
        user_count += 1

print(buss_count)
print(user_count)
with open('./yelp.train.rating', 'w', encoding="utf8") as train:
    for user_id, values in filter_sel_reviews.items():
        for val in values[:-1]:
            train.write("{}\t{}\t{}\t{}\n".format(user_id, val[0], val[1], val[2]))
    train.close()

print('Train file written')
with open('./yelp.test.rating', 'w', encoding="utf8") as train:
    for user_id, values in filter_sel_reviews.items():
        train.write("{}\t{}\t{}\t{}\n".format(user_id, values[-1][0], values[-1][1], values[-1][2]))
    train.close()

print('Test file written')

user_id_to_buss_ids = {}
all_business = set()
for user_id, values in filter_sel_reviews.items():
    business_ids = set([val[0] for val in values])
    all_business.update(business_ids)
    user_id_to_buss_ids[user_id] = business_ids

print(len(user_id_to_buss_ids))

negative_sample = {}
for user_id, values in filter_sel_reviews.items():
    business_ids = list(user_id_to_buss_ids[user_id].symmetric_difference(all_business))[0:99]
    negative_sample[user_id] = (values[-1][0], set(business_ids))

print(len(negative_sample))
with open('./yelp.test.negative', 'w', encoding="utf8") as negative:
    for key in sorted(negative_sample.keys()):
        values_tup = negative_sample[key]
        values = list(values_tup[1])
        negative.write("({},{})\t".format(key, values_tup[0]))
        for val in values[:-1]:
            negative.write("{}\t".format(val))
        negative.write("{}\n".format(values[-1]))
    negative.close()

print("Negative file written")