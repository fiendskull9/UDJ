from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('udj.auth',
    (r'^auth/?$', 'authenticate'),
)

urlpatterns += patterns('udj.views.library',
  (r'^users/(?P<user_id>\d+)/library/songs$', 'addSongsToLibrary'),
  (
    r'^users/(?P<user_id>\d+)/library/(?P<lib_id>\d+)$', 
    'deleteSongFromLibrary'
  ),
  (r'^users/(?P<user_id>\d+)/library$', 'deleteEntireLibrary'),
) 

urlpatterns += patterns('udj.views.event',
  (r'^events/(?P<latitude>-?\d+\.\d+)/(?P<longitude>-?\d+\.\d+)$',
    'getNearbyEvents'),
  (r'^events/event$', 'createEvent'),
  (r'^events/(?P<event_id>\d+)$', 'endEvent'),
  (r'^events/(?P<event_id>\d+)/user$', 'joinEvent'),
  (r'^events/(?P<event_id>\d+)/(?P<user_id>\d+)$', 'leaveEvent'),
  (r'^events/(?P<event_id>\d+)/available_music$', 'availableMusic'),
  (r'^events/(?P<event_id>\d+)/available_music/random_songs$', 
    'getRandomMusic'),
  (r'^events/(?P<event_id>\d+)/available_music/(?P<song_id>\d+)$', 
    'removeFromAvailableMusic'),
  (r'^events/(?P<event_id>\d+)/current_song$', 
    'currentSong'),
)
urlpatterns += patterns('udj.views.activeplaylist',
  (r'^events/(?P<event_id>\d+)/active_playlist$', 
    'getActivePlaylist'),
  (r'^events/(?P<event_id>\d+)/active_playlist/songs$', 
    'addToPlaylist'),
  (r'^events/(?P<event_id>\d+)/active_playlist/(?P<playlist_id>\d+)/upvote$', 
    'voteSongUp'),
  (r'^events/(?P<event_id>\d+)/active_playlist/(?P<playlist_id>\d+)/downvote$', 
    'voteSongDown'),
)
