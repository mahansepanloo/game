from celery import shared_task
from accounts.models import Player



@shared_task(bind=True, default_retry_delay= 5)
def restart(self):
    try:
        player = Player.objects.all()
        for player in player:
            player.limit = 3
            player.save()

    except Exception as e:
        return self.retry(exc=e,max_retries=10)