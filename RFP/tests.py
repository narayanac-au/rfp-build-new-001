'''
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div>
        <img src="{% static 'images/KPMG_Logo.png' %}" height="106" width="220">
        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
        <p class="d-inline text-center ml-5 display-5"><strong>Smart Request for Proposal (RFP) Builder</strong></p>
    </div>
    <link rel="stylesheet" href="{% static 'css/font-awesome.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <div class="border-bottom"></div>
    <title>Document</title>
</head>
<body>
    <p class="ml-3 mt-2"><strong>Preview</strong></p>
    <div class="container border border-secondary">
    {% for d in data %}
        <h4>{{d.Questions}}</h4>
        {% ifequal d.Tick1 'on'  %}
            <h2>{{d.options1}}</h2>
        {% endifequal %}
        {% ifequal d.Tick2 'on'  %}
            <h2>{{d.options2}}</h2>
        {% endifequal %}
        {% ifequal d.Tick3 'on'  %}
            <h2>{{d.options3}}</h2>
        {% endifequal %}
    {% endfor %}
    </div>  
    <div class="container mt-5">
    <a class="btn btn-primary mt-5 d-inline" href="/first/hi/">Edit</a>
    <button type="submit" class="btn btn-primary float-right d-inline">Submit</button>
    </div>
</body>
</html>
'''
------------------------
<option selected>Open this select menu</option>