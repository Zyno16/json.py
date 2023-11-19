import json
data = '''{
"name" : "chuck",
"phone" :{
"type" : "int1",
"number" : "+1 724 303 4456"
},
"email" : {
"hide" : "yes"
}
}'''
info = json.loads(data)
print('name:',info["name"])
print('hide:',info["email"]["hide"])