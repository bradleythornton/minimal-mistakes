---
layout: archive
permalink: /walkthroughs/
title: "Walkthroughs"
author_profile: false
---
hello
{% include base_path %}
{% include group-by-array collection=site.posts field="categories" %}

{% for category = walkthroughs %}
  {% assign posts = group_items[forloop.index0] %}
  <h2 id="{{ category | slugify }}" class="archive__subtitle">{{ category }}</h2>
  {% for post in posts %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}
