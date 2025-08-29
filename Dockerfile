# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create new Django project and configure the settings
RUN django-admin startproject core
RUN cp -r al_mirsal core

# Configure settings
RUN echo "AUTH_USER_MODEL = 'users.User'" >> core/settings.py
RUN echo "INSTALLED_APPS += [" >> core/settings.py
RUN echo "    'daphne'," >> core/settings.py
RUN echo "    'channels'," >> core/settings.py
RUN echo "    'al_mirsal'," >> core/settings.py
RUN echo "    'al_mirsal.api'," >> core/settings.py
RUN echo "    'al_mirsal.apps.channel'," >> core/settings.py
RUN echo "    'al_mirsal.apps.chats'," >> core/settings.py
RUN echo "    'al_mirsal.apps.groups'," >> core/settings.py
RUN echo "    'al_mirsal.apps.members'," >> core/settings.py
RUN echo "    'al_mirsal.apps.message'," >> core/settings.py
RUN echo "    'al_mirsal.apps.users'," >> core/settings.py
RUN echo "    'al_mirsal.ui'," >> core/settings.py
RUN echo "    'django_countries'," >> core/settings.py
RUN echo "    'phonenumber_field'," >> core/settings.py
RUN echo "    'django_filters'," >> core/settings.py
RUN echo "    'rest_wind'," >> core/settings.py
RUN echo "    'corsheaders'," >> core/settings.py
RUN echo "    'djoser'," >> core/settings.py
RUN echo "    'rest_framework'," >> core/settings.py
RUN echo "    'rest_framework.authtoken'," >> core/settings.py
RUN echo "]" >> core/settings.py
RUN echo "MIDDLEWARE += ['wagtail.contrib.redirects.middleware.RedirectMiddleware']" >> core/settings.py

# Setup URLConf
RUN echo "from django.conf import settings" >> core/urls.py
RUN echo "from django.conf.urls.i18n import i18n_patterns" >> core/urls.py
RUN echo "from django.conf.urls.static import static" >> core/urls.py
# URLPatterns
RUN echo "urlpatterns += [" >> core/urls.py
RUN echo "    path('', include('django.conf.urls.i18n'))," >> core/urls.py
RUN echo "    re_path( r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve')," >> core/urls.py
RUN echo "] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)" >> core/urls.py
# I18N
RUN echo "urlpatterns += i18n_patterns(" >> core/urls.py
RUN echo "    path('admin/', admin.site.urls)," >> core/urls.py
RUN echo "    path('api/', include('rest_framework.urls'))," >> core/urls.py
RUN echo "    path('api/', include('djoser.urls'))," >> core/urls.py
RUN echo "    path('api/', include('djoser.urls.authtoken'))," >> core/urls.py
RUN echo "    path('', include('django.contrib.auth.urls'))," >> core/urls.py
RUN echo "    path('api/', include('al_mirsal.api.urls'))," >> core/urls.py
RUN echo "    path('', include('al_mirsal.ui.urls', namespace='ui'))," >> core/urls.py
RUN echo ")" >> core/urls.py

# Run migrations
RUN cd core && python manage.py migrate


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
