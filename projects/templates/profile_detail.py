<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
</head>

<body>
    <h2>{{ profile.name }}</h2>
    <p>GitHub: {{ profile.github }}</p>
    <p>LinkedIn: {{ profile.linkedin }}</a></p>
    <p>Bio: {{ profile.bio }}</p>

    <h3>Projetos</h3>
    <ul>
        {% for project in profile.projects.all %}
        <p>{{ project.name }}</p>
        <p>Description: {{ project.description }}</p>
        <p>Github URL: {{ project.github_url }}</p>
        <p>Keyword: {{ project.keyword }}</p>
        <p>Key Skill: {{ project.key_skill }}</p>
        {% endfor %}
    </ul>
    <h2>Certificados</h2>
    <ul>
        {% for certificate in profile.certificates.all %}
        <li>{{ certificate.name }} ({{ certificate.certifying_institution.name }})</li>
        {% endfor %}
    </ul>

    <h2>Instituições Certificadoras</h2>
    <ul>
        {% for institution in profile.certifying_institutions.all %}
        <li>{{ institution.name }} ({{ institution.url }})</li>
        {% endfor %}
    </ul>

</body>

</html>