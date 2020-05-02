
import urllib.request, json 
with urllib.request.urlopen("https://api.nytimes.com/svc/mostpopular/v2/viewed/30.json?api-key=LMg1bM6zwK70QCdg9Fp7GFBINUxWIB0e") as url:
    data = json.loads(url.read().decode())
    for key, value in data.items():
        # data_items = data.items()
        print (value[3])



# import collections
# data =[{ "rad_exam_id": 1, "modality": "CT", "exam_duration": 10 },
# { "rad_exam_id": 6, "modality": "US", "exam_duration": 9 },
# { "rad_exam_id": 7, "modality": "US", "exam_duration": 7 }]

# count = collections.Counter()
# for k in data:
# count[k["modality"]] += k["exam_duration"]

# print([{"label":n,"value":str(v)} for n,v in count.items()])