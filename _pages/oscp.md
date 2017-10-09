---
layout: splash
classes:
  - landing
  - dark-theme
permalink: /oscp/
title: "OSCP"
author_profile: false
---

{% for post in site.categories.OSCP %} 
<article>
  {% if post.link %}
    <h2 class="link-post"><a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a> <a href="{{ post.link }}" target="_blank" title="{{ post.title }}"><i class="fa fa-link"></i></h2>
  {% else %}
    <h2><a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></h2>
    <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
  {% endif %}
</article>
{% endfor %}
