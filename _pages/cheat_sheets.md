---
layout: archive
permalink: /cheat_sheets/
title: "Cheat Sheet Articles"
header:
  overlay_color: "#333"
author_profile: false
---

{% capture written_year %}'None'{% endcapture %}
{% for post in site.categories.cheat_sheet %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% if year != written_year %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture written_year %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single.html %}
{% endfor %}
