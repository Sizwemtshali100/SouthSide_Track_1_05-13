<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Forms</title>
</head>
<body>
    <h1>Forms</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    <hr>
    <h2>Submitted Forms:</h2>
    <ul>
        {% for form in forms %}
            <li>{{ form.title }} - {{ form.created_at }}</li>
        {% endfor %}
    </ul>
</body>
</html>
