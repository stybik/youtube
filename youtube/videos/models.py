from django.db import models


#  Video title, description, publishing datetime, thumbnails URLs
class Video(models.Model):
    """
    Model to store video_title, description and URL of the youtube video.
    """

    title = models.CharField("Title", max_length=300)
    description = models.TextField()
    published_on = models.DateTimeField()
    thumbnail_url = models.URLField(max_length=255, help_text="URL of the thumbnail")
    url = models.URLField(max_length=255, help_text="URL of the video")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"
        ordering = ["-published_on"]

    def __str__(self):
        return self.title