#!/usr/bin/env python3.4

import os
import re

from markdown import markdown


class SiteGenerator(object):

    TEMPLATES = os.path.normpath(os.path.join("..", "templates"))
    BASE_TEMPLATE = os.path.join(TEMPLATES, "base.html")
    INDEX_TEMPLATE = os.path.join(TEMPLATES, "index.html")
    VIDEO_TEMPLATE = os.path.join(TEMPLATES, "video.html")
    ABOUT_TEMPLATE = os.path.join("..", "README.md")

    INDEX = os.path.normpath(os.path.join("..", "htdocs", "index.html"))
    ABOUT = os.path.normpath(os.path.join("..", "htdocs", "about.html"))
    VIDEO = os.path.normpath(os.path.join("..", "htdocs", "{:02}.html"))

    def __init__(self):

        with open(self.BASE_TEMPLATE) as f:
            self.base_template = f.read()

        with open(self.INDEX_TEMPLATE) as f:
            self.index_template = f.read()

        with open(self.ABOUT_TEMPLATE) as f:
            self.about_template = "".join(f.readlines()[1:])

        with open(self.VIDEO_TEMPLATE) as f:
            self.video_template = f.read()

    def generate_index(self):
        self.write(
            self.INDEX,
            self.base_template.replace("{{ home_active }}", " active"),
            self.index_template,
            "Grandpa"
        )

    def generate_about(self):
        self.write(
            self.ABOUT,
            self.base_template.replace("{{ about_active }}", " active"),
            '<div class="about">{}</div>'.format(
                markdown(re.sub("^#", "", self.about_template)).replace(
                    "a href",
                    'a class="text-info" href'
                )
            ),
            "About"
        )

    def generate_videos(self):
        for i in range(40):
            if i == 4:
                continue

            nfo = os.path.join("..", "resources", "nfo", "{:02}.nfo".format(i))
            with open(nfo) as f:
                metadata = ""
                for line in f:
                    line = line.strip()
                    if line:
                        metadata += "<li>{}</li>".format(line)

            self.write(
                self.VIDEO.format(i),
                self.base_template,
                self.video_template.replace("{{ metadata }}", metadata).format(i=i),
                "Video {}".format(i)
            )

    @staticmethod
    def write(target, host, insert, title):
        """
        :param target: The path to the target file
        :param host: The template containing the marker we're replacing
        :param insert: What replaces the marker
        :param title: What goes into the <title> tag
        """
        content = host.replace(
            "{{ content }}", insert
        ).replace(
            "{{ title }}", title
        ).replace(
            "{{ home_active }}", ""
        ).replace(
            "{{ about_active }}", ""
        )

        with open(target, "w") as f:
            f.write(content)


if __name__ == "__main__":
    g = SiteGenerator()
    g.generate_index()
    g.generate_about()
    g.generate_videos()
