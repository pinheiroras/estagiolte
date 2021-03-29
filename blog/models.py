from django.db import models
from django.utils.translation import ugettext_lazy as _

class Post(models.Model):
    '''Model definition for Post.'''

    title = models.CharField(_('Post'), max_length=50)
    content = models.TextField(_('Content'))
    is_publishable = models.BooleanField(_('Is Publishable ?'), default=False)
    created_at = models.DateTimeField(_('Created at '),auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at '),auto_now=True)

    class Meta:
        '''Meta definition for Post.'''

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        '''Unicode representation of Post.'''
        return self.title
