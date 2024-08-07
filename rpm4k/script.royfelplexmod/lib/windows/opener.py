from __future__ import absolute_import

import six
from plexnet import playqueue, plexapp, plexlibrary

from lib import util
from . import busy


def open(obj, **kwargs):
    if isinstance(obj, playqueue.PlayQueue):
        if busy.widthDialog(obj.waitForInitialization, None):
            if obj.type == 'audio':
                from . import musicplayer
                return handleOpen(musicplayer.MusicPlayerWindow, track=obj.current(), playlist=obj)
            elif obj.type == 'photo':
                from . import photos
                return handleOpen(photos.PhotoWindow, play_queue=obj, **kwargs)
            else:
                from . import videoplayer
                videoplayer.play(play_queue=obj, **kwargs)
                return ''
    elif isinstance(obj, six.string_types):
        key = obj
        if not obj.startswith('/'):
            key = '/library/metadata/{0}'.format(obj)
        return open(plexapp.SERVERMANAGER.selectedServer.getObject(key), **kwargs)
    elif obj.TYPE == 'episode':
        return episodeClicked(obj, **kwargs)
    elif obj.TYPE == 'movie':
        return playableClicked(obj, **kwargs)
    elif obj.TYPE in ('show'):
        return showClicked(obj, **kwargs)
    elif obj.TYPE in ('artist'):
        return artistClicked(obj, **kwargs)
    elif obj.TYPE in ('season'):
        return seasonClicked(obj, **kwargs)
    elif obj.TYPE in ('album'):
        return albumClicked(obj, **kwargs)
    elif obj.TYPE in ('photo',):
        return photoClicked(obj, **kwargs)
    elif obj.TYPE in ('photodirectory'):
        return photoDirectoryClicked(obj, **kwargs)
    elif obj.TYPE in ('track'):
        album = obj.album()
        if album:
            return trackClicked(obj, album=album, **kwargs)
        return trackClicked(obj, **kwargs)
    elif obj.TYPE in ('playlist'):
        return playlistClicked(obj, **kwargs)
    elif obj.TYPE in ('clip'):
        from . import videoplayer
        return videoplayer.play(video=obj)
    elif obj.TYPE in ('collection'):
        return collectionClicked(obj, **kwargs)
    elif obj.TYPE in ('Genre'):
        return genreClicked(obj, **kwargs)
    elif obj.TYPE in ('Director'):
        return directorClicked(obj, **kwargs)
    elif obj.TYPE in ('Role'):
        return actorClicked(obj, **kwargs)


def handleOpen(winclass, **kwargs):
    w = None
    try:
        autoPlay = kwargs.pop("auto_play", False)
        if autoPlay and hasattr(winclass, "doAutoPlay"):
            w = winclass.create(show=False, **kwargs)
            if w.doAutoPlay():
                w.modal()
        else:
            w = winclass.open(**kwargs)
        return w.exitCommand or ''
    except AttributeError:
        pass
    except util.NoDataException:
        raise
    finally:
        del w
        util.garbageCollect()

    return ''


def playableClicked(playable, **kwargs):
    from . import preplay
    return handleOpen(preplay.PrePlayWindow, video=playable, **kwargs)


def episodeClicked(episode, **kwargs):
    from . import episodes
    return handleOpen(episodes.EpisodesWindow, episode=episode, **kwargs)


def showClicked(show, **kwargs):
    from . import subitems
    return handleOpen(subitems.ShowWindow, media_item=show, **kwargs)


def artistClicked(artist, **kwargs):
    from . import subitems
    return handleOpen(subitems.ArtistWindow, media_item=artist, **kwargs)


def seasonClicked(season, **kwargs):
    from . import episodes
    return handleOpen(episodes.EpisodesWindow, season=season, **kwargs)


def albumClicked(album, **kwargs):
    from . import tracks
    return handleOpen(tracks.AlbumWindow, album=album, **kwargs)


def photoClicked(photo, **kwargs):
    from . import photos
    return handleOpen(photos.PhotoWindow, photo=photo, **kwargs)


def trackClicked(track, **kwargs):
    from . import musicplayer
    return handleOpen(musicplayer.MusicPlayerWindow, track=track, **kwargs)


def photoDirectoryClicked(photodirectory, **kwargs):
    return sectionClicked(photodirectory, **kwargs)


def playlistClicked(pl, **kwargs):
    from . import playlist
    return handleOpen(playlist.PlaylistWindow, playlist=pl, **kwargs)


def collectionClicked(collection, **kwargs):
    return sectionClicked(collection, **kwargs)


def sectionClicked(section, filter_=None, **kwargs):
    from . import library
    library.ITEM_TYPE = section.TYPE
    key = section.key
    if not key.isdigit():
        key = section.getLibrarySectionId()
    viewtype = util.getSetting('viewtype.{0}.{1}'.format(section.server.uuid, key))
    if section.TYPE in ('artist', 'photo', 'photodirectory'):
        default = library.VIEWS_SQUARE.get(viewtype)
        return handleOpen(
            library.LibraryWindow, windows=library.VIEWS_SQUARE.get('all'), default_window=default, section=section, filter_=filter_, **kwargs
        )
    else:
        default = library.VIEWS_POSTER.get(viewtype)
        return handleOpen(
            library.LibraryWindow, windows=library.VIEWS_POSTER.get('all'), default_window=default, section=section, filter_=filter_, **kwargs
        )


def genreClicked(genre, **kwargs):
    section = plexlibrary.LibrarySection.fromFilter(genre)
    filter_ = {'type': genre.FILTER, 'display': 'Genre', 'sub': {'val': genre.id, 'display': genre.tag}}
    return sectionClicked(section, filter_, **kwargs)


def directorClicked(director, **kwargs):
    section = plexlibrary.LibrarySection.fromFilter(director)
    filter_ = {'type': director.FILTER, 'display': 'Director', 'sub': {'val': director.id, 'display': director.tag}}
    return sectionClicked(section, filter_, **kwargs)


def actorClicked(actor, **kwargs):
    section = plexlibrary.LibrarySection.fromFilter(actor)
    filter_ = {'type': actor.FILTER, 'display': 'Actor', 'sub': {'val': actor.id, 'display': actor.tag}}
    return sectionClicked(section, filter_, ignoreLibrarySettings=True, **kwargs)
