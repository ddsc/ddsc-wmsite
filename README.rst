ddsc-wmsite
==========================================

Introduction

Usage, etc.


Post-nensskel setup TODO
------------------------

Here are some instructions on what to do after you've created the project with
nensskel.

- Fill in a short description on https://github.com/lizardsystem/ddsc-wmsite or
  https://github.com/nens/ddsc-wmsite if you haven't done so already.

- Use the same description in the ``setup.py``'s "description" field.

- Fill in your username and email address in the ``setup.py``, see the
  ``TODO`` fields.

- Check https://github.com/nens/ddsc-wmsite/settings/collaboration if the team
  "Nelen & Schuurmans" has access.

- Add a new jenkins job at
  http://buildbot.lizardsystem.nl/jenkins/view/djangoapps/newJob or
  http://buildbot.lizardsystem.nl/jenkins/view/libraries/newJob . Job name
  should be "ddsc-wmsite", make the project a copy of the existing "lizard-wms"
  project (for django apps) or "nensskel" (for libraries). On the next page,
  change the "github project" to ``https://github.com/nens/ddsc-wmsite/`` and
  "repository url" fields to ``git@github.com:nens/ddsc-wmsite.git`` (you might
  need to replace "nens" with "lizardsystem"). The rest of the settings should
  be OK.
