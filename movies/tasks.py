from celery import shared_task

from movies.omdb_integration import search_and_save

@shared_task
def search_and_save(search):
    return search_and_save(search)