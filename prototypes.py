import os
import sys

from django.conf import settings


BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='^w_ab(j-tj=3zv0)fs_xdh*1z_#g+j_)*uq*9(d_fq=nq326#u',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

