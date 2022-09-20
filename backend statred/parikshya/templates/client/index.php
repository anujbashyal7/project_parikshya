<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="{% static 'css/navbar.css' %}">
    <link rel="stylesheet" href="{% static 'css/banner.css' %}">
    <link rel="stylesheet" href="{% static 'css/packages.css' %}">
    <link rel="stylesheet" href="{% static 'css/footer.css' %}">
    <link rel="stylesheet" href="{% static 'css/responsive.css' %}">
    <link rel="stylesheet" href="{% static 'css/fontawesome-free-6.0.0-beta3-web/css/all.css' %}">
    <link rel="stylesheet" href="{% static 'css/fontawesome-free-6.0.0-beta3-web/css/all.min.css' %}">
    <title>Parikshya</title>
</head>
<body>
{% include '../header.html' %}
{% include '../client/banner.html' %}
{% include '../client/packages.html' %}
{% include '../footer.html' %}
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>